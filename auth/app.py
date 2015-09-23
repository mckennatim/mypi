from flask import Flask
from flask_jwt import JWT, jwt_required
from flask.ext.cors import CORS

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'mabibi eats birds'

jwt = JWT(app)
cors = CORS(app)

class User(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

@jwt.authentication_handler
def authenticate(username, password):
    if username == 'uli' and password == 'isadog':
        return User(id=1, username='joe')

@jwt.user_handler
def load_user(payload):
    if payload['user_id'] == 1:
        return User(id=1, username='uli')

@app.route('/protected')
@jwt_required()
def protected():
    return 'Success!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089)