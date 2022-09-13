from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request  # muốn lấy được thong tin do client gửi lên


app = Flask(__name__)

CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'


@app.route('/add', methods=['POST', 'GET'])
@cross_origin(origin='*')
def add_process():
    a = int(request.args.get('first_number'))
    b = int(request.args.get('second_number'))
    kq=a+b
    return 'kq la:' + str(kq)


@app.route('/minus', methods=['POST', 'GET'])
@cross_origin(origin='*')
def minus_process():
    a = request.args.get('first_number')
    b = request.args.get('second_number')
    kq = a - b
    return 'kq la:' + str(kq)


@app.route('/multi', methods=['POST', 'GET'])
@cross_origin(origin='*')
def multi_process():
    a = request.args.get('first_number')
    b = request.args.get('second_number')
    kq = a * b
    return 'kq la:' + str(kq)


@app.route('/div', methods=['POST', 'GET'])
@cross_origin(origin='*')
def div_process():
    a = request.args.get('first_number')
    b = request.args.get('second_number')
    kq = a / b
    return 'kq la:' + str(kq)


if __name__ == '__main--':
    app.run(host='0.0.0.0', port='9999')

