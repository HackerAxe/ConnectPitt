from flask import Flask, render_template, request, session, url_for
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
    return render_template("index.html", results_ref=url_for('results'))

@app.route("/results", methods=["POST", "GET"])
def results():

    name=request.form["name"]
    phoneNumber=request.form["phoneNumber"]
    linkedIn=request.form["linkedIn"]
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
    
    new_user_in_JSON_format=new_user.to_JSON()

    users = session.query(User).order_by(User.date_created).all()
    group=[]
    groupInJSONFormat=[]
    done=False
    maxAvgPercentDiff=0.0
    if len(users)>0:
        while done==False:
            for currUser in users:
                currUserInJSONFormat=currUser.to_JSON()
                avgPercentDiff=new_user.avgPercentDiff(currUser) # Error
                if avgPercentDiff<=maxAvgPercentDiff: 
                    group.add(currUser)
                    groupInJSONFormat.add(currUserInJSONFormat)
            if len(group)>0: done=True
            else: maxAvgPercentDiff=maxAvgPercentDiff+0.1

    print(groupInJSONFormat)

    try:
        session.add(new_user)
        session.commit()
        return render_template("results.html", users=groupInJSONFormat)
    except:
        return 'Issue adding task'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
