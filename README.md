# GAIA

Para ejecutar este proyecto debes:

Tener instalado Python, crear una maquina virtual, instalar las dependecias
que se encuentran dentro de requirements.txt.
Crear y activar un entorno virtual:

python3 -m venv myenv
source myenv/bin/activate  # En Windows: myenv\Scripts\activate

Instalar las dependencias:

pip install -r requirements.txt

Migrar la base de datos:

python manage.py makemigrations
python manage.py migrate

Ejecutar el servidor:

python manage.py runserver

Accede al proyecto desde el navegador:

http://127.0.0.1:8000  #Por defecto puede variar
