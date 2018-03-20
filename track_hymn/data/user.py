import datetime
import uuid
from sqlalchemy import Column, String, Boolean, DateTime, Integer

from track_hymn.data.modelbase import SABase


class User(SABase):
    __tablename__ = 'User'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()).replace('-', ''))
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    stake = Column(String)
    ward = Column(String)
    zip = Column(Integer)
    created = Column(DateTime, default=datetime.datetime.now, index=True)
    is_admin = Column(Boolean, default=False, nullable=False)
