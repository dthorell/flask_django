from flask import Flask, render_template
from flask_django_orm import DjangoORM
from flask_debugtoolbar import DebugToolbarExtension


db = DjangoORM()
toolbar = DebugToolbarExtension()


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config.from_pyfile("../settings.py")

    db.init_app(app)
    toolbar.init_app(app)

    from account.routes import bp as account
    app.register_blueprint(account, url_prefix="/account")

    @app.route("/")
    def index():
        return render_template("layout.html")

    return app
