import sqlalchemy
import sqlalchemy.orm

from track_hymn.data.modelbase import SABase


class Ward(SABase):
    __tablename__ = 'Ward'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)

    stake_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Stake.id'))
    stake = sqlalchemy.orm.relationship('Stake', back_populates='wards')
