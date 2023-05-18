from dotenv import load_dotenv
import os

load_dotenv()


class Configuration:
    SECRET_KEY = '3d6f!#45a5@*fc124+45'


class DevelopmentConfig(Configuration):
    DEBUG = True
    supabase_url = os.getenv('URL_API')
    supabase_key = os.getenv('SERVICE_ROLE')
    PASS_EMAIL = os.getenv('PASS_EMAIL')
    USER_EMAIL = os.getenv('USER_EMAIL')


config = {
    'development': DevelopmentConfig
}
