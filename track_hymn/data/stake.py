import sqlalchemy
import sqlalchemy.orm as orm

from track_hymn.data.modelbase import SABase


class Stake(SABase):
    __tablename__ = 'Stake'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    state = sqlalchemy.Column(sqlalchemy.String, index=True)

    wards = orm.relationship('Ward', back_populates='stake')
