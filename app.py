from flask import Flask, jsonify, request

# CORS
from flask_cors import CORS

# Services
from services import app_services

# DB
from db import db
from db.config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func, extract

# Modelos - Inicio
class Aeropuerto(db.Model):
    __tablename__ = 'aeropuertos'
    id_aeropuerto = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre_aeropuerto = db.Column(db.String(25), nullable=False)

    def __init__(self, nombre_aeropuerto):
        self.nombre_aeropuerto = nombre_aeropuerto

class Aerolinea(db.Model):
    __tablename__ = 'aerolineas'
    id_aerolinea = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre_aerolinea = db.Column(db.String(25), nullable=False)

    def __init__(self, nombre_aerolinea):
        self.nombre_aerolinea = nombre_aerolinea

class Movimiento(db.Model):
    __tablename__ = 'movimientos'
    id_movimiento = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)

    def __init__(self, descripcion):
        self.descripcion = descripcion

class Vuelo(db.Model):
    __tablename__ = 'vuelos'
    id_vuelo = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Se puede añadir una PK adicional si se requiere
    id_aerolinea = db.Column(db.Integer, db.ForeignKey('aerolineas.id_aerolinea'), nullable=False)
    id_aeropuerto = db.Column(db.Integer, db.ForeignKey('aeropuertos.id_aeropuerto'), nullable=False)
    id_movimiento = db.Column(db.Integer, db.ForeignKey('movimientos.id_movimiento'), nullable=False)
    # id_dia = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    id_dia = db.Column(db.Date, nullable=False, default=db.func.now())

    def __init__(self, id_aerolinea, id_aeropuerto, id_movimiento):
        self.id_aerolinea = id_aerolinea
        self.id_aeropuerto = id_aeropuerto
        self.id_movimiento = id_movimiento

    # Relaciones opcionales para acceder a los objetos relacionados desde la tabla "vuelos"
    aerolinea = db.relationship('Aerolinea', backref='vuelos')
    aeropuerto = db.relationship('Aeropuerto', backref='vuelos')
    movimiento = db.relationship('Movimiento', backref='vuelos')

# Modelos - Fin

app = Flask(__name__)
app.config.from_object(Config)
# db = SQLAlchemy(app)
db.init_app(app)
with app.app_context():
    db.create_all()  # Crear tablas en la base de datos

    print("Registros creados con éxito")

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

# http://127.0.0.1:3000/
@app.route("/")
def home():
    return jsonify({
        "msn": "It Works"
    })

# Task 1.1) http://127.0.0.1:3000/get-answered-responses
@app.route("/get-answered-responses")
def get_answered_responses():
    try:
        data = app_services.get_data()
        answered_responses, no_answered_responses = app_services.get_answered_responses(data)

        return jsonify({
            "msn": "Ok",
            "answeredResponses": answered_responses,
            "noAnsweredResponses": no_answered_responses
        })
    except:
        return jsonify({
            "msn": "An exception occurred"
        })

# Task 1.2) http://127.0.0.1:3000/get-answer-highest-reputation
@app.route("/get-answer-highest-reputation")
def get_answer_highest_reputation():
    try:
        data = app_services.get_data()
        res = app_services.get_answer_highest_reputation(data)

        return jsonify({
            "msn": "Ok",
            "reputation": res["reputation"],
            "title": res["title"],
            "displayName": res["display_name"],
            "link": res["link"]
        })
    except:
        return jsonify({
            "msn": "An exception occurred"
        })

# Task 1.3) http://127.0.0.1:3000/get-answer-fewest-views
@app.route("/get-answer-fewest-views")
def get_answer_fewest_views():
    try:
        data = app_services.get_data()
        res = app_services.get_answer_fewest_views(data)

        return jsonify({
            "msn": "Ok",
            "questionId": res["question_id"],
            "title": res["title"],
            "viewCount": res["view_count"],
            "displayName": res["display_name"],
            "isAnswered": res["is_answered"],
            "link": res["link"]
        })
    except:
        return jsonify({
            "msn": "An exception occurred"
        })

# Task 1.4) http://127.0.0.1:3000/get-oldest-and-newest-answer
@app.route("/get-oldest-and-newest-answer")
def get_oldest_and_newest_answer():
    try:
        data = app_services.get_data()
        oldest_answer, newest_answer = app_services.get_oldest_and_newest_answer(data)

        return jsonify({
            "msn": "Ok",
            "oldestAnswer": {
                "title": oldest_answer["title"],
                "creationDate": oldest_answer["creation_date"],
                "displayName": oldest_answer["display_name"],
                "link": oldest_answer["link"],
            },
            "newestAnswer": {
                "title": newest_answer["title"],
                "creationDate": newest_answer["creation_date"],
                "displayName": newest_answer["display_name"],
                "link": newest_answer["link"],
            },
        })
    except:
        return jsonify({
            "msn": "An exception occurred"
        })

