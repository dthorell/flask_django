"""
    flask_django_orm
    ~~~~~~~~~~~~~~~~

    :copyright: (c) 2020 by Daniel Thorell.
    :license: MIT, see LICENSE for more details.
"""

__version__ = "0.0"

import os
import django

class DjangoORM(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        if "djangoorm" not in app.extensions:
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
            django.setup()
            app.extensions["djangoorm"] = self
        self.app = app
