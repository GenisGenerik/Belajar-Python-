from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.dosen import (
    CreateDosen,
    UpdateDosen,
    DosenRespons,
    DosenListResponse
)
from services import dosen_service

router = APIRouter(prefix="/dosens", tags=["Dosens"])

@router.get("/", response_model=DosenListResponse)
def get_dosens(
    last_id: int | None = None,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    data, next_cursor = dosen_service.all_dosen(db, last_id, limit)

    return DosenListResponse(
        data=data,
        next_cursor=next_cursor
    )
@router.post("/", response_model=DosenRespons, status_code=status.HTTP_201_CREATED)
def create_dosen(
    dosen: CreateDosen,
    db: Session = Depends(get_db)
):
    return dosen_service.create_dosen(db, dosen)
@router.put("/{dosen_id}", response_model=DosenRespons)
def update_dosen(
    dosen_id: int,
    dosen: UpdateDosen,
    db: Session = Depends(get_db)
):
    updated = dosen_service.update_dosen(db, dosen_id, dosen)

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dosen tidak ditemukan"
        )

    return updated

@router.delete("/{dosen_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dosen(
    dosen_id: int,
    db: Session = Depends(get_db)
):
    deleted = dosen_service.delete_dosen(db, dosen_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Dosen tidak ditemukan"
        )

    return
