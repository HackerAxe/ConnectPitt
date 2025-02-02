import math
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import declarative_base
import datetime as dt

Base = declarative_base()

class User(Base):

    __tablename__ = "Users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    phoneNumber = Column("phoneNumber", String, nullable=False)
    linkedIn = Column("linkedIn", String, nullable=False)
    question_one = Column("question_one", Integer, nullable=False)
    question_two = Column("question_two", Integer, nullable=False)
    question_three = Column("question_three", Integer, nullable=False)
    question_four = Column("question_four", Integer, nullable=False)
    question_five = Column("question_five", Integer, nullable=False)
    question_six = Column("question_six", Integer, nullable=False)
    question_seven = Column("question_seven", Integer, nullable=False)
    question_eight = Column("question_eight", Integer, nullable=False)
    date_created = Column("date_created", Date, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, id, name, phone, social, q1, q2, q3, q4, q5, q6, q7, q8):
        self.id = id
        self.name = name
        self.pnum = phone
        self.social = social
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8

    #def to_JSON(self):
    #    return {"id":self.id,
    #           "name": self.name,
    #          "phoneNumber": self.pnum,
    #           "linkedIn": self.social,
    #           "question_one": self.q1,
    #           "question_two": self.q2,
    #           "question_three": self.q3,
    #           "question_four": self.q4,
    #           "question_five": self.q5,
    #           "question_six": self.q6,
    #           "question_seven": self.q7,
     #          "question_eight": self.q8
     #          }
    
    def percentDiff(self, valone, valtwo):
        val1=int(valone)
        val2=int(valtwo)
        return 2*abs(val1-val2)/(val1+val2)
    
    def avgPercentDiff(self, compuser):
        diff1=self.percentDiff(self.question_one, compuser.question_one)
        diff2=self.percentDiff(self.question_two, compuser.question_two)
        diff3=self.percentDiff(self.question_three, compuser.question_three)
        diff4=self.percentDiff(self.question_four, compuser.question_four)
        diff5=self.percentDiff(self.question_five, compuser.question_five)
        diff6=self.percentDiff(self.question_six, compuser.question_six)
        diff7=self.percentDiff(self.question_seven, compuser.question_seven)
        diff8=self.percentDiff(self.question_eight, compuser.question_eight)
        return (diff1+diff2+diff3+diff4+diff5+diff6+diff7+diff8)/8
    
