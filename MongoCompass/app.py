from flask import Flask
import Controller

app = Flask(__name__)

@app.route('/mongo', methods=['POST'])
def create_user():
    return Controller.create_user()

@app.route('/mongo/<id>', methods=['PUT'])
def update_user(id):
    return Controller.update_user(id)

@app.route('/mongo/<id>', methods=['GET'])
def get_user(id):
    return Controller.get_user(id)
@app.route('/')
def hello():
    return "Running"


if __name__ == '__main__':
    app.run(debug=True)
