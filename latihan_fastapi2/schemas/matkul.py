from pydantic import BaseModel


class MatkulSimple(BaseModel):
    id: int
    nama: str
    sks: int

    class Config:
        from_attributes = True


class MatkulRespons(BaseModel):
    id: int
    nama: str
    sks: int
    dosen_id: int 

    class Config:
        from_attributes = True


class CreateMatkul(BaseModel):
    nama: str
    sks: int


class UpdateMatkul(BaseModel):
    nama: str
    sks: int
    dosen_id: int
