from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine('postgresql://postgres:admin@localhost:5432/testdb',
    echo=True
)

Base=declarative_base()

Session=sessionmaker()