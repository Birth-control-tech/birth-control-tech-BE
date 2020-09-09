from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

DAYS = {'1': {"temperature":'97.1'},
                '2': {"temperature":'97.1'},
                '3': {"temperature":'97.1'},
                '4': {"temperature":'97.1'},
                '5': {"temperature":'97.1'},
                '6': {"temperature":'97.1'},
                '7': {"temperature":'97.1'},
                '8': {"temperature":'97.1'},
                '9': {"temperature":'97.1'},
                '10': {"temperature":'97.1'},
                '11': {"temperature":'97.1'},
                '12': {"temperature":'97.1'},
                '13': {"temperature":'97.1'},
                '14': {"temperature":'97.1'},
                '15': {"temperature":'97.1'},
                '16': {"temperature":'97.1'},
                '17': {"temperature":'97.1'},
                '18': {"temperature":'97.1'},
                '19': {"temperature":'97.1'},
                '20': {"temperature":'97.1'},
                }

if __name__ == "__main__":
    app.run(debug=True)

parser = reqparse.RequestParser()

class DaysList(Resource):
    def get(self):
        return DAYS

    def post(self):
        parser.add_argument("temperature")
        args = parser.parse_args()
        day_id = int(max(DAYS.keys())) + 1
        day_id = '%i' % day_id
        DAYS[day_id] = {
        "temperature": args["temperature"]
        }
        return DAYS[day_id], 201

api.add_resource(DaysList, '/days/')
