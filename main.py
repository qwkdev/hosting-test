from flask import Flask
import json
from datetime import datetime

app = Flask('test')

with open('data.json') as f:
    x = json.load(f)

@app.route('/')
def index():
    return x

@app.route('/update')
def update():
    x = {'time': datetime.now().strftime("%H:%M:%S")}
    with open('data.json', 'w') as f:
        json.dump(x, f)
            
app.run()
