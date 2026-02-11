from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
import model,schemas
from database import engine,SessionLocal

model.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db() :
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()


@app.get("/users",response_model=list[schemas.UserRespond])
def all_user(db:Session = Depends(get_db)) :
    users = db.query(model.User).all()
    return users

@app.post("/users/")
def create_user(user:schemas.CreateUser,db:Session = Depends(get_db)) :
    baru = model.User(nama =user.nama,umur = user.umur )
    db.add(baru)
    db.commit()
    db.refresh(baru)
    return baru

@app.put("/users/{user_id}")
def update_user(user_id:int,user:schemas.UpdateUser,db:Session = Depends(get_db)) :
    data_user = db.query(model.User).filter(model.User.id == user_id).first()
    if not data_user :
        raise HTTPException(status_code=404,detail="Data Tidak di Temukan")
    data_user.nama = user.nama
    data_user.umur = user.umur
    db.commit()
    db.refresh(data_user)
    return data_user

@app.delete("/users/{user_id}",response_model=schemas.UserRespond)
def delete_user(user_id:int,db:Session = Depends(get_db)) :
    data_user = db.query(model.User).filter(model.User.id == user_id).first()
    if not data_user :
        raise HTTPException(status_code=404,detail="Data Tidak di temukan")
    db.delete(data_user)
    db.commit()
    return data_user



@app.get("/hewans/",response_model=list[schemas.HewanRespon])
def all_hewans(db:Session = Depends(get_db)) :
    hewans = db.query(model.Hewan).all()
    if not hewans :
        raise HTTPException(status_code=404,detail="Data TidAK aADA")
    return hewans

@app.post("/hewan/",response_model=schemas.HewanRespon)
def create_hewan(hewan:schemas.CreateHewan,db:Session = Depends(get_db)) :
    hewan_baru = model.Hewan(nama = hewan.nama)
    db.add(hewan_baru)
    db.commit()
    db.refresh(hewan_baru)
    return hewan_baru


@app.put("/hewan/{hewan_id}",response_model=schemas.HewanRespon)
def update_hewan(hewan_id:int,hewan:schemas.UpdateHewan,db:Session = Depends(get_db)) :
    data_hewan = db.query(model.Hewan).filter(model.Hewan.id == hewan_id).first()
    if not data_hewan :
        raise HTTPException(status_code=404,detail="Hewan Tidak ada")
    data_hewan.nama = hewan.nama
    db.commit()
    db.refresh(data_hewan)
    return data_hewan


@app.delete("/hewans/{hewan_id}",response_model=schemas.HewanRespon)
def delete_hewan(hewan_id:int,db:Session = Depends(get_db)) :
    data_hewan  = db.query(model.Hewan).filter(model.Hewan.id == hewan_id).first()
    if not data_hewan :
        raise HTTPException(status_code=404,detail="Data Tidak ada")
    db.delete(data_hewan)
    db.commit()
    return data_hewan


@app.get("/hewan/{hewan_id}",response_model=schemas.HewanRespon)
def get_hewan(hewan_id:int,db:Session = Depends(get_db)) :
    data_hewan = db.query(model.Hewan).filter(model.Hewan.id == hewan_id).first()
    if not data_hewan :
        raise HTTPException(status_code=404,detail="Datat TiDAK ADA")
    return data_hewan