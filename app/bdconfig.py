from flask_mysqldb import MySQL
from app import app

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'prueba'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)