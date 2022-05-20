# Proyecto1-Backend-Django<br>
**Este es el primer proyecto para el bootcamp https://www.tzuzulcode.com**<br>

#### Crear un entorno virtual
pip install virtualenv <br>
python -m virtualenv venv <br>

asi habra creado su entorno virtual<br>

#### Activar entorno virtual<br>
cd venv/Scripts/activate
#### o puede hacerlo de forma manual 
cd venv<br>
cd Scripts<br>
activate<br>
**ahora tendra activado su entorno virtual**<br>

#### ahora tendra que instalar las dependencias<br>
pip install requirements.txt<br>

#### ahora tendra que aplicar las migraciones <br>
esto se hace para que se cree los modelos en la bd <br>

cd src<br>
python manage.py makemigrations<br>
python manage.py migrate<br>

**ahora estara listo para correr el proyecto**<br>
python manage.py runserver<br>

