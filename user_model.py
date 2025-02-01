from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import declarative_base
import datetime as dt
import os

Base = declarative_base()

class User(Base):

    __tablename__ = "Users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    phoneNumber = Column("phoneNumber", String, nullable=False)
    LinkedIn = Column("LinkedIn", String, nullable=False)
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
               "LinkedIn": self.LinkedIn,
               "question_one": self.question_one,
               "question_two": self.question_two,
               "question_three": self.question_three,
               "question_four": self.question_four,
               "question_five": self.question_five,
               "question_six": self.question_six,
               "question_seven": self.question_seven,
               "question_eight": self.question_eight
               }