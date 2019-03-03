"""
The flask application package.
"""
from flask import Flask

app = Flask(__name__)
import up_write.DB
import up_write.App.views
