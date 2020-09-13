from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from app import db
from app.models import Day
import random
import datetime

# release: python manage.py db upgrade

migrate = Migrate(app, db)
manager = Manager(app)



def low_risk_days(count=23):
    # fake = Faker()
    i = 0
    while i < count:
        u = Day(temperature=random.uniform(97.1, 97.5),
                 date=datetime.date(2020,10,1+i),
                 high_risk=False)
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()

def high_risk_days(count=7):
    # fake = Faker()
    i = 0
    while i < count:
        u = Day(temperature=random.uniform(97.6, 98.6),
                 date=datetime.date(2020,10,24+i),
                 high_risk=True)
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()

@manager.command
def seed():
    Day.query.all().clear()
    low_risk_days()
    high_risk_days()


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
    db.create_all()
    db.init_app(app)
