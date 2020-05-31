from flask_sqlalchemy import SQLAlchemy
from models.AreaModel import Area

db = SQLAlchemy()

class Country(db.Model):
    
    __tablename__ = "country"

    id = db.Column('id', db.Integer, primary_key=True)
    country_name = db.Column('country_name', db.String(20), unique=True,  nullable=False,index=True)
    areas = db.relationship('Area', backref='belongs')

    def __init__(self, country_name):
        self.country_name = country_name

    def __repr__(self):
        return '< %r>' % self.country_name
    
    def get_id(self):
        return str(self.id)
    
class Area(db.Model):
    __tablename__ = "area"

    id = db.Column('id', db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    area_en = db.Column('area_en', db.String(10), index=True)
    area_zh_tw = db.Column('area_zh_tw', db.String(10), index=True)
    area_code = db.Column('area_code', db.Integer, unique=True)
    
    def __init__(self, area_en, area_zh_tw, area_code):
        self.area_en = area_en
        self.area_zh_tw = area_zh_tw
        self.area_code = area_code


