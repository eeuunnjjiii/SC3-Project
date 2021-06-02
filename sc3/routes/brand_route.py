from flask import Blueprint, render_template, request, redirect, url_for, Response
from sc3.models.data_model import Project
from sc3.models.check_model import Check
from sc3 import db
from sc3.utils import main_funcs
import requests
from bs4 import BeautifulSoup


bp = Blueprint('brand', __name__, url_prefix='/brand')

@bp.route('/')
def index(): #http://127.0.0.1:5000/brand/?brandname=
    brandname = request.args.get('brandname', None)

    keyword="%{}%".format(brandname)
    data_list=Project.query.filter(Project.브랜드.like(keyword)).all()

    #brandname이 주어지지 않았을 때
    if brandname == None:
        return render_template('brand.html')

    #brandname이 db에 없을 때
    elif not data_list :
        try :
            address_keyword = str(brandname)
            url="https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=1&acq=60&qdt=0&ie=utf8&query="+ address_keyword
            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')
            link_text=soup.find(class_='source_url').text

            return render_template('brand_error.html', link_text=link_text)

        except:
            return render_template('brand_error.html')

    else:
        return render_template('brand.html', data_list=data_list)
       


@bp.route('/<brandname>')
def add_brandname(brandname=None):

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

    keyword="%{}%".format(brandname)
    data_list=Project.query.filter(Project.브랜드.like(keyword)).all()
    
    return render_template('brand.html', alert_msg=alert_msg, data_list=data_list)