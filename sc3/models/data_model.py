from sc3 import db

class Project(db.Model):
    __tablename__ = 'project'
    
    id = db.Column(db.Integer(), primary_key=True)
    브랜드 = db.Column(db.String(45), nullable=False)
    업종 = db.Column(db.String(45), nullable=False)
    상호 = db.Column(db.String(45))
    가맹점수 = db.Column(db.Integer())
    기준연도 = db.Column(db.Integer())
    자산 = db.Column(db.Integer())
    자본 = db.Column(db.Integer())
    부채 = db.Column(db.Integer())
    법위반횟수 = db.Column(db.Integer())
    매출액 = db.Column(db.Integer())
    영업이익 = db.Column(db.Integer())
    당기순이익 = db.Column(db.Integer())
    초기투자비용합계 = db.Column(db.Integer())
    신규개점 = db.Column(db.Integer())
    계약종료 = db.Column(db.Integer())
    계약해지 = db.Column(db.Integer())
    명의변경 = db.Column(db.Integer())
    평균매출액 = db.Column(db.Integer())
    평가 = db.Column(db.String(45))
    tweets = db.relationship('Check', backref='project', cascade = 'all,delete')
    
    def __repr__(self):
        return f'Data{self.브랜드}의 평가는 {self.평가} 입니다.'