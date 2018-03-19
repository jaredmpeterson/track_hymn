from track_hymn.data.dbsession import DBSessionFactory
from track_hymn.data.hymn import Hymn


class HymnsService:
    @staticmethod
    def get_hymns():
        session = DBSessionFactory.create_session()

        hymns = session.query(Hymn).order_by(Hymn.id).all()

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
