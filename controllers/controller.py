import os
from sqlite3.dbapi2 import connect
import json
from flask.views import MethodView
from flask import render_template,request,redirect,flash,jsonify,session,g
from db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename, send_from_directory


UPLOAD_FOLDER = '/static/img/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}



class apiController(MethodView):
    def get(self):
            db = get_db()
            products = db.execute("SELECT * FROM comentarios").fetchall()
            data = []
            
            for row in products:
                data.append([x for x in row])
                

            return (data)

class registerController(MethodView):
    
    def get(self):
        if "username" in session:
            return redirect("/api")
        else:
            return render_template("register.html")
    def post(self):
        
        try:
            # nombre = request.form["nombre"]
            # contraseña =request.form["contraseña"]
            nombre = 'yeico'
            contrasena = 'Akashinomoka0'
            db= get_db()
            db.execute('INSERT INTO Usuario (nombre,password,rol) VALUES(?,?,?)',(nombre,generate_password_hash(contrasena),3))
            db.commit()
            flash("la informacion se ingresado con exito","success")
            return redirect("/")
        except:
            flash("un error ha ocurrido ","error")
            return render_template("register.html")
    