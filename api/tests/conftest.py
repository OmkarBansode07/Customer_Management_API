import pytest
from flask import Flask
from app import create_app
from api.utils.db import db

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
  

    with app.app_context():
        db.create_all()
        yield app
    
    # with app.app_context():
    #     db.drop_all()
    #     yield app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client