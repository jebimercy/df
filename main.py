# install peewee
from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "PreeChia.db"))


# creating table
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()


class Meta:
    database = db


User.create_table


class Student(Model):
    name = CharField()
    Id = CharField(unique=True)
    student_class = CharField()


class Meta:
    database = db


Student.create_table
