import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import sqlalchemy.orm as orm

from track_hymn.data.modelbase import SABase


class Record(SABase):
    __tablename__ = 'Record'

    id = Column(Integer, primary_key=True, autoincrement=True)
    open = Column(Integer)
    sacrament = Column(Integer)
    rest = Column(Integer)
    close = Column(Integer)
    user_id = Column(String, ForeignKey('User.id'), index=True)
    date = Column(DateTime, default=datetime.datetime.now, index=True)
