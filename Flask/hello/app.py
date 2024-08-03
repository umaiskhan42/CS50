from flask import Flask, render_template, request

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])

def index():
    if request.method=="POST":
        name=request.form.get("name","world")
        return render_template("greet.html", name=name)
    else:
        return render_template("index.html")
    #return render_template("index.html")   # using render templates

# @app.route("/greet",methods=["GET","POST"])  # add methods 
# def greet():
#     name=request.args.get("name","world")
#     return render_template("greet.html", name=name)