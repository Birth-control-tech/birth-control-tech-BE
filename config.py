class Development(object):
    DEBUG = True
    TESTING = False

class Production(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Testing(object):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
