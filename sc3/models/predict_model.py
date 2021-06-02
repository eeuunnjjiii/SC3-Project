from sc3 import db


class Predict(db.Model):
    __tablename__ = 'predict'

    id = db.Column(db.Integer(), primary_key=True)
    업종 = db.Column(db.String(45))
    브랜드 = db.Column(db.String(45))
    가맹점수 = db.Column(db.Integer())
    초기투자비용합계 = db.Column(db.Integer())
    예상평균매출액 = db.Column(db.Integer())

    def __repr__(self):
        return f'Data{self.브랜드}의 평가는 {self.예상평균매출액} 입니다.'