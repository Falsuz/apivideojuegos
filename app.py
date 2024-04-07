from flask import Flask, request, jsonify, render_template, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://videogames_x44n_user:CCFK749Mn5CGtOMYnrWdp7lbDJ6lFyDk@dpg-co9huv4f7o1s739948s0-a.oregon-postgres.render.com/videogames_x44n'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Videojuego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    desarrollador = db.Column(db.String(120), nullable=False)
    anioLanzamiento = db.Column(db.String(120), nullable=False)
    plataforma = db.Column(db.String(120), nullable=False)
    clasificacion = db.Column(db.String(120), nullable=False)
    urlImagen = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<Videojuego {self.titulo}>"

@app.route('/create', methods=['GET'])
def create_table():
    db.create_all()
    return 'Tabla creada'

# en esta estructura devuelvo los videojuegos existentes
@app.route('/videojuegos', methods=['GET'])
def get_videojuegos():
    videojuegos = Videojuego.query.all()
    videojuegos_list = []
    for juego in videojuegos:
        videojuego_data = {
            'id': juego.id,
            'titulo': juego.titulo,
            'desarrollador': juego.desarrollador,
            'anio_lanzamiento': juego.anioLanzamiento,
            'plataforma': juego.plataforma,
            'clasificacion': juego.clasificacion,
            'urlImagen': juego.urlImagen
        }
        videojuegos_list.append(videojuego_data)
    return jsonify({"videojuegos": videojuegos_list})

@app.route('/videojuegos/<int:id>', methods=['GET'])
def get_videojuego(id):
    videojuego = Videojuego.query.get_or_404(id)
    videojuego_data = {
        'id': videojuego.id,
        'titulo': videojuego.titulo,
        'desarrollador': videojuego.desarrollador,
        'anio_lanzamiento': videojuego.anioLanzamiento,
        'plataforma': videojuego.plataforma,
        'clasificacion': videojuego.clasificacion,
        'urlImagen': videojuego.urlImagen
    }
    return jsonify({"videojuego": videojuego_data})

@app.route('/videojuegos', methods=['POST'])
def add_videojuego():
    data = request.json
    if not all(key in data for key in ['titulo', 'desarrollador', 'anio_lanzamiento', 'plataforma', 'clasificacion', 'urlImagen']):
        abort(400, 'Faltan campos en la solicitud')
    videojuego = Videojuego(titulo=data['titulo'], desarrollador=data['desarrollador'], anioLanzamiento=data['anio_lanzamiento'], plataforma=data['plataforma'], clasificacion=data['clasificacion'], urlImagen=data['urlImagen'])
    db.session.add(videojuego)
    db.session.commit()
    return jsonify({'message': 'Videojuego agregado correctamente'}), 201

@app.route('/videojuegos/<int:id>', methods=['DELETE'])
def delete_videojuego(id):
    videojuego = Videojuego.query.get_or_404(id)
    db.session.delete(videojuego)
    db.session.commit()
    return jsonify({'message': 'Videojuego eliminado correctamente'}), 200

@app.route('/')
def index():
    return 'API Videojuegos'

if __name__ == "__main__":
    app.run(debug=True, port=5001)
