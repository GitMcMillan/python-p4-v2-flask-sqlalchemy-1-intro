from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# contains definitions of tables and associated schema constructs
metadata = MetaData()

# create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# define a model class by inheriting from db.Model.


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)


class User(db.Model):
    __tablename__ = 'users'
    #id = primary key
    id = db.Column(db.Integer, primary_key=True)
    #username is unique str of 80 length. Null values NOT allowed. Index is set on the column to speed up queries when searched by this column
    username = db.Column(db.String(80), unique=True,
                         nullable=False, index=True)
    # unique string of length 120. Null values allowed
    email = db.Column(db.String(120), unique=True)
    #boolean value. Defaults to False if a value not given
    verified = db.Column(db.Boolean, default=False)