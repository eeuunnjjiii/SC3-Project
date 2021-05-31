from flask import Blueprint, render_template
from sc3.models.data_model import Project

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/user')
def brand_index():
    #data_list = data_model.get_data('죠스떡볶이')
    return render_template('index.html')

