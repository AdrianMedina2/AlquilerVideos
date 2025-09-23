from pydantic import BaseModel, EmailStr, Field

class Usuario:
    nombre: str = Field(..., min_length = 8, max_length = 64, description = "Nombre del usuario")
    apellido: str = Field(..., min_length = 8, max_length = 64, description = "Apellido del usuario")
    email: EmailStr = Field(..., min_length = 8, max_length = 64, description = "Email del usuario")
    contrasenia = str = Field(..., min_length = 8, max_length = 20, description= "Contraseña del usuario")

    # Ejemplo que se debe mostrar en la documentación de la API
    model_config = {
        "json_Scheme_extra": {
            "example": {
                "nombre": "Lelo",
                "apellido": "Juaneco",
                "email": "Lelojuaneco@gmail.com",
                "contrasenia": "21032007adrian"
            }
        }
    }