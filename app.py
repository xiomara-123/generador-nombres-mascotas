from flask import Flask, render_template, request, url_for
import os
import random

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Asegurar que la carpeta de uploads existe
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Diccionarios de nombres
nombres_machos = {
    "chistoso": ["Firulais", "Chicharrón", "Pelusa", "Toby", "Lomito"],
    "tierno": ["Osito", "Milo", "Copito", "Doki", "Teddy"],
    "rudo": ["Rex", "Thor", "Brutus", "Rocky", "Spartacus"]
}

nombres_hembras = {
    "chistoso": ["Chispa", "Lulu", "Bolita", "Sopita", "Pompón"],
    "tierno": ["Mimi", "Luna", "Canela", "Dulce", "Nina"],
    "rudo": ["Athena", "Kira", "Xena", "Mamba", "Electra"]
}

def generar_nombres(genero, estilo, cantidad=3):
    if genero == "macho":
        nombres = nombres_machos.get(estilo, [])
    elif genero == "hembra":
        nombres = nombres_hembras.get(estilo, [])
    else:
        return []

    return random.sample(nombres, min(cantidad, len(nombres)))  # Elegimos hasta 3 nombres aleatorios


@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    nombres_generados = None

    if request.method == "POST":
        file = request.files["file"]
        genero = request.form["gender"]
        estilo = request.form["style"]
        
        if file:
            filename = file.filename
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            # Ruta accesible desde el navegador
            image_url = url_for("static", filename=f"uploads/{filename}")

            # Generar nombres según el género y el estilo
            nombres_generados = generar_nombres(genero, estilo, cantidad=3)

    return render_template("index.html", image_url=image_url, nombres_generados=nombres_generados)


if __name__ == "__main__":
    app.run(debug=True)
