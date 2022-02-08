import os 

class Config: 
    '''
      General configuration parent class
      '''
 
    SECRET_KEY ='SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://barbra:reson1234@localhost/oneminute'

        #   email configurations
    MAIL_SERVER = 'bmootian@gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("barbra")
    MAIL_PASSWORD = os.environ.get("babimootian")

class ProdConfig(Config):
    """Production configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    """
    pass


class DevConfig(Config):
    """Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """

    DEBUG=True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
