from config.config import env
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random
import uuid
import enum
app = env['APP']
app.config['SQLALCHEMY_DATABASE_URI'] = env['SQL_CONF']['DB_URI']
db = SQLAlchemy(app)

class Participantes(db.Model):
    __tablename__ = 'participantes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.Text, nullable=False)
    codigo_estudiante = db.Column(db.String(120), nullable=False)
    genero = db.Column(db.String(10), nullable=True)
    imagen = db.Column(db.Text, nullable=True)
    activo = db.Column(db.Boolean, nullable=False, default=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

db.create_all()
