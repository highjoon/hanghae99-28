from dotenv import load_dotenv
from os import environ

load_dotenv()

WYC_SECRET_KEY = environ.get('SECRET_KEY')
MONGODB_USER = environ.get('MONGODB_USER')
MONGODB_PASSWORD = environ.get('MONGODB_PASSWORD')
MONGODB_HOST = environ.get('MONGODB_HOST')
BCRYPT_LEVEL = environ.get('BCRYPT_LEVEL')
