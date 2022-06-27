from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Residente_recibe(db.Model):
    __tablename__ = "residente_recibe"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    cedula_identidad = db.Column(db.Integer)
    edad = db.Column(db.Integer)
    telefono= db.Column(db.Integer)
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    fecha_registro = db.Column(db.DateTime)

    @classmethod
    def create(cls, nombre, apellido, cedula_identidad, edad, telefono, latitud, longitud, fecha_registro):
        afectado = Residente_recibe(nombre=nombre, apellido=apellido, cedula_identidad=cedula_identidad, edad=edad, telefono=telefono, latitud=latitud, longitud=longitud, fecha_registro=fecha_registro)
        return afectado.save()
    
    def save(self):
        try:
            db.session.add(self) #Añadi  
            db.session.commit() #Guarda
            return self
        except Exception as e:
            print(e)
            return None
    
    def delete(self):
        try:    
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'cedula_identidad': self.cedula_identidad,
            'edad': self.edad,
            'telefono': self.telefono,
            'latitud': self.latitud,
            'longitud': self.longitud,
            'fecha_registro': self.fecha_registro
        }
class Residente_envia(db.Model):
    __tablename__ = "residente_envia"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    cedula_identidad = db.Column(db.Integer, unique=True, nullable=False)
    edad = db.Column(db.Integer)
    telefono= db.Column(db.Integer)
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    fecha_registro = db.Column(db.DateTime)

    @classmethod
    def create(cls, nombre, apellido, cedula_identidad, edad, telefono, latitud, longitud, fecha_registro):
        afectado = Residente_envia(nombre=nombre, apellido=apellido, cedula_identidad=cedula_identidad, edad=edad, telefono=telefono, latitud=latitud, longitud=longitud, fecha_registro=fecha_registro)
        return afectado.save()
    
    def save(self):
        try:
            db.session.add(self) #Añadi  
            db.session.commit() #Guarda
            return self
        except Exception as e:
            print(e)
            return None
    
    def delete(self):
        try:    
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'cedula_identidad': self.cedula_identidad,
            'edad': self.edad,
            'telefono': self.telefono,
            'latitud': self.latitud,
            'longitud': self.longitud,
            'fecha_registro': self.fecha_registro
        }
class Involucrado(db.Model):
    _tablename_ = "Involucrado"
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    cedula = db.Column(db.String(50),unique = True, nullable =False)
    telefono = db.Column(db.String(50),unique = True, nullable =False)
    servicio_a_ofrecer = db.Column(db.String(50))
    fecha_registro = db.Column(db.DateTime)

    @classmethod
    def create(cls, nombre, apellido, cedula, telefono, servicio_a_ofrecer, fecha_registro):
        afectado = Residente_envia(nombre=nombre, apellido=apellido,cedula=cedula, telefono = telefono, servicio_a_ofrecer = servicio_a_ofrecer, fecha_registro=fecha_registro)
        return afectado.save()
    
    def save(self):
        try:
            db.session.add(self) #Añadi  
            db.session.commit() #Guarda
            return self
        except Exception as e:
            print(e)
            return None
    
    def delete(self):
        try:    
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'cedula' : self.cedula,
            'telefono' : self.telefono,
            'servicio_a_ofrecer' : self.servicio_a_ofrecer,
            'fecha_registro': self.fecha_registro
        }