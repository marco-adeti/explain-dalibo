import os
WTF_CSRF_ENABLED = False
SECRET_KEY = os.environ.get('SECRET_KEY', '{{app_secret}}')
DB_NAME = os.environ.get('DB_NAME', '{{pg_dbname}}')
DB_USER = os.environ.get('DB_USER', '{{pg_dbuser}}')
DB_PASS = os.environ.get('DB_PASS', '{{pg_dbpass}}')
DB_SERVICE = os.environ.get('DB_SERVICE', '{{pg_dbhost}}')
DB_PORT = os.environ.get('DB_PORT', 5432)
SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
)
DEBUG_TB_INTERCEPT_REDIRECTS = False
DEBUG_TB_PROFILER_ENABLED = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
# GOOGLE_ANALYTICS = "UA-XXXXXX-XX"

