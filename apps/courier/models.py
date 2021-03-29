# Django
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Project
from apps.shared.models import BaseModel
from .lookups import HasIntersection


class Courier(BaseModel):
    FOOT = 'foot'
    BIKE = 'bike'
    CAR = 'car'

    COURIER_TYPES = (
        (FOOT, 10),
        (BIKE, 15),
        (CAR, 50)
    )

    courier_id = models.IntegerField(primary_key=True)
    courier_type = models.CharField(max_length=30, choices=COURIER_TYPES)
    regions = ArrayField(models.IntegerField())
    working_hours = ArrayField(ArrayField(models.TimeField(), size=2))

    @property
    def id(self):
        return self.courier_id


ArrayField.register_lookup(HasIntersection)
