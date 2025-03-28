from db import db

# Modelo Aeropuerto
class AeropuertoModel(db.Model):
    __tablename__ = 'aeropuertos'
    id_aeropuerto = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre_aeropuerto = db.Column(db.String(25), nullable=False)

    def __init__(self, nombre_aeropuerto):
        self.nombre_aeropuerto = nombre_aeropuerto
