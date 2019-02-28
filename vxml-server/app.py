from flask import Flask, render_template, make_response, send_from_directory
app = Flask(__name__)

temp = '13'


@app.route('/weather')
def hello():
    vxml = render_template('weather.xml', temp=temp)
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab1')
def lab1():
    vxml = render_template('lab1.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab1_booking')
def lab1_booking():
    vxml = render_template('lab1_booking.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab1_delayed')
def lab1_delayed():
    vxml = render_template('lab1_delayed.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab1_menu')
def lab1_menu():
    vxml = render_template('lab1_menu.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab2')
def lab2():
    vxml = render_template('lab2.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/grammars/<path:path>')
def send_grammar(path):
    return send_from_directory('grammars', path)
