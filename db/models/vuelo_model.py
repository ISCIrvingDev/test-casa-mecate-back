# from app import db
from db import db

from db.models.aeropuerto_model import AeropuertoModel as Aeropuerto
from db.models.aerolinea_model import AerolineaModel as Aerolinea
from db.models.movimiento_model import MovimientoModel as Movimiento

# Modelo Vuelo
class VueloModel(db.Model):
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
