from passlib.handlers.sha2_crypt import sha512_crypt

from track_hymn.data.dbsession import DBSessionFactory
from track_hymn.data.user import User


class AccountService:
    @staticmethod
    def create_user(username, plain_text_pw, stake, ward, zip):
        session = DBSessionFactory.create_session()

        user = User()
        user.username = username
        user.password_hash = AccountService.hash_text(plain_text_pw)
        user.stake = stake
        user.ward = ward
        user.zip = zip

        session.add(user)
        session.commit()

        return user

    @staticmethod
    def hash_text(plain_text_pw):
        hashed_text = sha512_crypt.encrypt(plain_text_pw, rounds=150000)
        return hashed_text

    @classmethod
    def find_username(cls, username):
        if not username or not username.strip():
            return None

        username = username.lower().strip()

        session = DBSessionFactory.create_session()
        user = session.query(User).filter(User.username == username).first()

        return user

    @classmethod
    def authenticate(cls, username, plain_text_pw):
        user = AccountService.find_username(username)
        if not user:
            return None

        if not sha512_crypt.verify(plain_text_pw, user.password_hash):
            return None

        return user
