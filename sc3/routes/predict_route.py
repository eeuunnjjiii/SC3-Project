from flask import Blueprint, render_template, request
from sc3.models.predict_model import Predict
from sc3.models.data_model import Project
from sc3 import db
from sc3.utils import main_funcs
from sc3.utils.predict import predict

bp = Blueprint('predict', __name__, url_prefix='/predict')

@bp.route('/')
def index(): 
    brandname = request.args.get('brandname', None)

    keyword="%{}%".format(brandname)
    data_list=Project.query.filter(Project.브랜드.like(keyword)).all()

    #brandname이 주어지지 않았을 때
    if brandname == None:
        return render_template('predict.html')

    #brandname이 db에 없을 때
    elif not data_list :
        return render_template('brand_error.html')

    else:
        return render_template('predict.html', data_list=data_list)


@bp.route('/sales')
def sales(): 
    
    industry = request.args.get('industry', None)
    brandname = request.args.get('brandname', None)   
    franchisenum = request.args.get('franchisenum', None)
    invest = request.args.get('invest', None)

    #머신러닝을 위한 정수형변경
    industry_int = int(industry)
    franchisenum_int = int(franchisenum)
    invest_int = int(invest)

    #머신러닝 결과 리턴
    res = predict(industry_int, franchisenum_int, invest_int)

    #메세지
    alert_msg = main_funcs.msg_processor(3)

    #DB추가
    brand = Predict(업종=industry,
                브랜드=brandname,
                가맹점수=franchisenum,
                초기투자비용합계=invest,
                예상평균매출액=res[1])

    db.session.add(brand)
    db.session.commit()

    data_list=Predict.query.all()

    return render_template('predict.html', res=res, alert_msg = alert_msg, data_list=data_list)




@bp.route('/<id>')
def delete_id(id=None):

    #db에서 조회
    predict = Predict.query.filter(Predict.id == id).first()

    #이미 추가된 brandname이면,
    if predict:
        db.session.delete(predict)
        db.session.commit()

    alert_msg = main_funcs.msg_processor(1)
    data_list=Predict.query.all()
    
    return render_template('predict.html', alert_msg=alert_msg, data_list=data_list)

    

