from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.ext.declarative import DeclarativeMeta

Base: DeclarativeMeta = declarative_base()

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cases = relationship("Case", back_populates="client")

class Lawyer(Base):
    __tablename__ = 'lawyers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cases = relationship("Case", back_populates="lawyer")

class Case(Base):
    __tablename__ = 'cases'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'))
    lawyer_id = Column(Integer, ForeignKey('lawyers.id'))
    client = relationship("Client", back_populates="cases")
    lawyer = relationship("Lawyer", back_populates="cases")

DATABASE_URL = "sqlite:///./case_management.db"
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)