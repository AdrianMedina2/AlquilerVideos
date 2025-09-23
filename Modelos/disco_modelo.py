from pydantic import BaseModel, EmailStr, Field

class Disco:
    codigo: str = Field(..., min_lenth = 8, max_length = 8, description = "Código de identificación única de la identidad")
    nombre: str = Field(..., min_length = 8, max_length = 64, description = "Título o nombre de la pelicula")
    sipnosis: str = Field(..., min_length = 16, max_length = 256, description = "Sipnosis de la película")
    director: str = Field(..., min_length = 4, max_length = 64, description = "Director de la pelicula")
    duracion: int = Field(..., ge = 1, le = 2, description = "Tiempo de duración de la película")
    tamanio: int = Field(..., ge = 1, le = 5, description = "Tamaño de la película en GB")
    precio_venta: int = Field(..., ge = 100, le = 500, description = "Precio de venta del disco digital")
    precio_renta: int = Field(..., ge = 50, le = 70, description = "Precio de renta del disco digital")

    #Ejemplo que se debe mostrar en la documentación de la API
    model_config = {
        "json_Scheme_extra":{
            "example": {
                "codigo": "Code-101",
                "nombre": "Lilo & Stich",
                "sipnosis": "Una niña solitaria llamada Lilo adopta a Stich",
                "director": "Josiel",
                "duracion": 3,
                "tamanio": 5,
                "precio_venta": 400,
                "precio_renta": 70,
            }
        }
    }