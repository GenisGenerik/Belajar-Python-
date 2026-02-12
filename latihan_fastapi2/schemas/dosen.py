from pydantic import BaseModel, Field, ConfigDict
from typing import  Optional
from schemas.matkul import MatkulSimple


class DosenSimple(BaseModel):
    id: int
    nama: str

    model_config = ConfigDict(from_attributes=True)


class DosenRespons(BaseModel):
    id: int
    nama: str
    matkul: list[MatkulSimple] = Field(default_factory=list[MatkulSimple])

    model_config = ConfigDict(from_attributes=True)


class DosenListResponse(BaseModel):
    data: list[DosenRespons]
    next_cursor: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class CreateDosen(BaseModel):
    nama: str


class UpdateDosen(BaseModel):
    nama: str
