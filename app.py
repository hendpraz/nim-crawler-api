from flask import Flask, request
from rest_api.data_getter import get_data
from rest_api.util import response_api

app = Flask(__name__)


@app.route('/')
def nothing():
    return 'Hello. Belum ada dokumentasi untuk API ini.'


@app.route('/byname')
def get_data_by_name():
    if request.method == 'GET':
        name = request.args.get('nama', default='*', type=str)
        page = request.args.get('page', default=0, type=int)
        data = get_data(name, 'name', page)
        return response_api(data)


@app.route('/byid')
def get_data_by_id():
    if request.method == 'GET':
        name = request.args.get('query', default='*', type=str)
        page = request.args.get('page', default=0, type=int)
        data = get_data(name, 'nim', page)
        return response_api(data)


if __name__ == '__main__':
    app.run()
