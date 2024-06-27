from flask import Flask

school_app = Flask(__name__)

from school_app import routes
