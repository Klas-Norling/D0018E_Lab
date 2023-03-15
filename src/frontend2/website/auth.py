from flask import Blueprint, render_template, redirect, url_for, request


auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/sign-up")
def sign_up():
    return render_template("signup.html")

@auth.route("/chair",methods=['GET','POST'])
def post():
    name = request.comment.get('Name')
    object = request.comment.get('Object')
    rating = request.comment.get('Rating')
    comment = request.comment.get('comment')
    return render_template("chair.html")


@auth.route("/logout")
def logout():
    return redirect(url_for("views.home"))