from flask import Blueprint, render_template, request, redirect, url_for
from sc3.models.check_model import Check
from sc3 import db
from sc3.utils import main_funcs

bp = Blueprint('check', __name__, url_prefix='/check')

@bp.route('/')
def index(): 
    data_list=Check.query.all()
    return render_template('check.html', data_list=data_list)

@bp.route('/<brandname>')
def delete_brandname(brandname=None):

    #db에서 조회
    check = Check.query.filter(Check.브랜드 == brandname).first()

    #이미 추가된 brandname이면,
    if check:
        db.session.delete(check)
        db.session.commit()

    alert_msg = main_funcs.msg_processor(1)
    data_list=Check.query.all()
    
    return render_template('check.html', alert_msg=alert_msg, data_list=data_list)