import datetime
import sqlalchemy as sa

from track_hymn.data.modelbase import SABase


class User(SABase):
    __tablename__ = 'User'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column(sa.String, unique=True)
    stake = sa.Column(sa.String)
    ward = sa.Column(sa.String)
    zip = sa.Column(sa.Integer)
    created = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    is_admin = sa.Column(sa.Boolean, default=False)
