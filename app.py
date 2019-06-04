

import pymongo
from flask import Flask, render_template, request

from flask import Flask, render_template, json, request
from flask import Flask, render_template
from flask import Flask
app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["databaseuse"]
mycol = mydb["users"]



@app.route("/")
def main():
 return render_template('index.html')

@app.route("/alumni")
def alumni():
 return render_template('alumni.html')

@app.route("/student")
def student():
 return render_template('student.html')
 #put code here to access the interests of the student from the db
 #and display it somewhere on the page

@app.route("/form")
def form():
  return render_template('form.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/Showlogin')
def Login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def LoginUser():
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _status = request.form['status']

    if _email and _password:


     myquery = {"email": _email , "password":_password , "status": _status }


     mydoc = mycol.find(myquery)

    for x in mydoc:
        if _status == "student":
         return render_template('student.html')
        else:
            return render_template('alumni.html')
    else:
        return render_template('login.html')








@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values from the UI

    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _status = request.form['status']
    if _status == "student":
        _status2 = "student"
    else:
        _status2 = "alumni"


    # validate the received values
    if _name and _email and _password:

        myquery = {"email": _email, "password": _password}

        mydoc = mycol.find(myquery)

        for x in mydoc:
            return  render_template('signup.html')
            print('user is signed up')
        else:

         mydict = {"name": _name, "email": _email, "password": _password , "confirm": "No" , "status": _status2 }

        x = mycol.insert_one(mydict)
        return render_template('alumni.html')








if __name__ == "__main__":
 app.run()





