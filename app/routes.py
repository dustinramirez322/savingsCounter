from app import app
from flask import render_template, redirect, url_for, request, make_response, session
from datetime import datetime
import sql.crud as crud

@app.route('/')
def home():
    resp = make_response(render_template('index.html'))
    return resp


@app.route('/postDeposit', methods=['POST'])
def postDeposit():
    date = datetime.now().strftime('%Y-%m-%d')
    year = datetime.now().strftime('%Y')
    amount = request.form["amount"]
    type = request.form["type"]
    input = {'date': date, 'year': year, 'amount': amount}
    try:
        total = crud.get_total(type) + float(amount)
        input[type] = total
        #crud.post_new(input, type)
        print(input)
    except Exception as e:
        print(e)
    return redirect(url_for('home'))



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404