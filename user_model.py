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
    question_one=Column("question_one", Integer, nullable=False)
    question_two=Column("question_two", Integer, nullable=False)
    question_three=Column("question_three", Integer, nullable=False)
    question_four=Column("question_four", Integer, nullable=False)
    question_five=Column("question_five", Integer, nullable=False)
    question_six=Column("question_six", Integer, nullable=False)
    question_seven=Column("question_seven", Integer, nullable=False)
    question_eight=Column("question_eight", Integer, nullable=False)
    date_created = Column("date_created", Date, nullable=False, default=dt.datetime.utcnow)

    def to_JSON(self):
        return{"id":self.id,
               "name": self.name,
               "phoneNumber": self.phoneNumber,
               "linkedIn": self.linkedIn,
               "question_one": self.question_one,
               "question_two": self.question_two,
               "question_three": self.question_three,
               "question_four": self.question_four,
               "question_five": self.question_five,
               "question_six": self.question_six,
               "question_seven": self.question_seven,
               "question_eight": self.question_eight
               }
    def percentDiff(valone, valtwo):
        return 2*Math.abs(valone-valtwo)/(valone+valtwo)
    def avgPercentDiff(compuser):
        diff1=percentDiff(self.question_one, compuser.question_one)
        diff2=percentDiff(self.question_two, compuser.question_two)
        diff3=percentDiff(self.question_three, compuser.question_three)
        diff4=percentDiff(self.question_four, compuser.question_four)
        diff5=percentDiff(self.question_five, compuser.question_five)
        diff6=percentDiff(self.question_six, compuser.question_six)
        diff7=percentDiff(self.question_seven, compuser.question_seven)
        diff8=percentDiff(self.question_eight, compuser.question_eight)
        return (diff1+diff2+diff3+diff4+diff5+diff6+diff7+diff8)/8
    
