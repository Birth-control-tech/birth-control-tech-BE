from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
# from app import db
# from models import Day


def days(count=23):
    fake = Faker()
    i = 0
    while i < count:
        u = Day(temperature=fake.between(97.1, 97.5),
                 date=fake.date_between(start_date = '2020, 10, 1', end_date = '2020, 10, 23'),
                 high_risk='false')
        db.session.add(u)
        i += 1
        # try:
            # db.session.commit()
        # except IntegrityError:
            # db.session.rollback()

def days(count=7):
    fake = Faker()
    i = 0
    while i < count:
        u = Day(temperature=fake.between(97.6, 98.6),
                 date=fake.date_between(start_date = '2020, 10, 24', end_date = '2020, 11, 1'),
                 high_risk='true')
        db.session.add(u)
        i += 1
        # try:
            # db.session.commit()
        # except IntegrityError:
            # db.session.rollback()


# def posts(count=100):
#     fake = Faker()
#     user_count = User.query.count()
#     for i in range(count):
#         u = User.query.offset(randint(0, user_count - 1)).first()
#         p = Post(body=fake.text(),
#                  timestamp=fake.past_date(),
#                  author=u)
#         db.session.add(p)
#     db.session.commit()
