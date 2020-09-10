from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

DAYS = {'1': {"temperature":'97.1', "date": 'today'},
                '2': {"temperature":'97.1', "date": 'monday'},
                '3': {"temperature":'97.1', "date": 'tuesday'},
                '4': {"temperature":'97.1', "date": 'wednesday'},
                '5': {"temperature": '97.1', "date": 'thursday'}
                }

if __name__ == "__main__":
    app.run(debug=True)

parser = reqparse.RequestParser()

class DaysList(Resource):
    def get(self):
        return DAYS
    
    def post(self):
        parser.add_argument("temperature", location='form')
        parser.add_argument("date", location='form')
        args = parser.parse_args()
        day_id = int(max(DAYS.keys())) + 1
        day_id = '%i' % day_id
        DAYS[day_id] = {
            "temperature": args["temperature"],
            "date": args["date"],
        }

        return DAYS[day_id], 201

api.add_resource(DaysList, '/days/')

# @app.route('/days', methods=['POST'])