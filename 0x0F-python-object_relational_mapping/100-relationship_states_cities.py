#!/usr/bin/python3
"""module execute sql query using SQLAlchemy module"""
import sys
from relationship_state import State, Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def main(argv):
    """function containing the connection and executing the query"""
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)
    session.add(state)
    session.commit()
    session.close()


if __name__ == '__main__':
    if (len(sys.argv) == 4):
        main(sys.argv)
