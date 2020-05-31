from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

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
        

