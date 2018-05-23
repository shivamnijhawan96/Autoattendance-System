import sys 
from sqlalchemy import Column, ForeignKey,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()
class Attendance(Base):
    __tablename__ = 'attendance_record'

    name = Column(String(80))
    attend = Column(String(5))
    roll_no = Column(String(12),primary_key=True)
    

engine = create_engine('sqlite:///attendance.db')
Base.metadata.create_all(engine)
