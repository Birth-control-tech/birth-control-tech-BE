from flask import Flask
# from flask_restful import Resource, Api, reqparse
from flask import request, jsonify
app = Flask(__name__)
# api = Api(app)

days = [{"temperature":'97.1', "date": 'today'},
                {"temperature":'97.1', "date": 'monday'},
                {"temperature":'97.1', "date": 'tuesday'},
                {"temperature":'97.1', "date": 'wednesday'},
                {"temperature": '97.1', "date": 'thursday'}
                ]

@app.route('/', methods=['GET'])
def home():
    return 'Lono Data'

@app.route('/api/v1/resources/days/', methods=['GET'])
def returnAll():
    return jsonify(days)

@app.route('/api/v1/resources/days/', methods=['POST'])
def addOne():
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
