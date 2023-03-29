import os

STAGES = ('development', 'production')
ENV = os.getenv('ENV', 'production').lower()
DEBUG = ENV != 'production'
TESTING = ENV == 'testing'

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')
#REDIS_URL = os.getenv('REDIS_URL') or f'redis://{REDIS_HOST}:{REDIS_PORT}'
CACHE_ACTIVE = True


logger = ()



