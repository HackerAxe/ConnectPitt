from flask import Flask, redirect, render_template, request, session, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user_model import Base, User

app = Flask(__name__)

engine = create_engine("sqlite:///users.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/results", methods=["POST"])
def results():
    name=request.form["name"]
    phoneNumber=request.form["phoneNumber"]
    linkedIn=request.form["LinkedIn"]
    question_one=request.form["question_one"]
    question_two=request.form["question_two"]
    question_three=request.form["question_three"]
    question_four=request.form["question_four"]
    question_five=request.form["question_five"]
    question_six=request.form["question_six"]
    question_seven=request.form["question_seven"]
    question_eight=request.form["question_eight"]

    new_user=User(name=name, phoneNumber=phoneNumber, linkedIn=linkedIn, question_one=question_one,
                  question_two=question_two, question_three=question_three, question_four=question_four,
                  question_five=question_five, question_six=question_six, question_seven=question_seven,
                  question_eight=question_eight)
    new_user_in_JSON_format=new_user.toJSON()
    users = session.query(User).order_by(User.date_created).all()
    group=[]
    groupInJSONFormat=[]
    done=false
    maxAvgPercentDiff=0.0
    if len(users)>0:
        while done==false:
            for currUser in users:
                currUserInJSONFormat=user.toJSON()
                avgPercentDiff=new_user.avgPercentDiff(new_user, currUser)
                if avgPercentDiff<=maxAvgPercentDiff: 
                    group.add(user)
                    groupINJSONFormat.add(currUserInJSONFormat)
            if len(group)>0: done=true
            else: maxAvgPercentDiff=maxAvgPercentDiff+0.1

    print(groupINJSONFormat)

    try:
        session.add(new_user)
        session.commit()
        return render_template("results.html", users=groupINJSONFormat)
    except:
        return 'Issue adding task'

if __name__ == '__main__':
    app.run(debug=True)
