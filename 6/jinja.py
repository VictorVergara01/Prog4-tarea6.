from main import app 

from flask import render_template

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/jinja")
def Jinja():

    my_name= "Victor"

    return render_template("jinja.html", my_name=my_name)

@app.route("/about")
def about():
    return "<h1 style='color:blue'>hola estudio en la uip</h1>"