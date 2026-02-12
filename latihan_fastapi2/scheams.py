from pydantic import BaseModel

class DosenRespons(BaseModel) :
    id:int
    nama:str
    matkul:list[MatkulSimple] = []
    class Config :
        from_attributes = True
        
class MatkulRespons(BaseModel) :
    id:int
    nama:str
    sks:int
    dosen:DosenSimple
    class Config :
        from_attributes = True


class MatkulSimple(BaseModel) :
    id:int
    nama:str
    sks:int



class DosenSimple(BaseModel) :
    id:int
    nama:str

class CreateDosen(BaseModel) :
    nama:str

class CreateMatkul(BaseModel) :
    nama:str
    sks:int

class UpdateMatkul(BaseModel) :
    nama:str
    sks:int
    dosen_id:int

class UpdateDosen(BaseModel) :
    nama:str
