from flask import Blueprint, render_template 

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new_facts')
def new_facts():
    return render_template('facts/new_facts.html')
