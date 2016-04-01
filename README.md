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
    ---- apps/                  # Aplicaciones propias en django
    -------- comments/          # Aplicacion de commentarios (crea api para paquete de tercero 'django_comments_xtd')
    -------- favorite/          # Aplicacion de favoritos (asocia a un usuario y un objeto generico)
    -------- notification/      # Aplicacion para generar notificaciones
    -------- program/           # Aplicacion para administrar videos por programas, episodios y categorias
    -------- user/              # Aplicacion para reescribir alguna logicas para el sistema de authenticacion
    -------- userProfile/       # Aplicacion que genera perfiles de usuario
    ---- tvlibre/               # Projecto
    -------- media/             # Archivos media
    -------- static/            # Archivos Estaticos
    ------------ bower_components/  # Contiene paquetes instalado con bower (paquetes/librerias javascript de terceros)
    ------------ css/               # Contiene hojas de estilo propia
    ------------ js/                # Contiene Script de javascript propios
    ------------ templates-utils    # Contiene template utiles
    ------------ tvapp/             # Contiene aplicacion de angular
    ---------------- canal/         # Modulo para manejar "canales"
    ---------------- comment/       # Modulo de comentarios
    ---------------- favorite/      # Modulo de favoritos
    ---------------- layout/        # Modulo donde se definen diferentes partes del layout (como el sidebar)
    ---------------- notification/  # Modulo de notificacion
    ---------------- program/       # Modulo para manejar programas y episodios
    ---------------- user/          # Modulo de usuario
    ---------------- util/          # Modulo donde contiene directivas, controladores y template utils que se usan en diferentes lugares de la aplicacion
    ---------------- app.config.js  # Configuracion de la aplicacion
    ---------------- app.js         # Define la aplicacion
    ---------------- app.routes.js  # Define las rutas de la aplicacion
    -------- templates/             # Contiene los template que procesa django
    ------------ account/           # Reescribiendo template del paquete "allauth"
    ------------ notification/      # Template de la aplicacion de notificacion
    ------------ user/              # Template de la aplicacion de usuarios
    ------------ base.html          # Template base
    ------------ dashboard.html     # Template que levanta la aplicacion de angular
    ------------ index.html



