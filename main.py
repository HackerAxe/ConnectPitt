from flask import Flask, render_template, request, session, url_for
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

app = Flask(__name__)
class Base(DeclarativeBase): pass
engine = create_engine('sqlite:///allusers.db', echo=True)

class Users(Base):
    __tablename__ = "Users"
    _id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    phone = Column('phone', String)
    social = Column('social', String)
    q1 = Column('q1', Integer)
    q2 = Column('q2', Integer)
    q3 = Column('q3', Integer)
    q4 = Column('q4', Integer)
    q5 = Column('q5', Integer)
    q6 = Column('q6', Integer)
    q7 = Column('q7', Integer)
    q8 = Column('q8', Integer)
    _date = Column('date', String)

    def __init__(self, name, phone, social, q1, q2, q3, q4, q5, q6, q7, q8):
        self.name = name
        self.phone = phone
        self.social = social
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def main():
    return render_template("index.html", results_ref=url_for('results'))

@app.route("/results", methods=["POST"])
def results():
    
    # Retrieve Form Values - Working
    name = request.form["name"]
    pnum = request.form["phoneNumber"]
    social = request.form["linkedIn"]
    q1 = request.form["question_one"]
    q2 = request.form["question_two"]
    q3 = request.form["question_three"]
    q4 = request.form["question_four"]
    q5 = request.form["question_five"]
    q6 = request.form["question_six"]
    q7 = request.form["question_seven"]
    q8 = request.form["question_eight"]
    
    # Create a new User - Working
    user = Users(name, pnum, social, q1, q2, q3, q4, q5, q6, q7, q8)

    # Add & Commit New User to DataBase - Working
    session.add(user)
    session.commit()

    # Return dictionary to results.html
    users_all = session.query(Users).all() 
    return render_template('results.html', users = users_all)

    # users = session.query(User).order_by(User.date_created).all()
    # group=[]
    # groupInJSONFormat=[]
    # done=False
    # maxAvgPercentDiff=0.0
    
    # Issue Here
    #if len(users)>0:
    #    while done==False:
    #       for currUser in users:
    #            currUserInJSONFormat=currUser.to_JSON()
    #            avgPercentDiff=new_user.avgPercentDiff(currUser) # Error
    #            if avgPercentDiff<=maxAvgPercentDiff: 
    #                group.add(currUser)
    #                groupInJSONFormat.add(currUserInJSONFormat)
    #        if len(group)>0: done=True
    #       else: maxAvgPercentDiff=maxAvgPercentDiff+0.1

    #try:
        #session.add(new_user)
        #session.commit()
        
    #except:
        #return 'Issue adding task'
    
# Nearest Neighbors Algorithm
def clustering():
    pass
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
