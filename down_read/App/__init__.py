"""
The flask application package.
"""
from flask import Flask

app = Flask(__name__)
import down_read.DB
import down_read.LocalCacheDB
import down_read.App.views
