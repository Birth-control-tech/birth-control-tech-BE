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

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.String(20), nullable=False)
    avg_period = db.Column(db.String(20), nullable=False)
    avg_cycle = db.Column(db.String(20), nullable=False)

    def __init__(self, start_date, avg_period, avg_cycle):
        self.start_date = start_date
        self.avg_period = avg_period
        self.avg_cycle = avg_cycle

    def __repr__(self):
        return f"UserData('{self.start_date}', '{self.avg_period}', '{self.avg_cycle}')"
