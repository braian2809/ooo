from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from modelos import model_producto
from pydantic import BaseModel

router = APIRouter()


class CasoVialCreate(BaseModel):
    problema_comun: str
    solucion_legal: str
    id_n: int


@router.get("/casos_viales_all")
def listar_casos(db: Session = Depends(get_db)):
    return db.query(model_producto.CasoVial).all()

@router.get("/caso_vial/{id_cas}")
def obtener_caso(id_cas: int, db: Session = Depends(get_db)):
    caso = db.query(model_producto.CasoVial).filter(model_producto.CasoVial.id_cas == id_cas).first()
    if not caso:
        raise HTTPException(status_code=404, detail="Caso no encontrado")
    return caso

@router.get("/casos_viales_por_norma/{id_n}")
def casos_por_norma(id_n: int, db: Session = Depends(get_db)):
    return db.query(model_producto.CasoVial).filter(model_producto.CasoVial.id_n == id_n).all()

@router.post("/caso_vial/crear")
def crear_caso(caso: CasoVialCreate, db: Session = Depends(get_db)):  # ✅ Recibe JSON
    # Verificar norma
    norma = db.query(model_producto.Norma).filter(model_producto.Norma.id_n == caso.id_n).first()
    if not norma:
        raise HTTPException(status_code=404, detail="Norma no existe")
    
    nuevo = model_producto.CasoVial(
        problema_comun=caso.problema_comun,
        solucion_legal=caso.solucion_legal,
        id_n=caso.id_n
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/caso_vial/actualizar/{id_cas}")
def actualizar_caso(id_cas: int, caso: CasoVialCreate, db: Session = Depends(get_db)):  # ✅ Recibe JSON
    caso_db = db.query(model_producto.CasoVial).filter(model_producto.CasoVial.id_cas == id_cas).first()
    if not caso_db:
        raise HTTPException(status_code=404, detail="Caso no encontrado")
    
    norma = db.query(model_producto.Norma).filter(model_producto.Norma.id_n == caso.id_n).first()
    if not norma:
        raise HTTPException(status_code=404, detail="Norma no existe")
    
    caso_db.problema_comun = caso.problema_comun
    caso_db.solucion_legal = caso.solucion_legal
    caso_db.id_n = caso.id_n
    db.commit()
    db.refresh(caso_db)
    return caso_db

@router.delete("/caso_vial/borrar/{id_cas}")
def eliminar_caso(id_cas: int, db: Session = Depends(get_db)):
    caso = db.query(model_producto.CasoVial).filter(model_producto.CasoVial.id_cas == id_cas).first()
    if not caso:
        raise HTTPException(status_code=404, detail="ID no existe")
    db.delete(caso)
    db.commit()
    return {"mensaje": f"Caso {id_cas} eliminado"}