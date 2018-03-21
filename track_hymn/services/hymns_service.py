from track_hymn.data.dbsession import DBSessionFactory
from track_hymn.data.hymn import Hymn
from track_hymn.data.record import Record



class HymnsService:
    @staticmethod
    def get_hymns():
        session = DBSessionFactory.create_session()

        hymns = session.query(Hymn).order_by(Hymn.id).all()

        return hymns

    @staticmethod
    def get_user_hymns(user_id):
        session = DBSessionFactory.create_session()

        hymns = session.query(Record).filter(Record.user_id == user_id).order_by(Record.date).all()

        return hymns

    @staticmethod
    def old_get_hymns():
        return [
            {"id": 1,
             "title": "The Morning Breaks",
             },
            {"id": 2,
             "title": "The Spirit of God",
             },
            {"id": 3,
             "title": "Now Let Us Rejoice",
             },
        ]

    @staticmethod
    def record_hymns(opening, sacrament, rest, closing, user_id):
        session = DBSessionFactory.create_session()

        record = Record()
        record.open = opening
        record.sacrament = sacrament
        record.rest = rest
        record.close = closing
        record.user_id = user_id

        session.add(record)
        session.commit()

        return record
