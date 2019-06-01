# coding: utf-8
from app import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)

class Criterion(db.Model):
    __tablename__ = 'criterions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    categories_id = db.Column(db.ForeignKey('categories.id', ondelete='CASCADE', onupdate='CASCADE'))
    categories = db.relationship('Category')


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.Text)
    subkod1 = db.Column(db.String)
    oktmo = db.Column(db.Text, unique=True)
    subject = db.Column(db.Text)
    subject_id = db.Column(db.ForeignKey('subject.id', ondelete='CASCADE', onupdate='CASCADE'))

    subject1 = db.relationship('Subject')


class Subject(db.Model):
    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    kod = db.Column(db.String, unique=True)


class Statistic(db.Model):
    __tablename__ = 'statistic'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    date = db.Column(db.Integer)
    criterions_id = db.Column(db.ForeignKey('criterions.id', ondelete='CASCADE', onupdate='CASCADE'))
    locations_id = db.Column(db.ForeignKey('locations.id', ondelete='CASCADE', onupdate='CASCADE'))
    locations = db.Column(db.String)

    criterions = db.relationship('Criterion')
    locations1 = db.relationship('Location')

