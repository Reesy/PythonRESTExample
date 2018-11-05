from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# This should return a count from a textfile on disk. 
class Counter(Resource):
    def get(self):
        file = open('Count.txt', 'r');
        fileContents = file.read();
        return fileContents;

# This should increment a value inside a textfile on disk.
class Incrementer(Resource):
    def post(self):
        file = open('Count.txt', 'r');
        fileContents = file.read();
        request_data = request.get_json();
        incrementAmount = request_data['IncrementAmount'];
        file.close();
        result = int(fileContents) + incrementAmount;
        file = open('Count.txt', 'w');
        stringifiedResult = str(result);
        file.write(stringifiedResult);     
        file.close();
        return result;

api.add_resource(Counter, '/api/count') 
api.add_resource(Incrementer, '/api/increment');

if __name__ == '__main__':
     app.run(port='8080')