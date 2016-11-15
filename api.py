#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

json_data = open('me.json').read()

@app.route('/', methods=['GET'])
def get_info():
    return json_data

if __name__ == '__main__':
    app.run()
