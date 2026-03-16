from pydantic import BaseModel
from typing import Optional, List


class CategoriaBase(BaseModel):
    nom_cat: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id_cat: int
    
    class Config:
        from_attributes = True


class VehiculoBase(BaseModel):
    tipo_v: str
    marca: str
    modelo: str
    placa: Optional[str] = "N/A"

class VehiculoCreate(VehiculoBase):
    pass

class Vehiculo(VehiculoBase):
    id_v: int
    
    class Config:
        from_attributes = True


class NormaBase(BaseModel):
    id_cat: int
    descripcion_norma: str
    aplica_a: str

class NormaCreate(NormaBase):
    pass

class Norma(NormaBase):
    id_n: int
    
    class Config:
        from_attributes = True


class ComponenteBase(BaseModel):
    nombre_componente: str
    estado_sugerido: str
    id_v: int

class ComponenteCreate(ComponenteBase):
    pass

class Componente(ComponenteBase):
    id_com: int
    
    class Config:
        from_attributes = True


class CasoVialBase(BaseModel):
    problema_comun: str
    solucion_legal: str
    id_n: int

class CasoVialCreate(CasoVialBase):
    pass

class CasoVial(CasoVialBase):
    id_cas: int
    
    class Config:
        from_attributes = True