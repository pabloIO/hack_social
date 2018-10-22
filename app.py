from flask import Flask, render_template, request, Response
from flask_cors import CORS, cross_origin
from config.config import env
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, template_folder="public")
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = env['APP_SECRET']
app.config['UPLOAD_FOLDER'] = env['UPLOADS_DIR']
## DATABASE CONFIG AND INSTANTIATION
app.config['SQLALCHEMY_DATABASE_URI'] = env['SQL_CONF']['DB_URI']
db = SQLAlchemy(app)

cors = CORS(app, resources={r"/login": {"origins": "http://localhost:3000"}})

from controllers import participantes_ctrl

##################################
####### VIEWS ROUTES #############
##################################
@app.route("/")
def main():
    return render_template('index.html')
###################################
###################################
###################################

###################################
####### PARTICIPANT ROUTES ########
###################################
@app.route(env['API_VERSION'] + "/test", methods=['GET'])
def upload_book():
    return 'hola'
@app.route(env['API_VERSION'] + "/concurso", methods=['POST', 'GET'])
def upload_book():
    return participantes_ctrl.ParticipantesCtrl.register(db, request, Response)

# @app.route(env['API_VERSION'] + "/libro/denounce", methods=['POST', 'GET'])
# def denounce_book():
#     return libros_ctrl.LibrosCtrl.denounceBook(db, request, Response)
#
# @app.route(env['API_VERSION'] + "/libro/download", methods=['GET'])
# def download_book():
#     return libros_ctrl.LibrosCtrl.turn_leds()

#############################
#############################
#############################

if __name__ == '__main__':
    print(str.format('CONECTADO EN PUERTO {0}', env['PORT']))
    app.run(host=env['HOST'], port=env['PORT'], debug=True, threaded=True)
