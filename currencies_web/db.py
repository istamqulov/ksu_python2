from sqlalchemy import Integer, Column, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from currencies.main import Currencies

Base = declarative_base()


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    code = Column(String)

    def __str__(self):
        return self.name


engine = create_engine(
    "mysql://root:pp0nlin3devbong@localhost/test_currencies?charset=utf8mb4",
    echo=True,
)


session = sessionmaker(
    bind=engine,
)()
Base.metadata.create_all(engine)

service = Currencies()
currencies = service.load_currencies()


def create_initial_currencies():
    for code, name in currencies.items():
        currency = Currency(
            name=name,
            code=code
        )
        session.add(currency)
    session.commit()


usd = session.query(Currency).filter(
   Currency.code == 'usd'
).first()
print(usd)
