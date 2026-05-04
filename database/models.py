# database/models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_whatsapp = Column(String(50), unique=True, nullable=False)
    nombre = Column(String(100), nullable=True)
    modulo_actual = Column(Integer, default=1)
    sesion_activa = Column(String(50), default="inicio")
    activo = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    ultima_interaccion = Column(DateTime, default=datetime.utcnow)
    recordatorios_activados = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Paciente {self.nombre} - {self.numero_whatsapp} - Modulo {self.modulo_actual}>"


class RegistroMensaje(Base):
    __tablename__ = "registro_mensajes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_whatsapp = Column(String(50), nullable=False)
    direccion = Column(String(10), nullable=False)
    contenido = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Mensaje [{self.direccion}] {self.numero_whatsapp}: {self.contenido[:40]}>"
    