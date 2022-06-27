import os

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True # Set to True to enable debugging features in Flask
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
}