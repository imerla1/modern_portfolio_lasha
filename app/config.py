import os
import yaml

with open('cfg.yaml', 'r') as yaml_file:
    cfg = yaml.load(yaml_file)

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = cfg['secret']['SECRET_KEY']
    MAIL_SERVER = cfg['mail_config']['MAIL_SERVER']
    MAIL_PORT = cfg['mail_config']['MAIL_PORT']
    MAIL_USERNAME = cfg['mail_config']['MAIL_USERNAME']
    MAIL_PASSWORD = cfg['mail_config']['MAIL_PASSWORD']
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
