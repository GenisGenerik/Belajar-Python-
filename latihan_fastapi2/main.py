from fastapi import FastAPI
from database import engine, Base



from routers import dosen_router, matkul_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(dosen_router.router)
app.include_router(matkul_router.router)
