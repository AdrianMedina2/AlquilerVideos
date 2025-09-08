# TestAlquilerVideo
Proyeto que implementa una API REST para una tienda virtual de vídeos, construida con un lenguaje python y el framework FastAPI. El objetivo es gestionar un catalogo de discos(películas o videos digitales) junto con las operaciones de registro de usuarios, ventas y alquileres.

##Estructura del proyecto
| -- Main.py #Punto de entrada de la aplicación de la API, FastAPI
|
  entidades/ #Directorio de paquetes que contiene todas las clases
    |- _init_.py 
    |- disco.py
    |- usuario.py
    |- venta.py
    |- alquiler.py
    |- catalogo.py
## Instalación y ejecución
  1. Clonar el repositorio
     git clone https://github.com/AdrianMedina2/TestAlquilerVideo.git
  2. CD test-alquiler.video
  3. Crear y activar el entorno virtual (opcional, recomendado)
  4. python -m venv venv
  5. source venv/bin/activate #Linux/Mac
  6. venv\Scripts\activate #Windows
  7. Instalar dependencias
     7.1 pip install fastapi uvicorn pydantic
  8. Ejecutar el servidor
     8.1 uvicorn main:app --reload
  9. Acceder a la API
      * Documentación interactiva: http//127.0.0.1:8000/docs
      * Documentación alternativa (ReDoc): http://127.0.0.1:8000/redoc

## Endpoints principales (versión inicial)
Metodo  Endpoint      Descripción
GET     /discos/      Lista los discos disponibles
POST    /discos/      Agregar un nuevo disco
PUT     /discos/{id}  Actualizar información de un disco
DELETE  /discos/{id}  Eliminar un disco
POST    /usuarios/    Registro de nuevo usuario
POST    /ventas/      Registrar ventas
POST    /arquileres/  Registrar un alquiler

## Tecnologías utilizadas
* Python 3.12.8
* FastApi
* Uvicorn (Servidor ASGI)

## Proyecto desarrollado como casa de estudio
* Nombre: *Adrian Medina Cubillo.* <amedinapya18@gmail.com>
* Github: @AdrianMedina2
