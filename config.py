#!/usr/bin/python

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///test.db'

class Production(Config):
    pass
    
class Development(Config):
    DEBUG = True
