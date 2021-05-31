"""empty message

Revision ID: 4011efb4df41
Revises: 623e7f8a5e17
Create Date: 2021-05-30 11:46:54.504500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4011efb4df41'
down_revision = '623e7f8a5e17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('check', sa.Column('업종', sa.String(length=45), nullable=True))
    op.add_column('check', sa.Column('상호', sa.String(length=45), nullable=True))
    op.add_column('check', sa.Column('가맹점수', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('기준연도', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('자산', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('자본', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('부채', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('법위반횟수', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('매출액', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('영업이익', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('당기순이익', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('초기투자비용합계', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('신규개점', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('계약종료', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('계약해지', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('명의변경', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('평균매출액', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('평가', sa.String(length=45), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('check', '평가')
    op.drop_column('check', '평균매출액')
    op.drop_column('check', '명의변경')
    op.drop_column('check', '계약해지')
    op.drop_column('check', '계약종료')
    op.drop_column('check', '신규개점')
    op.drop_column('check', '초기투자비용합계')
    op.drop_column('check', '당기순이익')
    op.drop_column('check', '영업이익')
    op.drop_column('check', '매출액')
    op.drop_column('check', '법위반횟수')
    op.drop_column('check', '부채')
    op.drop_column('check', '자본')
    op.drop_column('check', '자산')
    op.drop_column('check', '기준연도')
    op.drop_column('check', '가맹점수')
    op.drop_column('check', '상호')
    op.drop_column('check', '업종')
    # ### end Alembic commands ###
