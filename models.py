from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db =SQLAlchemy()

class Subject(db.Model):
    __tablename__='subject'
    id =db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(50),unique=True, nullable=False)
    #relation to link experiment to subject
    experiments =db.relationship('Experiment',backref='subject', lazy=True)

class Experiment(db.Model):
        __tablename__='experiments'
        id = db.Column(db.Integer,primary_key=True)
        subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'),nullable=False)
        title =db.Column(db.String(100),nullable=False)
        description = db.Column(db.Text)
        youtube_url=db.Column(db.String(255))
        #link for the video hub
        

class UserProgress(db.Model):
        __tablename__='user_progress'
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
        experiment_id = db.Column(db.Integer, db.ForeignKey('experiments.id'), nullable=False)
        progress = db.Column(db.Float, default=0.0)  # percentage of completion
        last_accessed = db.Column(db.DateTime, default=datetime.utcnow)        

class User(db.Model):
            __tablename__='users'
            id = db.Column(db.Integer, primary_key=True)
            username = db.Column(db.String(50), unique=True, nullable=False)
            email = db.Column(db.String(120), unique=True, nullable=False)
            password_hash = db.Column(db.String(255), nullable=False)
            created_at = db.Column(db.DateTime, default=datetime.utcnow)
            #relation to link user to experiments they created


class Question(db.Model):
     __tablename__ = 'quizzes' # This tells Flask to use your existing table
    
     id = db.Column(db.Integer, primary_key=True)
     exp_id = db.Column(db.Integer, db.ForeignKey('experiments.id'), nullable=False)
     question = db.Column(db.Text, nullable=False)
     option_a = db.Column(db.String(255), nullable=False)
     option_b = db.Column(db.String(255), nullable=False)
     option_c = db.Column(db.String(255), nullable=False)
     option_d = db.Column(db.String(255), nullable=False)
     correct_answer = db.Column(db.String(1), nullable=False)           
            