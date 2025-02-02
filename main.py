from flask import Flask, render_template, request, session, url_for
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from user_model import Base, User

app = Flask(__name__)

engine = create_engine("sqlite:///users.db", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

id = 0

@app.route("/")
def main():
    return render_template("index.html", results_ref=url_for('results'))

@app.route("/results", methods=["POST"])
def results():
    
    # Retrieve Form Values
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

    user_object = {'Name':name, 'Phone Number':pnum, 'LinkedIn':social, 
                'Question 1':q1, 
                'Question 2':q2, 'Question 3':q3, 'Question 4':q4, 
                'Question 5':q5, 'Question 6': q6, 'Question7': q7, 
                'Question 8':q8}
    
    # Create a new User
    # Add to DataBase
    print(pnum)
    global id
    id += 1
    session.add(User(id=0, name=name, phone=0, social=social, q1=0,
                  q2=1, q3=2, q4=3, q5=5, q6=7, q7=8, q8=9))
    session.commit()

    return render_template('results.html', request = user_object)
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
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
