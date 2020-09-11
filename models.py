from __main__ import db

class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    high_risk = db.Column(db.Boolean(), nullable=True)

    def __repr__(self):
        return f"Day('{self.temperature}', '{self.date}')"
