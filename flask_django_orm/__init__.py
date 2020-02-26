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
            self.init_app()

    def init_app(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
        django.setup()
