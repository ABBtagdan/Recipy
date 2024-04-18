from flask import Flask, request, render_template
from markupsafe import escape
import data_loader
import tools

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_user/", methods=["GET", "POST"])
def create_user():
    if request.method == "GET":
        return render_template("new_user_form.html")


@app.route("/recipes/", methods=["GET"])
def get_recipies():
    x = data_loader.load("./recipes/" + request.args["user"] + ".json")
    filter = request.args.getlist("filter")
    x = tools.filter(x, filter)
    return render_template("recipes.html", recipes=x)


@app.route("/filter_card", methods=["GET", "DELETE"])
def filter_card():
    if request.method == "GET":
        filter: str = request.args["filter"]
        filter = filter.strip()
        return f'<li hx-trigger="click" hx-target="this" hx-delete="/filter_card" hx-swap="outerHTML"><input type="hidden" name="filter" value="{escape(filter)}"/>{escape(filter)}</li>'
    return ""


if __name__ == "__main__":
    app.run(debug=True)
