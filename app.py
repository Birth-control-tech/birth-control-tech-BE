from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_restful import Resource, Api, reqparse
from flask import request, jsonify
from models import Day

app = Flask(__name__)
# api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# days = [{"temperature":'97.1', "date": '01/01/2020'},
#             {"temperature":'97.1', "date": '01/02/2020'},
#             {"temperature":'97.7', "date": '01/03/2020'},
#             {"temperature":'97.6', "date": '01/04/2020'},
#             {"temperature": '97.1', "date": '01/05/2020'}]

# days = [
#     {
#         'temperature': '97.1',
#         'date':'01/01/2020'
#     },
#     {
#         'temperature': '97.0',
#         'date':'01/02/2020'
#     }
# ]

@app.route('/', methods=['GET'])
def home():
    return 'Lono Data'

@app.route('/api/v1/resources/days/', methods=['GET'])
def returnAll():
    return jsonify(days)

@app.route('/api/v1/resources/days/', methods=['POST'])
def addOne():
    # db.session.add or some sht
    # db.session.commit()
    new_day = request.get_json()
    days.append(new_day)
    return jsonify(days)

if __name__ == "__main__":
    app.run(debug=True)
# parser = reqparse.RequestParser()

# class DaysList(Resource):
#     def get(self):
#         return DAYS
    
#     def post(self):
#         parser.add_argument("temperature", location='form')
#         parser.add_argument("date", location='form')
#         args = parser.parse_args()
#         day_id = int(max(DAYS.keys())) + 1
#         day_id = '%i' % day_id
#         DAYS[day_id] = {
#             "temperature": args["temperature"],
#             "date": args["date"],
#         }

#         return DAYS[day_id], 201

# api.add_resource(DaysList, '/days/')
