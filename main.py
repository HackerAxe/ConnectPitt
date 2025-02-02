from flask import Flask, render_template, request, session, url_for
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from user_model import Base, User

app = Flask(__name__)

engine = create_engine("sqlite:///users.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def main():
    return render_template("index.html", results_ref=url_for('results'))

@app.route("/results", methods=["POST"])
def results():

    # Retrieve Form Values
    name = request.form["name"]
    pNum = request.form["phoneNumber"]
    social = request.form["linkedIn"]
    q1 = request.form["question_one"]
    q2 = request.form["question_two"]
    q3 = request.form["question_three"]
    q4 = request.form["question_four"]
    q5 = request.form["question_five"]
    q6 = request.form["question_six"]
    q7 = request.form["question_seven"]
    q8 = request.form["question_eight"]

    # Create a new User
    new_user=User(name=name, phoneNumber=pNum, linkedIn=social, question_one=q1,
                  question_two=q2, question_three=q3, question_four=q4,
                  question_five=q5, question_six=q6, question_seven=q7,
                  question_eight=q8)
    
    # Convert to JSON & Delete ID
    new_user_JSON = new_user.to_JSON()
    del new_user_JSON["id"]

    print(new_user_JSON)

    # Add to DataBase
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


    try:
        session.add(new_user)
        session.commit()
        return render_template('results.html', request=new_user_JSON)
    except:
        return 'Issue adding task'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
