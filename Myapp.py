from flask import Flask, jsonify
from flask_restful import  Resource, Api

app = Flask(__name__)
api = Api(app)


class Helloworld(Resource):
    def get(self):
        
        return ({"messge" : "Helloworld"})
    
api.add_resource(Helloworld, '/hello')
        


if __name__ == '__main__':
    app.run(debug=True)