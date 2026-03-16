from fastapi import FastAPI

from metodos import consultarApi 
from database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Gestión Vial - VialDP")


app.include_router(consultarApi.router, prefix="/vial")

@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a VialDP",
        "documentacion": "/docs",
        "estado": "Conectado a MySQL"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
