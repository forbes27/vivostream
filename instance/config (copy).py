import os

user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
host = os.environ.get("DB_HOST")
dbname = os.environ.get("DB_NAME")

SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = "postgres://adminuser:password123@gd18vzstqbz7azp.cnuipuiqebbi.us-east-1.rds.amazonaws.com:5432/dreamteam_db"
