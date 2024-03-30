from flask import Flask
import json
from datetime import datetime

app = Flask(__name__)

with open('site/data.json') as f:
    x = json.load(f)

@app.route('/')
def index():
    with open('site/data.json') as f:
        x = json.load(f)
    return x

@app.route('/update')
def update():
    x = {'time': datetime.now().strftime("%H:%M:%S")}
    with open('site/data.json', 'w') as f:
        json.dump(x, f)
