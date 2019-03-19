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
    vxml = render_template('lab1/lab1.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab1_booking')
def lab1_booking():
    vxml = render_template('lab1/lab1_booking.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab1_delayed')
def lab1_delayed():
    vxml = render_template('lab1/lab1_delayed.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab1_menu')
def lab1_menu():
    vxml = render_template('lab1/lab1_menu.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab2')
def lab2():
    vxml = render_template('lab2/lab2.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab3')
def lab3():
    vxml = render_template('lab3/lab3.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab4')
def lab4():
    vxml = render_template('lab4/lab4.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab4_booking')
def lab4_booking():
    vxml = render_template('lab4/lab4_booking.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/lab4_delayed')
def lab4_delayed():
    vxml = render_template('lab4/lab4_delayed.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/menu')
def project_menu():
    vxml = render_template('project/menu.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/exit')
def project_exit():
    vxml = render_template('project/exit.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/game')
def project_game():
    vxml = render_template('project/game.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response


@app.route('/grammars/<path:path>')
def send_grammar(path):
    return send_from_directory('grammars', path)
