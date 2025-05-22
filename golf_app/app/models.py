from . import db # Assuming db will be initialized in app/__init__.py
from datetime import datetime

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    current_hole = db.Column(db.Integer, nullable=True, default=1)
    current_score = db.Column(db.Integer, nullable=True, default=0)
    score_logs = db.relationship('ScoreLog', backref='player', lazy='dynamic')

    def __repr__(self):
        return f'<Player {self.name}>'

class ScoreLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    hole_number = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<ScoreLog player_id={self.player_id} hole={self.hole_number} score={self.score}>'
