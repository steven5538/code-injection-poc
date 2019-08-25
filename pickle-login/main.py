from flask import Flask, request, make_response
import pickle
import base64

app = Flask(__name__)

SECRET_KEY = '1ts4V3ryS3r3tk3y!'

class User:
    def __init__(self):
        self.role = 'guest'

    def set_admin(self):
        self.role = 'admin'

@app.route('/')
def hello():
    user = User()
    if 'token' in request.cookies:
        user = pickle.loads(base64.b64decode(request.cookies['token']))

    if user.role == 'admin':
        return f'WOW, {SECRET_KEY}!'
    else:
        resp = make_response(f'Hello, {user.role}!')
        resp.headers['Set-Cookie'] = 'token=' + base64.b64encode(pickle.dumps(user)).decode('utf-8')
        return resp