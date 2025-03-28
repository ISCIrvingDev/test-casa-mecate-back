from db import db

# Modelo Aerolinea
class AerolineaModel(db.Model):
    __tablename__ = 'aerolineas'
    id_aerolinea = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nombre_aerolinea = db.Column(db.String(25), nullable=False)

    def __init__(self, nombre_aerolinea):
        self.nombre_aerolinea = nombre_aerolinea
