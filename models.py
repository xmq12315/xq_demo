from exts import db
from datetime import datetime
class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(50),nullable=False)
    telephone=db.Column(db.String(11),nullable=False)
    password=db.Column(db.String(100),nullable=False)
class Question(db.Model):
    __tablename__='question'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(50),nullable=False)
    content=db.Column(db.Text,nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)
    author_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    author=db.relationship('User',backref=db.backref('questions'))