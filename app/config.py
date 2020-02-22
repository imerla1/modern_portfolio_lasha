import os
import yaml

with open('cfg.yaml', 'r') as yaml_file:
    cfg = yaml.load(yaml_file)


class Config():
    SECRET_KEY = cfg['secret']['SECRET_KEY']
    MAIL_SERVER = cfg['mail_config']['MAIL_SERVER']
    MAIL_PORT = cfg['mail_config']['MAIL_PORT']
    MAIL_USERNAME = cfg['mail_config']['MAIL_USERNAME']
    MAIL_PASSWORD = cfg['mail_config']['MAIL_PASSWORD']
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
