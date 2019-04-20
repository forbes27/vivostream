import os

user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
host = os.environ.get("DB_HOST")
dbname = os.environ.get("DB_NAME")

SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = "postgres://%s:%s@%s:5432/%s" % (user,password,host,dbname)
