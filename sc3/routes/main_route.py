from flask import Blueprint, render_template
from sc3.models.data_model import Project

bp = Blueprint('main', __name__)

@bp.route('/') #http://127.0.0.1:5000
def index():
    return render_template('index.html')
 