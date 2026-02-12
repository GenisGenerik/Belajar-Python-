from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy import Integer,String
from database import Base



class Dosen(Base) :
    __tablename__ = "dosen"

    id:Mapped[int] = mapped_column(Integer,primary_key=True,index=True)
    nama:Mapped[str] = mapped_column(String,nullable=False)
    
    matkul = relationship("Matkul",back_populates="dosen",cascade="all,delete")