import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))



@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "ingredients_list": request.form.get("ingredients_list"),
            "recipe_description": request.form.get("recipe_description"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))
    
    vegies = mongo.db.vegies.find().sort("vegie_name", 1)
    return render_template("add_recipe.html", vegies=vegies)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "ingredients_list": request.form.get("ingredients_list"),
            "recipe_description": request.form.get("recipe_description"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": submit})
        flash("Recipe Successfully Updated")
        
    
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    vegies = mongo.db.vegies.find().sort("vegie_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, vegies=vegies)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_vegies")
def get_vegies():
    vegies = list(mongo.db.vegies.find().sort("vegie_name", 1))
    return render_template("manage_vegies.html", vegies=vegies)


@app.route("/add_vegie", methods=["GET", "POST"])
def add_vegie():
    if request.method == "POST":
        vegie = {
            "vegie_name": request.form.get("vegie_name")
        }
        mongo.db.vegies.insert_one(vegie)
        flash("New Veg Added")
        return redirect(url_for("get_vegies"))

    return render_template("add_vegies.html")


@app.route("/edit_vegie/<vegie_id>", methods=["GET", "POST"])
def edit_vegie(vegie_id):
    if request.method == "POST":
        submit = {
            "vegie_name": request.form.get("vegie_name")
        }
        mongo.db.vegies.update_many({"_id": ObjectId(vegie_id)}, {"$set": submit})
        flash("Vegie Successfully Updated")
        return redirect(url_for("get_vegies"))

    vegie = mongo.db.vegies.find_one({"_id": ObjectId(vegie_id)})
    return render_template("edit_vegies.html", vegie=vegie)


@app.route("/delete_vegie/<vegie_id>")
def delete_vegie(vegie_id):
    mongo.db.vegies.delete_one({"_id": ObjectId(vegie_id)})
    flash("Vegie Successfully Deleted")
    return redirect(url_for("get_vegies"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)