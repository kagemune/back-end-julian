from flask import Flask
from routes.routes import *
from db import get_db
import os
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="DEVELOPMENT"
)
UPLOOAD_FOLDER ='/static/img/'
ALLOWED_EXTENSIONS={'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config[UPLOOAD_FOLDER]=UPLOOAD_FOLDER

#rutas de la aplicacion 
app.add_url_rule(routes['api_rut'], view_func=routes['api_cont'])
app.add_url_rule(routes["reg_rut"], view_func=routes["reg_cont"])
#ruta del 404
app.register_error_handler(routes['notFound_route'], routes['not_found_cont'])


@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

@app.before_request
def load_logged_in_user():
    username = session.get('username') #get es para devolver valores de un diccionario
    #print('entro a app.before_request')
    if username is None:
        g.user = None
        #print('g.user : ',g.user)
    else: #trae una tupla
        g.user = get_db().execute( 
            'SELECT * FROM Usuario WHERE nombre= ?',(username,)
        ).fetchone()
        g.rol = g.user[3]    


if  __name__ == "__main__":
    # os.environ['FLASK_DEBUG'] = 'development'
    app.run(debug=True)