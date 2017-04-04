from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base


def connect_database(url):
    engine = create_engine('mysql://root:root@127.0.0.1:3306/fbdummy', echo=False)
    inspector = inspect(engine)

    for table_name in inspector.get_table_names():
        print table_name


def get_data():
    base = automap_base()
    engine = create_engine('mysql://root:root@127.0.0.1:3306/fbdummy', echo=False)
    base.prepare(engine, reflect=True)

    session = Session(engine)
    Status = base.classes.status

    session.add(Status(value='Pending'))
    session.commit()
