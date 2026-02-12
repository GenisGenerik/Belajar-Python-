from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.matkul import (
    CreateMatkul,
    UpdateMatkul,
    MatkulRespons
)
from services import matkul_service

router = APIRouter(prefix="/matkuls", tags=["Matkuls"])

@router.get("/", response_model=list[MatkulRespons])
def get_matkuls(
    db: Session = Depends(get_db)
):
    return matkul_service.all_matkul(db)

@router.post("/", response_model=MatkulRespons, status_code=status.HTTP_201_CREATED)
def create_matkul(
    dosen_id: int,
    matkul: CreateMatkul,
    db: Session = Depends(get_db)
):
    created = matkul_service.create_matkul(db, dosen_id, matkul)

    if created is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dosen tidak ditemukan"
        )

    return created

@router.put("/{matkul_id}", response_model=MatkulRespons)
def update_matkul(
    matkul_id: int,
    matkul: UpdateMatkul,
    db: Session = Depends(get_db)
):
    updated = matkul_service.edit_matkul(db, matkul_id, matkul)

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Matkul atau Dosen tidak ditemukan"
        )

    return updated

@router.delete("/{matkul_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_matkul(
    matkul_id: int,
    db: Session = Depends(get_db)
):
    deleted = matkul_service.delete_matkul(db, matkul_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Matkul tidak ditemukan"
        )

    return
