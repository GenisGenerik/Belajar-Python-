from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Integer,String
from database import Base


class User(Base) :
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    nama:Mapped[str] = mapped_column(String,nullable=False)
    umur:Mapped[int] = mapped_column(Integer,nullable=False)


class Hewan(Base) :
    __tablename__= "hewan"
    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    nama:Mapped[str] =  mapped_column(String,nullable=False)