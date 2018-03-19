import sqlalchemy
import sqlalchemy.orm

from track_hymn.data.modelbase import SABase


class Hymn(SABase):
    __tablename__ = 'Hymn'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
