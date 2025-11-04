from models.model_base import Model_basel

from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future.engine import Engine

__engine: Optional[Engine] = None

def create_engine():
    global __engine

    if __engine:
        return
    
    conn_str = "postgresql://postgres:root@localhost:5432/usuarios_3"
    __engine = sa.create_engine(url=conn_str, echo=False)

    return __engine


def create_session() -> Session:
    global __engine

    if not __engine:
        create_engine()

    __session = sessionmaker(bind=__engine, expire_on_commit=False, class_=Session)

    session: Session = __session()

    return session


def create_table():
    global __engine

    if not __engine:
        create_engine()

    import models.__all_models

    Model_basel.metadata.drop_all(__engine)
    Model_basel.metadata.create_all(__engine)