from flask import Flask, redirect, render_template, request, url_for
import mysql.connector

# creating an object to connect to MySQL


app = Flask(__name__)


mysql = mysql.connector.connect(host = 'localhost', user = 'root', password = 'admin', database = 'crime')

# creating cursor object to execute mysql queries in python code
mycursor = mysql.cursor()

# Link four pages to the flask app
@app.route('/')
def mainpage():
    return render_template('index.html')
    
@app.route('/index.html')
def hello():
    return render_template('index.html')


@app.route('/victim.html')
def victim():
    return render_template('victim.html')


@app.route('/investigator.html')
def investigator():
    return render_template('investigator.html')

@app.route('/admin.html')
def admin():
    return render_template('admin.html')


@app.route('/vregister.html',methods=['GET','POST'])
def vregister():

    # checking if data is inputted
    if (request.method == 'POST'):

        # check the data for any errors
        for x in request.form:
            print(request.form[x], end=" : ")
            print(type(request.form[x]))

        # saving sql command in a variable
        sql_Insert_Query = "INSERT INTO victim (vname,address, age, mobileno,gender,email, password ) VALUES (%s, %s,%s, %s, %s, %s, %s)"

        # fetching data from HTML form to python code and storing it in a list
        Input_From_User = []
        for x in request.form:
            Input_From_User.append(str(request.form[x]))

        # typecasting from list to tuple
        Input_From_User = tuple(Input_From_User)

        # if UserName is not present in the Database then register it in the database
        mycursor.execute(sql_Insert_Query, Input_From_User)

        mysql.commit()
        return "Account registered successfully!!!"

    return render_template('vregister.html')

@app.route('/iregister.html')
def iregister():

    if(request.method == 'POST'):
        
        # check the data for any errors
        for x in request.form:
            print(request.form[x], end=" : ")
            print(type(request.form[x]))

        # saving sql command in a variable
        sql_Insert_Query = "INSERT INTO investigator (name,area, mobileno,mailid, password ) VALUES (%s, %s,%s, %s, %s)"

        # fetching data from HTML form to python code and storing it in a list
        Input_From_User = []
        for x in request.form:
            Input_From_User.append(str(request.form[x]))

        # typecasting from list to tuple
        Input_From_User = tuple(Input_From_User)

        # if UserName is not present in the Database then register it in the database
        mycursor.execute(sql_Insert_Query, Input_From_User)

        mysql.commit()
        return "Account registered successfully!!!"


    return render_template('iregister.html')


if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)