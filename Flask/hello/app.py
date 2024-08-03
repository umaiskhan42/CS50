from flask import Flask, render_template, request

app=Flask(__name__)
@app.route("/")

def index():

    return render_template("index.html")   # using render templates

@app.route("/greet",methods=["GET","POST"])  # add methods 
def greet():
    name=request.args.get("name","world")
    return render_template("greet.html", name=name)