# Task 2.1) http://127.0.0.1:3000/flights/airport-more-movements/2021
@app.route("/flights/airport-more-movements/<int:year>", methods=["GET"])
def airport_more_movements(year):
    try:
        # Realizar la consulta agregando filtros por año y agrupando por id_aeropuerto
        res = (
            db.session.query(Aeropuerto.nombre_aeropuerto, func.count(Vuelo.id_aeropuerto).label("total_movimientos"))
            .join(Vuelo, Aeropuerto.id_aeropuerto == Vuelo.id_aeropuerto)
            .filter(extract("year", Vuelo.id_dia) == year)  # Filtrar por año
            .group_by(Aeropuerto.nombre_aeropuerto)
            .order_by(func.count(Vuelo.id_aeropuerto).desc())  # Ordenar por total de movimientos
            .first()  # Obtener el aeropuerto con más movimientos
        )

        if res:
            nombre_aeropuerto, total_movimientos = res
            return jsonify({
                "msn": "Ok",
                "airportName": nombre_aeropuerto,
                "totalMovements": total_movimientos,
                "year": year
            })
        else:
            return jsonify({"message": f"No hay movimientos registrados para el {year}"}), 404
    except Exception as e:
        print(e)
        return jsonify({
            "msn": "An exception occurred"
        })

# Task 2.2) http://127.0.0.1:3000/flights/airline-more-flights/2021
@app.route('/flights/airline-more-flights/<int:year>', methods=['GET'])
def airline_more_flights(year):
    res = (
        db.session.query(
            Aerolinea.nombre_aerolinea,  # Nombre de la aerolínea
            func.count(Vuelo.id_aerolinea).label("total_vuelos")  # Conteo de vuelos
        )
        .join(Vuelo, Aerolinea.id_aerolinea == Vuelo.id_aerolinea)
        .filter(extract("year", Vuelo.id_dia) == year)  # Filtrar por año
        .group_by(Aerolinea.nombre_aerolinea)  # Agrupar por nombre de aerolínea
        .order_by(desc("total_vuelos"))  # Ordenar por cantidad de vuelos
        .first()  # Obtener la aerolínea con más vuelos
    )

    if res:
        nombre_aerolinea, total_vuelos = res
        return jsonify({
            "msn": "Ok",
            "airlineName": nombre_aerolinea,
            "totalFlights": total_vuelos,
            "year": year
        })
    else:
        return jsonify({"message": f"No hay vuelos registrados para el {year}"}), 404

# Task 2.3) http://127.0.0.1:3000/flights/date-more-flights
@app.route('/flights/date-more-flights', methods=['GET'])
def date_more_flights():
    # Consulta para contar vuelos agrupados por día y ordenar en orden descendente
    res = (
        db.session.query(
            Vuelo.id_dia,  # Fecha del vuelo
            func.count(Vuelo.id_dia).label("total_vuelos")  # Conteo de vuelos en esa fecha
        )
        .group_by(Vuelo.id_dia)  # Agrupar por día
        .order_by(desc("total_vuelos"))  # Ordenar por número de vuelos
        .first()  # Obtener el día con más vuelos
    )

    if res:
        dia, total_vuelos = res
        return jsonify({
            "msn": "Ok",
            "date": dia.strftime("%Y-%m-%d"),  # Convertir la fecha a formato legible
            "totalFlights": total_vuelos
        })
    else:
        return jsonify({"message": "No se han encontrado vuelos registrados"}), 404

# Task 2.4) http://127.0.0.1:3000/flights/airlines-more-flights
@app.route('/flights/airlines-more-flights', methods=['GET'])
def airlines_more_flights():
    # Consulta para obtener aerolíneas con más de 2 vuelos por día
    res = (
        db.session.query(
            Aerolinea.id_aerolinea,
            Aerolinea.nombre_aerolinea,
            Vuelo.id_dia,
            func.count(Vuelo.id_aerolinea).label("total_vuelos")
        )
        .join(Vuelo, Aerolinea.id_aerolinea == Vuelo.id_aerolinea)
        .group_by(Aerolinea.id_aerolinea, Aerolinea.nombre_aerolinea, Vuelo.id_dia)
        .having(func.count(Vuelo.id_aerolinea) > 2)  # Filtrar aerolíneas con más de 2 vuelos por día
        .order_by(Aerolinea.nombre_aerolinea, Vuelo.id_dia)  # Ordenar por nombre y día
        .all()  # Obtener todos los resultados
    )

    # Construcción de la lista de resultados
    aerolineas_vuelos = []
    for id_aerolinea, nombre_aerolinea, dia, total_vuelos in res:
        aerolineas_vuelos.append({
            "msn": "Ok",
            "idAerolinea": id_aerolinea,
            "airlineName": nombre_aerolinea,
            "date": dia.strftime("%Y-%m-%d"),  # Convertir fecha a formato legible
            "totalFlights": total_vuelos
        })

    if aerolineas_vuelos:
        return jsonify(aerolineas_vuelos)
    else:
        return jsonify({"message": "No se encontraron aerolineas con mas de 2 vuelos por dia"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=3000)
