import sqlalchemy
import sqlalchemy.orm

from track_hymn.data.modelbase import SABase


class Stake(SABase):
    __tablename__ = 'Stake'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)

    wards = sqlalchemy.orm.relationship('Ward', back_populates='stake')
