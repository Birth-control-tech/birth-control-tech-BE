from flask import request, jsonify, session, render_template
# from app import app
from app.models import Day
from app.models import UserData
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
    return render_template('days.html', days=Day.query.all())


@app.route('/add_day', methods=['POST'])
def createDay():
    temp = request.form['temperature']
    date = request.form['date']
    new_day = Day(temp, date)
    db.session.add(new_day)
    db.session.commit()
    return "<p>Day has been added</p>"


@app.route('/user_data', methods=['GET'])
def returnData():
    return render_template('data.html', data=UserData.query.all())


@app.route('/add_data', methods=['POST'])
def createData():
    start_date = request.form['start_date']
    avg_period = request.form['avg_period']
    avg_cycle = request.form['avg_cycle']
    new_data = UserData(start_date, avg_period, avg_cycle)
    db.session.add(new_data)
    db.session.commit()
    return "<p>Data has been added</p>"
