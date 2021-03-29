# Django
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Project
from apps.shared.models import BaseModel


class Order(BaseModel):
    FOOT = 'foot'
    BIKE = 'bike'
    CAR = 'car'

    COURIER_TYPES = (
        (FOOT, 'Foot'),
        (BIKE, 'Bike'),
        (CAR, 'Car')
    )

    order_id = models.IntegerField(primary_key=True)
    courier = models.ForeignKey(
        'courier.Courier', on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='orders'
    )
    is_completed = models.BooleanField(default=False)
    weight = models.FloatField()
    region = models.IntegerField()
    delivery_hours = ArrayField(ArrayField(models.TimeField(), size=2))
    assign_time = models.DateTimeField(null=True, blank=True)
