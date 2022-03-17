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
@app.route("/get_festivals")
def get_festivals():
    festivals = list(mongo.db.festivals.find())
    return render_template("festivals.html", festivals=festivals)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    festivals = list(mongo.db.festivals.find({"$text": {"$search": query}}))
    return render_template("festivals.html", festivals=festivals)


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
        return redirect(url_for("profile", username=session["user"]))

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


@app.route("/add_festival", methods=["GET", "POST"])
def add_festival():
    if request.method == "POST":
        festival = {
            "country_name": request.form.get("country_name"),
            "festival_name": request.form.get("festival_name"),
            "festival_dates": request.form.get("festival_dates"),
            "festival_djs": request.form.get("festival_djs"),
            "festival_location": request.form.get("festival_location"),
            "created_by": session["user"]
        }
        mongo.db.festivals.insert_one(festival)
        flash("Festival successfully added!")
        return redirect(url_for("get_festivals"))

    countries = mongo.db.countries.find().sort("country_name", 1)
    return render_template("add_festival.html", countries=countries)


@app.route("/edit_festival/<festival_id>", methods=["GET", "POST"])
def edit_festival(festival_id):
    if request.method == "POST":
        submit = {
            "country_name": request.form.get("country_name"),
            "festival_name": request.form.get("festival_name"),
            "festival_dates": request.form.get("festival_dates"),
            "festival_djs": request.form.get("festival_djs"),
            "festival_location": request.form.get("festival_location"),
            "created_by": session["user"]
        }
        mongo.db.festivals.update_one(
            {"_id": ObjectId(festival_id)}, {'$set': submit})
        flash("Festival successsfully updated!")

    festival = mongo.db.festivals.find_one({"_id": ObjectId(festival_id)})

    countries = mongo.db.countries.find().sort("country_name", 1)
    return render_template(
        "edit_festival.html", festival=festival, countries=countries)


@app.route("/delete_festival/<festival_id>")
def delete_festival(festival_id):
    mongo.db.festivals.delete_one({"_id": ObjectId(festival_id)})
    flash("Festival successfully deleted")
    return redirect(url_for("get_festivals"))


@app.route("/get_countries")
def get_countries():
    countries = list(mongo.db.countries.find().sort("country_name", 1))
    return render_template("countries.html", countries=countries)


@app.route("/add_country", methods=["GET", "POST"])
def add_country():
    if request.method == "POST":
        country = {
            "country_name": request.form.get("country_name")
        }
        mongo.db.countries.insert_one(country)
        flash("New country Added")
        return redirect(url_for("get_countries"))

    return render_template("add_country.html")


@app.route("/edit_country/<country_id>", methods=["GET", "POST"])
def edit_country(country_id):
    if request.method == "POST":
        submit = {
            "country_name": request.form.get("country_name")
        }
        mongo.db.countries.update_one(
            {"_id": ObjectId(country_id)}, {'$set': submit})
        flash("Country successfully updated")
        return redirect(url_for("get_countries"))

    country = mongo.db.countries.find_one({"_id": ObjectId(country_id)})
    return render_template("edit_country.html", country=country)


@app.route("/delete_country/<country_id>")
def delete_country(country_id):
    mongo.db.countries.delete_one({"_id": ObjectId(country_id)})
    flash("Country successfully deleted")
    return redirect(url_for("get_countries"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
