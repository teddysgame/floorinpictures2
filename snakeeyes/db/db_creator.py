from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///vinyllib.db', echo=True)
Base = declarative_base()


class Label(Base):
    __tablename__ = "label"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Label: {}>".format(self.name)


class Album(Base):
    """"""
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    title = Column(String)
    code = Column(String)
    price = Column(Integer)

    label_id = Column(Integer, ForeignKey("labels.id"))
    label = relationship("Label", backref=backref(
        "albums", order_by=id))


# create tables
Base.metadata.create_all(engine)