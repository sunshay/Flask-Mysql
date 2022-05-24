# from crypt import methods
from unicodedata import name
from flask import Flask, render_template, request #1.import flask module
from flask_pymysql import MySQL
import yaml


#2.instantiate an object for this class flask
app = Flask(__name__)   #we pass in the current module identify by __name__

#13 import yaml file
db =  yaml.load(open('db.yaml'))
#12.configure db + #13.1 add value from yaml file 
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_ USER']= db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = ''

#14 instanciate an object for MySQL module
mysql = MySQL(app)


#4.with the decorator route called on the app variable
#forward a load on the server : repesented by (/)
#The request is made on the (/)
@app.route('/', methods=['GET', 'POST']) #10.add method GET and POST and add if request in the function to choose between POST or GET
def index():
    if request.method == 'POST': #11.store user info name and email 
        # fetch the form data
        userDetails = request.form 
        name = userDetails['name']
        email = userDetails['email']
    #15 use mysql object within our POST request to make an entry into the database
        cur = mysql.connection.cursor() 
    #15.1 after create a cursor cur; we can make queries on our database / %s is string 
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return 'succes'

     #6.return '<h1>Text example</h1>' or look for index page on the project
    return render_template('form.html')          

#3.run the app
if __name__ == '__main__':
    app.run(debug=True) #5.debug=True means any change will take effect immediately


