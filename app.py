from flask import Flask, render_template, request #1.import flask module

#2.instantiate an object for this class flask
app = Flask(__name__)   #we pass in the current module identify by __name__

#4.with the decorator route called on the app variable
#forward a load on the server : repesented by (/)
#The request is made on the (/)
@app.route('/')
def index():
     #6.return '<h1>Text example</h1>' or look for index page on the project
    return render_template('form.html')          

#3.run the app
if __name__ == '__main__':
    app.run(debug=True) #5.debug=True means any change will take effect immediately


