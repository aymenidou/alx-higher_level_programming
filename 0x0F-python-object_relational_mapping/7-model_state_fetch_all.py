#!/usr/bin/python3
import sys
from model_state import State, Base
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import Session


def main(argv):
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(asc(State.id)).all():
        print("{}: {}".format(state.id, state.name))
    session.close()


if __name__ == '__main__':
    if (len(sys.argv) == 4):
        main(sys.argv)
