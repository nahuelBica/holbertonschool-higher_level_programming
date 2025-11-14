#!/usr/bin/python3
"""
Script used to get all states from db
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    av = sys.argv[1:]
    engine = create_engine(
        f'mysql+mysqldb://{av[0]}:{av[1]}@localhost/{av[2]}',
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session(engine)

    states = session.query(State).order_by(State.id).all()

    for s in states:
        print('{}: {}'.format(s.id, s.name))
