import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    TESTING = False

    
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True

    MAX_CONTENT_LENGTH= 2.5 * 1024 * 1024 # 2.5MB
    

    @staticmethod
    def init_app(app):
        pass
        
class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    
class TestingConfig(Config):
    TESTING = True
    

class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE  = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    



    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    'testing': TestingConfig
}