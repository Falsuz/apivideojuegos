from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    # Obtener la lista de videojuegos
    videojuegos = obtener_videojuegos_api()
    # Pasar la lista de videojuegos a la plantilla HTML
    return render_template('index.html', videojuegos=videojuegos)


def obtener_videojuegos_api():
    # Hacer una solicitud GET a tu API en Render
    url = 'https://apivideojuegos.onrender.com/api/videojuegos'
    respuesta = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Devolver los datos de la API en formato JSON
        return respuesta.json()
    else:
        # Si la solicitud no fue exitosa, devolver un mensaje de error
        return []


if __name__ == '__main__':
    app.run(debug=True)
