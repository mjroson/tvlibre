## Despliegue de la aplicacion sobre sistemas operativos basados en debian.

    # Paquetes requeridos en el sistema:
        $ sudo apt-get install python3-pip libpng12-dev zlib1g-dev libfreetype6-dev libjpeg-dev python3-all-dev

    # Install virtualenv (paquete de python para generar entornos para trabajar con paquetes de python)
        $ sudo pip3 install virtualenv

    # Crear entorno virtual
        $ virtualenv env

    # Activar entorno virtual
        $ source env/bin/activate

    # Descargar projecto y instalar los requerimientos
        $ git clone git@github.com/[USUARIO]:tvlibre
        $ pip install -r ./tvlibre/requirements.txt

    # Correr migraciones y crear super usuario
        $ cd ./tvlibre
        $ ./manage.py makemigrations
        $ ./manage.py migrate
        $ ./manage.py createsuperuser

    # Correr proyecto
        $ ./manage.py runserver


## Distribucion de carpetas

    tvlibre/
    ---- apps/
    -------- comments/
    -------- favorite/
    -------- notification/
    -------- program/
    -------- user/
    -------- userProfile/
    ---- tvlibre/
    -------- media/
    -------- static/
    ------------ bower_components/
    ------------ css/
    ------------ js/
    ------------ templates-utils
    ------------ tvapp/
    ---------------- canal/
    ---------------- comment/
    ---------------- favorite/
    ---------------- layout/
    ---------------- notification/
    ---------------- program/
    ---------------- user/
    ---------------- util/
    ---------------- app.config.js
    ---------------- app.js
    ---------------- app.routes.js
    -------- templates/
    ------------ account/
    ------------ notification/
    ------------ user/
    ------------ base.html
    ------------ dashboard.html
    ------------ index.html



