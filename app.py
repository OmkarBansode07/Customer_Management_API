from flask import Flask  # Importing Flask class from Flask module
from flask_restx import Api  # Importing Api class from flask_restx module
from api.config.config import Config  # Importing Config class from api.config.config module
from api.utils.db import db  # moduleImporting db instance from api.utils.db 
from api.models.customer import Customer  # Importing Customer model from api.models.customer module
from api.auth.views import customer_ns  # Importing customer_ns namespace from api.auth.views module

def create_app():
    # Creating a Flask application instance
    app = Flask(__name__)  # __name__ is the name of the current Python module 

    # Configuring the Flask application using the Config class
    app.config.from_object(Config)

    # Initializing the database instance with the Flask application
    db.init_app(app)

    # Creating database tables
    create_table(app)

    # Creating an instance of the Api class with the Flask application
    api = Api(app, title="Customer API", description="A REST API for a Customer Management System")

    # Adding the customer namespace to the API with the specified path
    api.add_namespace(customer_ns, path='/customers')

    return app  # Returning the Flask application instance

def create_table(app):
    # Creating database tables within the Flask application context
    with app.app_context():
        db.create_all()  # Creating all tables defined in the models

if __name__ == "__main__":
    # Call the create_app function to create and run the Flask application
    create_app(debug=True)  