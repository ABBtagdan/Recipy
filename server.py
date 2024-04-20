from flask import Flask, request, render_template, session, url_for, redirect
from markupsafe import escape
from datetime import datetime
from flask_session import Session  # noqa: syntax
from werkzeug.utils import secure_filename
from flask import send_from_directory
import os
import tools
import uuid

app = Flask(__name__)

app.config.from_pyfile("config.py")

Session(app)

IMAGE_FOLDER = "/images"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_user/", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        form = request.form
        file = request.files["image"]
        file_name = IMAGE_FOLDER + "/" + secure_filename(uuid.uuid4().hex)
        file.save(os.path.abspath("." + file_name))
        new_user = (
            form["username"],
            form["real_name"],
            file_name,
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
        user_password = tools.execute_fetchone(
            tools.get_user_query(request.form["username"])
        )[4]
        if request.form["password"] == user_password:
            session["logged_in_user"] = request.form["username"]
            return redirect(url_for("index"))
    return """<form method='post'>
        <input type='text' name = 'username'>Username</input>
        <input type = 'password' name = 'password'>Password</input>
        <button type = 'submit'>Log in</button>
    </form>
    """


@app.route("/images/<filename>")
def images(filename):
    return send_from_directory(
        os.path.abspath("." + IMAGE_FOLDER),
        filename,
        as_attachment=False,
        mimetype="image",
    )


@app.route("/create_recipe/", methods=["GET", "POST"])
def create_recipe():
    if session["logged_in_user"] is None:
        return redirect(url_for("log_in"))
    if request.method == "POST":
        form = request.form
        file = request.files["image"]
        file_name = IMAGE_FOLDER + "/" + secure_filename(uuid.uuid4().hex)
        file.save(os.path.abspath("." + file_name))
        uuid_str = str(uuid.uuid4())
        new_recipe = (
            form["title"],
            session["logged_in_user"],
            form["time"],
            form["ingredients"],
            form["amounts"],
            form["units"],
            file_name,
            form["tags"],
            form["recipe"],
            uuid_str,
            datetime.now(),
        )
        if tools.add_recipe(new_recipe):
            return redirect("/")
    return render_template("new_recipe_form.html")


@app.route("/recipes/<id>")
@app.route("/recipes/", methods=["GET"])
def get_recipies(id=None):
    if id is None:
        user = session["logged_in_user"]
        if user is None:
            return ""
        request.args.getlist("filter")
        recipes = tools.execute_fetchall(tools.get_user_recipes_query(user))
        return render_template("recipes.html", recipes=recipes)
    else:
        recipe = tools.execute_fetchone(tools.get_recipe_by_id_query(id))
        return str(recipe)


@app.route("/filter_card/", methods=["GET", "DELETE"])
def filter_card():
    if request.method == "GET":
        filter: str = request.args["filter"]
        filter = filter.strip()
        return f'<li hx-trigger="click" hx-target="this" hx-delete="/filter_card" hx-swap="outerHTML"><input type="hidden" name="filter" value="{escape(filter)}"/>{escape(filter)}</li>'
    return ""


@app.route("/ingredient_card/", methods=["GET", "DELETE"])
def ingredient_card():
    if request.method == "GET":
        ingredient = request.args["ingredient"].strip()
        amount = request.args["amount"].strip()
        unit = request.args["unit"].strip()
        return f"""<li hx-trigger='click' hx-target="this" hx-delete="/ingredient_card" hx-swap="outerHTML">
            <input type="hidden" name = "amounts" value="{escape(amount)}">
            <input type="hidden" name = "ingredients" value="{escape(ingredient)}">
            <input type="hidden" name = "units" value="{escape(unit)}">
            <p>{escape(ingredient)} - {escape(amount)} {escape(unit)}</p>
        </li>    
        """


@app.route("/tag_card", methods=["GET", "DELETE"])
def tag_card():
    if request.method == "GET":
        tag = request.args["tag"].strip()
        return f'<li hx-trigger="click" hx-target="this" hx-delete="/tag_card" hx-swap="outerHTML"><input type="hidden" name="tags" value="{escape(tag)}"/>{escape(tag)}</li>'
    return ""


if __name__ == "__main__":
    app.run(debug=True)
