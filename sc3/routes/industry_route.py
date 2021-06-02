from flask import Blueprint, render_template, request
from sc3.models.data_model import Project
from sc3.models.check_model import Check
from sc3 import db
from sc3.utils import main_funcs

bp = Blueprint('industry', __name__, url_prefix='/industry')


@bp.route('/')
def index(): #http://127.0.0.1:5000/industry/?industryname=
    industryname = request.args.get('industryname', None)

    keyword = "%{}%".format(industryname)
    data_list = Project.query.filter(Project.업종.like(keyword), Project.기준연도 == 2020).order_by(Project.평균매출액.desc()).limit(1)
    industry_all = Project.query.filter(Project.업종.like(keyword)).all()
    
    #industryname이 없을 때,
    if industryname == None:
        return render_template('industry.html')

    #industryname이 db에 없을 때,
    elif not industry_all :
        return render_template('industry_error.html')
   
    else:
        return render_template('industry.html', data_list=data_list)



@bp.route('/<industryname>/<brandname>')
def add_brandname(industryname=None, brandname=None):

    #db에서 조회
    choice = Project.query.filter(Project.브랜드 == brandname, Project.기준연도==2020).first()
    check = Check.query.filter(Check.브랜드 == brandname).first()

    #brandname이 주어지지 않으면,
    if brandname==None:
        return render_template('brand.html') 

    #이미 추가된 brandname이면,
    elif check:
        db.session.delete(check)
        db.session.commit()


    #새로 추가된 brandname이면,
    brand = Check(브랜드_id=choice.id, 
            브랜드=choice.브랜드,
            상호=choice.상호,
            가맹점수=choice.가맹점수,
            초기투자비용합계=choice.초기투자비용합계,
            신규개점=choice.신규개점,
            계약종료=choice.계약종료,
            계약해지=choice.계약해지,
            평균매출액=choice.평균매출액,)
            
    db.session.add(brand)
    db.session.commit()

    alert_msg = main_funcs.msg_processor(0)
    
    keyword = "%{}%".format(industryname)
    data_list = Project.query.filter(Project.업종.like(keyword), Project.기준연도 == 2020).order_by(Project.평균매출액.desc()).limit(1)
        
    return render_template('industry.html', alert_msg=alert_msg, data_list=data_list)