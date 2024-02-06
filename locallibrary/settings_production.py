from decouple import Config

# Configura la clase Config con el archivo .env
config = Config()

# Define las variables de entorno necesarias
POSTGRES_DATABASE = config('POSTGRES_DATABASE')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_HOST = config('POSTGRES_HOST')

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DATABASE,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': '5432',  
    }
}
