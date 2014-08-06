import flask.ext.restless
from app import app, db
from models import *


# Create the Flask-Restless API manager.
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(User, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Observation, methods=['GET', 'POST'])
manager.create_api(Product, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Sensor, methods=['GET', 'POST', 'DELETE'])