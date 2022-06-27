from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import config
from models import db, Residente_envia, Residente_recibe, Involucrado
import requests


app = Flask(__name__)
                                        #### PORQUE PASA ESTOOOOOO
def createapp(environment):
    app = Flask(__name__)    
    app.config.from_object(environment)
    with app.app_context(): 
        db.init_app(app)
        db.create_all()
    return app

environment=config["development"]

app=createapp(environment)


@app.route("/")
def index():
    return render_template("index.html")


# Creamos nuestra ruta de formulario de receptores de la informacion. "/login"
@app.route('/form_receptor')
def form_receptor():
    #Renderizamos la plantilla. Formulario HTML
    # templates/form.html
    return render_template("form_receptor.html")

# Creamos nuestra ruta de formulario de informates de alertas. 
@app.route('/form_informer')
def form_informer():
    #Renderizamos la plantilla. Formulario HTML
    # templates/form.html
    return render_template("form_informer.html")

# Creamos nuestra ruta de formulario de involucrados o voluntarios. 
@app.route('/form_involved')
def form_involved():
    #Renderizamos la plantilla. Formulario HTML
    # templates/form.html
    return render_template("form_involved.html")

# Definimos el route con el metodo POST
@app.route('/formulario/usuario',methods=['POST'])
def usuario():
    #Obtenemos la informacion del parametro "nombreUser"
    nombreUser=request.form['nombreUser']

    #Retornamos la respuesta
    return "<h1>Bienvenido " + nombreUser + " ya estas inscripto</h1>"

@app.route("/api/v1", methods =['POST'])  # info de afuera
def apiv1():
    datos_receptor = request.form
    print(datos_receptor)

    return render_template("form_receptor.html")



    

if __name__ == '__main__':
    #Iniciamos la aplicacion en modo debug
    app.run(debug=True)


