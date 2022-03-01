from flask import Flask

app = Flask(__name__)

from app.main import views, errors
from app.requests import configure_request
configure_request()
