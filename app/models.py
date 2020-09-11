from app import db

class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    high_risk = db.Column(db.Boolean(), nullable=True)

    def __init__(self, temperature, date):
        self.temperature = temperature
        self.date = date

    def __repr__(self):
        return f"Day('{self.temperature}', '{self.date}', '{self.high_risk}')"
