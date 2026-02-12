from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import scheams,model
from database import engine,SessionLocal



model.Base.metadata.create_all(bind = engine)
app = FastAPI()


def get_db() :
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()

@app.get("/dosens",response_model=list[scheams.DosenRespons]) 
def all_dosen(db:Session = Depends(get_db)) :
    data = db.query(model.Dosen).all()
    if not data :
        raise HTTPException(status_code=404,detail="Data Tidak ADA")
    return data

@app.get("/matkuls",response_model=list[scheams.MatkulRespons])
def all_matkul(db:Session = Depends(get_db)) :
    data = db.query(model.Matkul).all()
    if not data :
        raise HTTPException(status_code=404,detail="Matkul Tidak Ada")
    return data


@app.post("/dosen/",response_model=scheams.DosenRespons)
def create_dosen(dosen:scheams.CreateDosen,db:Session = Depends(get_db)) :
    data = model.Dosen(nama = dosen.nama)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


@app.post("/matkul/",response_model=scheams.MatkulRespons)
def create_matkul(dosen_id:int,matkul:scheams.CreateMatkul,db:Session = Depends(get_db)) :
    dosen = db.query(model.Dosen).filter(model.Dosen.id == dosen_id).first()
    if not dosen :
        raise HTTPException(status_code=404,detail="Dosen Tidak ada")
    data = model.Matkul(nama = matkul.nama,sks = matkul.sks,dosen_id = dosen_id)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

@app.put("/matkul/{matkul_id}",response_model=scheams.MatkulRespons) 
def edit_matkul(matkul_id:int,matkul:scheams.UpdateMatkul,db:Session = Depends(get_db)) :
    data = db.query(model.Matkul).filter(model.Matkul.id == matkul_id).first()
    if not data :
        raise HTTPException(status_code=404,detail="Maktul Tidak ada")
    dosen = db.query(model.Dosen).filter(model.Dosen.id == matkul.dosen_id).first()
    if not dosen :
        raise HTTPException(status_code=404,detail="Dosen Tidak ada")
    data.nama = matkul.nama
    data.sks = matkul.sks
    data.dosen_id = matkul.dosen_id
    data.dosen_id = matkul.dosen_id
    db.commit()
    db.refresh(data)
    return data

@app.put("/dosen/{dosen_id}",response_model=scheams.DosenRespons)
def update_dosen(dosen_id:int,dosen:scheams.UpdateDosen,db:Session = Depends(get_db)) :
    data = db.query(model.Dosen).filter(model.Dosen.id == dosen_id).first()
    if not data :
        raise HTTPException(status_code=404,detail="Dosen Tidak ada")
    data.nama = dosen.nama
    db.commit()
    db.refresh(data)
    return data

@app.delete("/dosen/{dosen_id}")
def delete_dosen(dosen_id:int,db:Session = Depends(get_db)) :
    dosen = db.query(model.Dosen).filter(model.Dosen.id == dosen_id).first()
    if not dosen :
        raise HTTPException(status_code=404,detail="Dosen Tidak ada")
    db.delete(dosen)
    db.commit()
    return {"Message" : " Dosen TELAH DI HAPUSUSSSU"}

@app.delete("/matkul/{matkul_id}")
def delete_matkul(matkul_id:int,db:Session = Depends(get_db)) :
    matkul = db.query(model.Matkul).filter(model.Matkul.id == matkul_id).first()
    if not matkul :
        raise HTTPException(status_code=404,detail="Dosen Tidak ada")
    db.delete(matkul)
    db.commit()
    return {"Message" : " Matkul TELAH DI HAPUSUSSSU"}
