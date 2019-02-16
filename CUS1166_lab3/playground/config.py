import os
basedir = os.path.abspath(os.path.dirname('app.db'))

class Config(object):
    SQLALCHEMY_DATABASE_URI =\
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
