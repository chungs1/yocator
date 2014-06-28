import os
CSRF_ENABLED = False

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

API_TOKEN = "0b10db0b-0f40-c453-6cb3-0b906fdf3fb8"

