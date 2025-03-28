from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegurar que la carpeta de imágenes existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    nombres_generados = []
    
    if request.method == "POST":
        # Manejo de archivo subido
        file = request.files["file"]
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            image_url = url_for('static', filename=f'uploads/{file.filename}')
        
        # Obtener género y estilo
        gender = request.form["gender"]
        style = request.form["style"]

        # Generar nombres de ejemplo
        nombres_macho = {
            "chistoso": ["Chispas", "Firulais", "Bigotes"],
            "tierno": ["Peluchín", "Doki", "Copito"],
            "rudo": ["Rocky", "Thor", "Spike"]
        }

        nombres_hembra = {
            "chistoso": ["Lulú", "Princesa", "Manchitas"],
            "tierno": ["Dulce", "Mimi", "Canela"],
            "rudo": ["Xena", "Pantera", "Fiera"]
        }

        # Elegir nombres basados en la selección
        if gender == "macho":
            nombres_generados = nombres_macho.get(style, [])
        else:
            nombres_generados = nombres_hembra.get(style, [])

    return render_template("index.html", image_url=image_url, nombres_generados=nombres_generados)

if __name__ == "__main__":
    app.run(debug=True)
