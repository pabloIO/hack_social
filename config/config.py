from flask import Flask
import os

env = {
    'PORT'      : 5000,
    'HOST'      : '0.0.0.0',
    'APP_ENV'   : 'DEV',
    'APP_SECRET': 'libr0s_abiert0s',
    'APP'       : Flask(__name__, template_folder="public"),
    'SQL_CONF'  : {
        'DB_NAME'  : 'premio_falso',
        'DB_URI'   : str.format('sqlite:///{0}', os.path.abspath('database/concurso.db')) if 'PYTHONANYWHERE_DOMAIN' not in  os.environ else 'sqlite://///home/GROVERLUIS2018/hack_social/hack_social/database/concurso.db'
    },
    'UPLOADS_DIR': os.path.abspath('static') if 'PYTHONANYWHERE_DOMAIN' not in  os.environ else os.path.abspath('static'),
    'ALLOWED_EXTENSIONS_IMG': set(['png', 'svg', 'gif', 'jpg', 'jpeg']),
    'API_VERSION': '/api/v1',
}
