from typing import Tuple, List
from sqlalchemy.orm import Session, subqueryload
from models.dosen import Dosen
from schemas.dosen import CreateDosen, UpdateDosen


def all_dosen(
    db: Session,
    last_id: int | None,
    limit: int
) -> Tuple[List[Dosen], int | None]:

    query = (
        db.query(Dosen)
        .options(subqueryload(Dosen.matkul))
        .order_by(Dosen.id)
    )

    if last_id is not None:
        query = query.filter(Dosen.id > last_id)

    data = query.limit(limit).all()
    next_cursor = data[-1].id if data else None

    return data, next_cursor


def create_dosen(db: Session, dosen: CreateDosen) -> Dosen:
    try:
        data = Dosen(nama=dosen.nama)
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
    except Exception:
        db.rollback()
        raise


def update_dosen(
    db: Session,
    dosen_id: int,
    dosen: UpdateDosen
) -> Dosen | None:

    data = db.query(Dosen).filter(Dosen.id == dosen_id).first()

    if data is None:
        return None

    try:
        data.nama = dosen.nama
        db.commit()
        db.refresh(data)
        return data
    except Exception:
        db.rollback()
        raise



def delete_dosen(db: Session, dosen_id: int) -> bool:

    dosen = db.query(Dosen).filter(Dosen.id == dosen_id).first()

    if dosen is None:
        return False

    try:
        db.delete(dosen)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise

