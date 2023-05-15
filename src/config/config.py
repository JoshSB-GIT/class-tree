from dotenv import load_dotenv
import os

load_dotenv()


class Configuration:
    SECRET_KEY = '3d6f!#45a5@*fc124+45'


class DevelopmentConfig(Configuration):
    DEBUG = True
    # MYSQL_HOST = os.getenv('MYSQL_HOST')
    # MYSQL_USER = os.getenv('MYSQL_USER')
    # MYSQL_PASS = ''  # os.getenv('MYSQL_PASS')
    # MYSQL_DB = os.getenv('MYSQL_DB')


config = {
    'development': DevelopmentConfig
}
