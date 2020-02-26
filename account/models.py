from django.db import models
from werkzeug.security import generate_password_hash, check_password_hash



class User(models.Model):
    email = models.CharField(max_length=150, unique=True, null=True)
    password_hash = models.CharField(max_length=128, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password, method="pbkdf2:sha512:8000")

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return self.email



"""
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(254), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(150), nullable=False, default="images/anonymous.png")

"""