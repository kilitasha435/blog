import os

class Config:
    '''
    Parent configuration class
    '''
    debug = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevin:kilitasha@123@localhost/blogss'
    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevin:kilitasha@123@localhost/blogss'

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    SECRET_KEY = 'niMIMI'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevin:kilitasha@123@localhost/blogss'
    DEBUG = True
    ENV = 'development'
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}