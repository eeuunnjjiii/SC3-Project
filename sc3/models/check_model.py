from sc3 import db


class Check(db.Model):
    __tablename__ = 'check'

    id = db.Column(db.Integer(), primary_key=True)
    브랜드_id = db.Column(db.Integer(), db.ForeignKey('project.id'))
    브랜드 = db.Column(db.String(45), nullable=False)
    상호 = db.Column(db.String(45))
    가맹점수 = db.Column(db.Integer())
    초기투자비용합계 = db.Column(db.Integer())
    신규개점 = db.Column(db.Integer())
    계약종료 = db.Column(db.Integer())
    계약해지 = db.Column(db.Integer())
    평균매출액 = db.Column(db.Integer())
    

    def __repr__(self):
        return f'Data{self.브랜드}, {self.평균매출액} 입니다.'