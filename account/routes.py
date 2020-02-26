from django.db.utils import IntegrityError
from flask import Blueprint, render_template, redirect, url_for, flash, session
from .forms import RegisterForm, LoginForm
from .models import User

bp = Blueprint("account", __name__)

@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.password = form.password1.data
        try:
            user.save()
        except IntegrityError:
            flash("Username / Email already registerd!", "danger")
            return render_template("register.html", form=form)
        return redirect(url_for("index"))
    return render_template("register.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session.clear()
        user = User.objects.filter(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            session["user_id"] = user.id
            flash("Logged In", "success")
        else:
            flash("Invalid username and/or password", "danger")
        return redirect(url_for("index"))
    return render_template("login.html", form=form)

@bp.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect(url_for("index"))
