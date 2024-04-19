from flask import Flask, request, render_template, session, url_for, redirect
from markupsafe import escape
import data_loader
import tools
import uuid
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_user/", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        form = request.form
        new_user = (
            form["username"],
            form["real_name"],
            form["image"],
            form["description"],
            form["password"],
        )
        if tools.add_user(new_user):
            session["logged_in_user"] = form["username"]
            return redirect(url_for("index"))
    return render_template("new_user_form.html")


@app.route("/log_in/", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        user_password = tools.get_user(request.form["username"])[4]
        if request.form["password"] == user_password:
            session["logged_in_user"] = request.form["username"]
            return redirect(url_for("index"))
    return """<form method='post'>
        <input type='text' name = 'username'>Username</input>
        <input type = 'password' name = 'password'>Password</input>
        <button type = 'submit'>Log in</button>
    </form>
    """


@app.route("/create_recipe/", methods=["GET", "POST"])
def create_recipe():
    if request.method == "GET":
        return render_template("new_recipe_form.html")
    elif request.method == "POST":
        form = request.form
        new_recipe = (
            form["title"],
            form["owner"],
            form["time"],
            form["ingredients"],
            form["amount"],
            form["unit"],
            form["image"],
            form["tags"],
            form["description"],
            str(uuid.uuid4()),
            datetime.now(),
        )
        if tools.add_recipe(new_recipe):
            return "<p>Succesfully added recipe</p><a href = '/'>Return to home</a>"
        return (
            "<p>Couldn't create recipe.</p> <a href = '/create_user/'>Try again?</a> "
        )


@app.route("/recipes/", methods=["GET"])
def get_recipies():
    x = data_loader.load("./recipes/" + request.args["user"] + ".json")
    filter = request.args.getlist("filter")
    x = tools.filter(x, filter)
    return render_template("recipes.html", recipes=x)


@app.route("/filter_card/", methods=["GET", "DELETE"])
def filter_card():
    if request.method == "GET":
        filter: str = request.args["filter"]
        filter = filter.strip()
        return f'<li hx-trigger="click" hx-target="this" hx-delete="/filter_card" hx-swap="outerHTML"><input type="hidden" name="filter" value="{escape(filter)}"/>{escape(filter)}</li>'
    return ""


if __name__ == "__main__":
    app.run(debug=True)
