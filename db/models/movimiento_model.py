from db import db

# Modelo Movimiento
class MovimientoModel(db.Model):
    __tablename__ = 'movimientos'
    id_movimiento = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)

    def __init__(self, descripcion):
        self.descripcion = descripcion
