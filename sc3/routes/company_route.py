from flask import Blueprint, render_template, request
from sc3.models.data_model import Project
from sc3.models.check_model import Check
from sc3 import db
from sc3.utils import main_funcs

bp = Blueprint('company', __name__, url_prefix='/company')


@bp.route('/')
def index(): #http://127.0.0.1:5000/company/?companyname=핫시즈너
    companyname = request.args.get('companyname', None)
    keyword="%{}%".format(companyname)
    data_list=Project.query.filter(Project.상호.like(keyword), Project.기준연도==2020).all()
    return render_template('company.html', data_list=data_list)

@bp.route('/<brandname>')
def add_brandname(brandname=None):

    #db에서 조회
    choice = Project.query.filter(Project.브랜드 == brandname, Project.기준연도==2020).first()
    check = Check.query.filter(Check.브랜드 == brandname).first()

    #이미 추가된 brandname이면,
    if check:
            db.session.delete(check)
            db.session.commit()


    #새로 추가된 brandname이면,
        #SQL 구문 : INSERT INTO Check SELECT * FROM Project WHERE 브랜드 == brandname

    brand = Check(id=choice.id, 
        브랜드=choice.브랜드,
        업종=choice.업종,
        상호=choice.상호,
        가맹점수=choice.가맹점수,
        기준연도=choice.기준연도,
        자산=choice.자산,
        자본=choice.자본,
        부채=choice.부채,
        법위반횟수=choice.법위반횟수,
        매출액=choice.매출액,
        영업이익=choice.영업이익,
        당기순이익=choice.당기순이익,
        초기투자비용합계=choice.초기투자비용합계,
        신규개점=choice.신규개점,
        계약종료=choice.계약종료,
        계약해지=choice.계약해지,
        명의변경=choice.명의변경,
        평균매출액=choice.평균매출액,
        평가=choice.평가)
        
    db.session.add(brand)
    db.session.commit()

    alert_msg = main_funcs.msg_processor(0)

    return render_template('company.html', alert_msg=alert_msg)