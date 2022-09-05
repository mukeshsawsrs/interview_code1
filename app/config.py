# import necessary libraries and modules
from app import app
from flaskext.mysql import MySQL

# create mysql object which will be used later on to connect to the database
mysql = MySQL()

# set configuration for database connectivity
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'flask_demo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306

# initialize mysql object with database config
mysql.init_app(app)
# This mysql object can be used directly to connect to the database