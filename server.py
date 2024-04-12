from flask import Flask, request, render_template
import data_loader

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recipes/", methods=['POST'])
def get_recipies():
    x = data_loader.load("./recipes/"+request.form['user']+".json")
    return x
 
