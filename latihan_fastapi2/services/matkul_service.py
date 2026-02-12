from typing import List
from sqlalchemy.orm import Session
from models.matkul import Matkul
from models.dosen import Dosen
from schemas.matkul import CreateMatkul, UpdateMatkul


def all_matkul(db: Session) -> List[Matkul]:
    return db.query(Matkul).all()


def create_matkul(
    db: Session,
    dosen_id: int,
    matkul: CreateMatkul
) -> Matkul | None:

    dosen = db.query(Dosen).filter(Dosen.id == dosen_id).first()

    if dosen is None:
        return None

    try:
        data = Matkul(
            nama=matkul.nama,
            sks=matkul.sks,
            dosen_id=dosen_id
        )
        db.add(data)
        db.commit()
        db.refresh(data)
        return data
    except Exception:
        db.rollback()
        raise


def edit_matkul(
    db: Session,
    matkul_id: int,
    matkul: UpdateMatkul
) -> Matkul | None:

    data = db.query(Matkul).filter(Matkul.id == matkul_id).first()

    if data is None:
        return None

    dosen = db.query(Dosen).filter(Dosen.id == matkul.dosen_id).first()

    if dosen is None:
        return None

    try:
        data.nama = matkul.nama
        data.sks = matkul.sks
        data.dosen_id = matkul.dosen_id

        db.commit()
        db.refresh(data)

        return data
    except Exception:
        db.rollback()
        raise


def delete_matkul(
    db: Session,
    matkul_id: int
) -> bool:

    matkul = db.query(Matkul).filter(Matkul.id == matkul_id).first()

    if matkul is None:
        return False

    try:
        db.delete(matkul)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise
