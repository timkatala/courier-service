from django.apps import AppConfig
from django.contrib.postgres.fields import ArrayField

from .lookups import HasIntersection

class MyAppConfig(AppConfig):
    name = 'couriers'

    def ready(self):

        ArrayField.register_lookup(HasIntersection)