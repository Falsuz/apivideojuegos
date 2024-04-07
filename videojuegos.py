from flask import Flask, jsonify, render_template, abort
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Obtener la lista de videojuegos
    videojuegos = obtener_videojuegos_api()
    # Pasar la lista de videojuegos a la plantilla HTML
    return render_template('index.html', videojuegos=videojuegos)


@app.route('/videojuego/<int:videojuego_id>')
def obtener_videojuego_por_id(videojuego_id):
    # Obtener el videojuego por su ID
    videojuego = obtener_videojuego_api(videojuego_id)
    # print(videojuego)
    if videojuego:
        # Renderizar la plantilla HTML del videojuego con los datos
        return render_template('videojuego.html', videojuego=videojuego)
    else:
        # Si no se encuentra el videojuego, devolver un error 404
        abort(404)


def obtener_videojuegos_api():
    # Hacer una solicitud GET a tu API en Render
    url = 'https://apivideojuegos.onrender.com/videojuegos'
    respuesta = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Devolver los datos de la API en formato JSON
        return respuesta.json()['videojuegos']
    else:
        # Si la solicitud no fue exitosa, devolver una lista vacía
        return []


def obtener_videojuego_api(videojuego_id):
    # Hacer una solicitud GET a tu API en Render para obtener el videojuego por su ID
    url = f'https://apivideojuegos.onrender.com/videojuegos/{videojuego_id}'
    respuesta = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if respuesta.status_code == 200:
        # Devolver los datos de la API en formato JSON
        return respuesta.json()['videojuego']
    else:
        # Si la solicitud no fue exitosa, devolver None
        return None

if __name__ == '__main__':
    app.run(debug=True)
