from track_hymn.data.modelbase import SABase
import sqlalchemy
import sqlalchemy.orm as orm
import track_hymn.data.user
import track_hymn.data.ward
import track_hymn.data.stake
import track_hymn.data.hymn


class DBSessionFactory:
    factory = None

    @staticmethod
    def global_init(db_file):
        if DBSessionFactory.factory:
            return

        if not db_file:
            raise Exception("You must specify a data file.")

        conn_str = 'sqlite:///' + db_file
        print("Connecting to db with: {}".format(conn_str))
        engine = sqlalchemy.create_engine(conn_str, echo=True)
        SABase.metadata.create_all(engine)
        DBSessionFactory.factory = orm.sessionmaker(bind=engine)

    @staticmethod
    def create_session():
        return DBSessionFactory.factory()
