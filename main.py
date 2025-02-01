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
    LinkedIn=request.form["LinkedIn"]
    question_one=request.form["question_one"]
    question_two=request.form["question_two"]
    question_three=request.form["question_three"]
    question_four=request.form["question_four"]
    question_five=request.form["question_five"]
    question_six=request.form["question_six"]
    question_seven=request.form["question_seven"]
    question_eight=request.form["question_eight"]

    new_user=User(name=name, phoneNumber=phoneNumber, LinkedIn=LinkedIn, question_one=question_one,
                  question_two=question_two, question_three=question_three, question_four=question_four,
                  question_five=question_five, question_six=question_six, question_seven=question_seven,
                  question_eight=question_eight)
    new_user_in_JSON_format=new_user.toJSON()
    users = session.query(User).order_by(User.date_created).all()
    groupInJSONFormat=[]
    done=false
    maxAvgPercentDiff=0.0
    while done==false:
        for user in users:
            currUserInJSONFormat=user.toJSON()
            
            
    
    

    
    print(new_user_in_JSON_format)

    try:
        session.add(new_user)
        session.commit()
        return render_template("results.html", user=new_user_in_JSON_format)
    except:
        return 'Issue adding task'

if __name__ == '__main__':
    app.run(debug=True)
