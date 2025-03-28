from flask import Flask, render_template, request, url_for
import os
import requests
import random

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Usa UNA de tus claves API
API_KEY = "TU_API_KEY_AQUI"
DOG_API_URL = "https://api.thedogapi.com/v1/images/upload"

# Asegurar que la carpeta de uploads existe
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Diccionario de nombres por raza
nombres_por_raza = {
    "Labrador Retriever": ["Max", "Buddy", "Charlie", "Milo", "Cooper"],
    "Bulldog": ["Rocky", "Bruno", "Duke", "Tank", "Zeus"],
    "Golden Retriever": ["Bailey", "Teddy", "Leo", "Rusty", "Marley"],
    "Chihuahua": ["Taco", "Chispa", "Luna", "Pepito", "Bella"],
}

def detectar_raza(image_path):
    """Envía la imagen a la API y obtiene la raza detectada."""
    with open(image_path, "rb") as image_file:
        headers = {"x-api-key": API_KEY}
        files = {"file": image_file}
        response = requests.post(DOG_API_URL, headers=headers, files=files)

    if response.status_code == 201:
        data = response.json()
        if "breeds" in data and len(data["breeds"]) > 0:
            return data["breeds"][0]["name"]  # Nombre de la raza detectada
    return "Desconocida"

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    nombres_generados = None
    raza_detectada = None

    if request.method == "POST":
        file = request.files["file"]
        
        if file:
            filename = file.filename
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)
            image_url = url_for("static", filename=f"uploads/{filename}")

            # Detectar raza
            raza_detectada = detectar_raza(file_path)

            # Generar nombres según la raza detectada
            nombres_generados = nombres_por_raza.get(raza_detectada, ["Firulais", "Pelusa", "Lucky"])

    return render_template("index.html", image_url=image_url, nombres_generados=nombres_generados, raza_detectada=raza_detectada)

if __name__ == "__main__":
    app.run(debug=True)
