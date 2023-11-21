#!/usr/bin/python3
"""module execute sql query using SQLAlchemy module"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import Session


def main(argv):
    """function containing the connection and executing the query"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).order_by(asc(State.id)).first()
    if (state):
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == '__main__':
    if (len(sys.argv) == 4):
        main(sys.argv)
