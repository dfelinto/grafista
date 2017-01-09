from peewee import SqliteDatabase
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Configuration')

db = SqliteDatabase('test.sqlite')
