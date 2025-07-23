import os.path
import cherrypy
import json
import hashlib
import sqlite3 as sql
import time
baseDir = os.path.abspath(os.path.dirname(__file__))

print(baseDir)