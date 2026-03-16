from sqlalchemy import Column, Integer, String, Enum, Text, ForeignKey
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"
    id_cat = Column(Integer, primary_key=True, index=True)
    nom_cat = Column(String(50), nullable=False)

class Vehiculo(Base):
    __tablename__ = "vehiculos"
    id_v = Column(Integer, primary_key=True, index=True)
    tipo_v = Column(Enum('Moto', 'Cicla'), nullable=False)
    marca = Column(String(30))
    modelo = Column(String(20))
    placa = Column(String(10), default='N/A')

class Norma(Base):
    __tablename__ = "normas"
    id_n = Column(Integer, primary_key=True, index=True)
    id_cat = Column(Integer, ForeignKey("categorias.id_cat"))
    descripcion_norma = Column(Text)
    aplica_a = Column(Enum('Moto', 'Cicla', 'Ambos'))

class Componente(Base):
    __tablename__ = "componentes"
    id_com = Column(Integer, primary_key=True, index=True)
    nombre_componente = Column(String(50))
    estado_sugerido = Column(String(100))
    id_v = Column(Integer, ForeignKey("vehiculos.id_v"))

class CasoVial(Base):
    __tablename__ = "casos_viales"
    id_cas = Column(Integer, primary_key=True, index=True)
    problema_comun = Column(Text)
    solucion_legal = Column(Text)
    id_n = Column(Integer, ForeignKey("normas.id_n"))
