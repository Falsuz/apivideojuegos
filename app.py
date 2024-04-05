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
        "url": "https://i.blogs.es/638318/super_mario_bros_logo/450_1000.webp"
    },
    {
        "id": 2,
        "titulo": "The Legend of Zelda: Ocarina of Time",
        "desarrollador": "Nintendo",
        "anio_lanzamiento": 1998,
        "plataforma": "Nintendo 64",
        "clasificacion": "E (Everyone)"
        "url": "https://upload.wikimedia.org/wikipedia/en/5/57/The_Legend_of_Zelda_Ocarina_of_Time.jpg"
    },
    {
        "id": 3,
        "titulo": "Final Fantasy VII",
        "desarrollador": "Square Enix",
        "anio_lanzamiento": 1997,
        "plataforma": "PlayStation",
        "clasificacion": "T (Teen)"
        "url": "https://upload.wikimedia.org/wikipedia/en/c/c2/Final_Fantasy_VII_Box_Art.jpg"
    },
    {
        "id": 4,
        "titulo": "The Elder Scrolls V: Skyrim",
        "desarrollador": "Bethesda Game Studios",
        "anio_lanzamiento": 2011,
        "plataforma": "PC, PlayStation 3, Xbox 360",
        "clasificacion": "M (Mature)"
    },
    {
        "id": 5,
        "titulo": "Grand Theft Auto V",
        "desarrollador": "Rockstar North",
        "anio_lanzamiento": 2013,
        "plataforma": "PC, PlayStation 3, PlayStation 4, Xbox 360, Xbox One",
        "clasificacion": "M (Mature)"
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
