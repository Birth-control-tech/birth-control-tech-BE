from flask import request, jsonify, session, render_template
from app import app
from app.models import Day
from app import db


days = [{'temperature':'97', 'date':'01/01/2020', 'high_risk':False},
        {'temperature': '97', 'date': '01/02/2020', 'high_risk': False},
        {'temperature': '98', 'date': '01/03/2020', 'high_risk': True},
        {'temperature': '98.5', 'date': '01/04/2020', 'high_risk': True},
        {'temperature': '98', 'date': '01/05/2020', 'high_risk': True}
]

@app.route('/', methods=['GET'])
def home():
    return 'Lono Data'


@app.route('/days/', methods=['GET'])
def returnAll():
    # return jsonify(days)
    # days = Day.query.all()
    return render_template('days.html', days=Day.query.all())

# @app.route('/days/new', methods=['POST'])
# def newDay():


@app.route('/add_day', methods=['POST'])
def createDay():
    temp = request.form['temperature']
    date = request.form['date']
    # date = request.form.get('date')
    # schema = DaySchema()
    # day_info = {
    #     'temperature': request.form.get('temperature'),
    #     'date': request.form.get('date')
    # }
    # db.session.add or some sht
    # db.session.commit()
    new_day = Day(temp, date)
    db.session.add(new_day)
    db.session.commit()
    return "<p>Data is updated</p>"
    # days.append(new_day)
    # return jsonify(days)

