from flask import Blueprint, render_template, redirect, url_for, request, make_response
from datetime import datetime
import sql.crud as crud
import dotenv
import os

savings = Blueprint('savings', __name__)

dotenv.load_dotenv()
# Basic homepage that displays index.html
@savings.route('/')
def home():
    resp = make_response(render_template('index.html', grafana_page=os.environ.get("GRAFANA_PAGE")))
    return resp

@savings.route('/total')
def total():
    resp = make_response(render_template('total.html', grafana_total_page=os.environ.get("GRAFANA_TOTAL_PAGE")))
    return resp


# Page that is POSTed to upon pressing the submit button on the home page
@savings.route('/postDeposit', methods=['POST'])
def postDeposit():
    # Get date information and pull information from the web form
    date = datetime.now().strftime('%Y-%m-%d')
    year = datetime.now().strftime('%Y')
    amount = request.form["amount"]
    try:
        float(amount)
    except ValueError:
        return render_template('404.html'), 404
    deposit_type = request.form["type"]
    # Consolidate this into out input type
    deposit_input = {'date': date, 'year': year, 'amount': amount}
    try:
        # Get the final portion of our input type by calling the get_total function and adding our current deposit
        total = crud.get_type_total(deposit_type) + float(amount)
        # Update final month for graph purposes
        crud.update_type_total(deposit_type, total)
        deposit_input[deposit_type] = total
        # Post this new input along with the type of deposit using the post_new function
        crud.post_new(deposit_input, deposit_type)
        current_total = crud.get_current_total()
        total_update = {'date': date, 'year': year, 'amount': amount, 'type': deposit_type}
        total_update['total'] = str(float(amount) + float(current_total))
        crud.update_total(total_update)
    except Exception as e:
        # If it fails log the error
        print(e)
    # Send the user back to the home page
    return redirect(url_for('savings.home'))


@savings.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404
