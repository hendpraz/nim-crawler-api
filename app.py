from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def nothing():
    return 'Nothing'


@app.route('/byname')
def get_data_by_name():
    name = request.args.get('name', default = '*', type = str)
    page = request.args.get('page', default = 1, type = int)


@app.route('/byid')
def get_data_by_id():
    name = request.args.get('name', default = '*', type = str)
    page = request.args.get('page', default = 1, type = int)


if __name__ == '__main__':
    app.run()
