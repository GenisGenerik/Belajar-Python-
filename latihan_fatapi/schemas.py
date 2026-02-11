from pydantic import BaseModel


class UserRespond(BaseModel) :
    id:int
    nama:str
    umur:int

class CreateUser(BaseModel) :
    nama:str
    umur:int

class UpdateUser(BaseModel) :
    nama:str
    umur:int

class HewanRespon(BaseModel) :
    nama:str
class CreateHewan(BaseModel) :
    nama:str
class UpdateHewan(BaseModel) :
    nama:str
