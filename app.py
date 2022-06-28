from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import config
from models import db, Residente_envia, Residente_recibe, Involucrado
import requests
from datetime import datetime
import folium
from folium.plugins import MarkerCluster



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

@app.route("/api/v1", methods =['POST'])
def apiv1():

    datos_receptor=request.form
    print(datos_receptor)
    fecha_actual=datetime.now()
    residente_recibe=Residente_recibe.create(
    nombre=datos_receptor["nombre"], 
    apellido=datos_receptor["apellido"], 
    cedula_identidad=datos_receptor["cedula_identidad"],
    edad=datos_receptor["edad"],
    telefono=datos_receptor["telefono"], 
    latitud=datos_receptor["latitud"], 
    longitud=datos_receptor["longitud"], 
    fecha_registro=fecha_actual)

    return render_template("form_receptor.html")


# Ahora creamos la ruta para recepcion de los datos desde el form_informer
@app.route('/api/v2',methods=['POST'])
def apiv2():
    datos_informer=request.form
    print(datos_informer)
    fecha_actual=datetime.now()
    residente_envia=Residente_envia.create(
    nombre=datos_informer["nombre"], 
    apellido=datos_informer["apellido"], 
    cedula_identidad=datos_informer["cedula_identidad"],
    edad=datos_informer["edad"],
    telefono=datos_informer["telefono"], 
    latitud=datos_informer["latitud"], 
    longitud=datos_informer["longitud"], 
    fecha_registro=fecha_actual
    )
    return render_template("form_informer.html")


# Ahora creamos la ruta para recepcion de los datos desde el form_involved
@app.route('/api/v3',methods=['POST'])
def apiv3():
    datos_involved=request.form
    print(datos_involved)
    fecha_actual=datetime.now()
    involucrado=Involucrado.create(
    nombre=datos_involved["nombre"], 
    apellido=datos_involved["apellido"], 
    cedula_identidad=datos_involved["cedula_identidad"],
    telefono=datos_involved["telefono"], 
    servicio_a_ofrecer=datos_involved["servicio_a_ofrecer"],
    fecha_registro=fecha_actual
    )
    return render_template("form_involved.html")



@app.route('/mapa')
def mapa():
    mapa=folium.Map(location=[-25.3011646,-57.6320055],width="50%",height="50%",zoom_start=13)
    cluster=MarkerCluster().add_to(mapa)
    
    ##Resindentes que quieren recibir alertas
    lista_coordenadas_recibe=Residente_recibe.query.all()
    print(lista_coordenadas_recibe)
    extracion_coordenadas_recibe=[]
    for elemento in lista_coordenadas_recibe:
        coordenadas_especificas_residente_recibe_lat_lon=[elemento.latitud , elemento.longitud]  
        extracion_coordenadas_recibe.append(coordenadas_especificas_residente_recibe_lat_lon) 
    print(extracion_coordenadas_recibe) 
    for point in extracion_coordenadas_recibe:
        marcador_recibe = point[0] , point[1]
        folium.Marker(location=marcador_recibe , icon=folium.Icon(color="green")).add_to(cluster)

    ##Resindentes que quieren envien alertas
    lista_coordenadas_envia=Residente_envia.query.all()
    print(lista_coordenadas_envia)
    extracion_coordenadas_envia=[]
    for elemento in lista_coordenadas_envia:
        coordenadas_especificas_residente_envia_lat_lon=[elemento.latitud , elemento.longitud]  
        extracion_coordenadas_envia.append(coordenadas_especificas_residente_envia_lat_lon) 
    print(extracion_coordenadas_envia) 
    for point in extracion_coordenadas_envia:
        marcador_envia = point[0] , point[1]
        folium.Marker(location=marcador_envia,  icon=folium.Icon(color="blue")).add_to(cluster)




    return mapa._repr_html_()



# hola esto es un comentario

if __name__ == '__main__':
    #Iniciamos la aplicacion en modo debug
    app.run(debug=True)
