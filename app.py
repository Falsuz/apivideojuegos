from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo
videojuegos = [
    {
        "id": 1,
        "titulo": "Super Mario Bros.",
        "desarrollador": "Nintendo",
        "anio_lanzamiento": 1985,
        "plataforma": "Nintendo Entertainment System",
        "clasificacion": "E (Everyone)"
    }
]

# Ruta para obtener todos los videojuegos
@app.route('/api/videojuegos', methods=['GET'])
def obtener_videojuegos():
    return jsonify({"videojuegos": videojuegos})

# Ruta para obtener un videojuego por su ID
@app.route('/api/videojuegos/<int:videojuego_id>', methods=['GET'])
def obtener_videojuego(videojuego_id):
    juego = next((juego for juego in videojuegos if juego["id"] == videojuego_id), None)
    if juego:
        return jsonify({"videojuego": juego})
    else:
        return jsonify({"mensaje": "Videojuego no encontrado"}), 404

# Ruta para agregar un nuevo videojuego
@app.route('/api/videojuegos', methods=['POST'])
def agregar_videojuego():
    nuevo_videojuego = request.json
    videojuegos.append(nuevo_videojuego)
    return jsonify({"mensaje": "Videojuego agregado correctamente"}), 201

@app.route('/')
def index():
    return('api videojuegos')

if __name__ == '__main__':
    app.run(debug=True)
