import datetime
from xmlrpc.client import DateTime
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column
from models import BaseModel

class AtletaModel():
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key = True)
    nome: Mapped[str] = mapped_column(String(50), nullable = False)
    cpf: Mapped[str] = mapped_column(String(11), nullable = False)
    idade: Mapped[str] = mapped_column(Integer, nullable = False)
    peso: Mapped[float] = mapped_column(Float, nullable = False)
    altura: Mapped[float] = mapped_column(Float, nullable = False)
    sexo: Mapped[str] = mapped_column(String(1), nullable = False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable = False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates = 'atleta')
    categoria_id = Mapped[int] = mapped_column(ForeighKey('categorias.pk_id'))
    
    