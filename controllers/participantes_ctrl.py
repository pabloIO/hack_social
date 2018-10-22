import string, random, json, sys, os.path, uuid
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
# from models import sesion
import models.models as database
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.functions import func
from sqlalchemy import desc
import uuid
from config.config import env
from werkzeug.utils import secure_filename
from flask import flash, redirect, url_for, jsonify

## Chequear que solo existe una extension
def allowed_file(file, type):
    if type == 'img' and file == None:
        return False
    return '.' in file.filename and \
           file.filename.rsplit('.', 1)[1].lower() in env['ALLOWED_EXTENSIONS_IMG']

def id_generator(size=150, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class ParticipantesCtrl(object):
    @staticmethod
    def register(db, request, response):
        try:
            res = {
                'success': False,
            }
            # print(request.form)
            # print(request.files)
            if request.method == 'POST':
                # print(request.files['fileimg'] == None)
                if 'img' not in request.files:
                    res['success'] = False
                    res['msg'] = 'Debe seleccionar un archivo del escrito'
                    res['code'] = 400
                imgfile = request.files['img'] if 'img' in request.files else None
                if imgfile or allowed_file(imgfile, 'img'):
                    imgfilename = uuid.uuid4().hex + secure_filename(imgfile.filename)
                    print(imgfilename)
                    newRegister = database.Participantes(
                        nombre=request.form['nombre'],
                        apellidos=request.form['apellidos'],
                        codigo_estudiante=request.form['codigo'],
                        genero=request.form['genero'],
                        imagen=imgfilename
                    )
                    db.session.add(newRegister)
                    db.session.commit()
                    print(env['UPLOADS_DIR'])
                    imgfile.save(os.path.join(env['UPLOADS_DIR'] + '/images', imgfilename))
                    res['success'] = True
                    res['route'] = 'http://se.unifranz.edu.bo/'
                    return redirect(res['route'], code=302)
                else:
                    print('err')
                    res['success'] = False
                    res['msg'] = 'Formato no aceptado'
                    res['code'] = 400
        except Exception as e:
            print(e)
            db.session.rollback()
            res['msg'] = 'Hubo un error, inténtelo nuevamente'
        finally:
            return response(json.dumps(res), mimetype='application/json')
