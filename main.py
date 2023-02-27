# install peewee
from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "PreeChia.db"))


# creating table
class User(Model):
    name = CharField()
    email = CharField()
    password = CharField()


class Meta:
    database = db


User.create_table()


class Student(Model):
    name = CharField()
    Id = CharField()
    room = CharField()


class Meta:
    database = db


Student.create_table()


class People(Model):
    name = CharField()
    phone = CharField()
    email = CharField()
    password = CharField()
    gender = CharField()
    religion = CharField()
    county = CharField()


class Meta:
    database = db


People.create_table()
