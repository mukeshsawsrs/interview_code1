# import necessary libraries and modules
from flask import Flask

# create object of class flask
app = Flask(__name__)
app.secret_key = b'3_s#K6"F7Q2z\g\yec]/'

# import routes
from app import routes

