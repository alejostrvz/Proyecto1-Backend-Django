# Proyecto1-Backend-Django
**Este es el primer proyecto para el bootcamp https://www.tzuzulcode.com**

#### Crear un entorno virtual
pip install virtualenv 
python -m virtualenv venv 

asi habra creado su entorno virtual

#### Activar entorno virtual
cd venv/Scripts/activate
#### o puede hacerlo de forma manual 
cd venv
cd Scripts
activate
**ahora tendra activado su entorno virtual**

#### ahora tendra que instalar las dependencias
pip install requirements.txt

#### ahora tendra que aplicar las migraciones 
esto se hace para que se cree los modelos en la bd 

cd src
python manage.py makemigrations
python manage.py migrate

**ahora estara listo para correr el proyecto**
python manage.py runserver

