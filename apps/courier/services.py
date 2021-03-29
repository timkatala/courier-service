# Project
from .models import Courier
from apps.order.models import Order
from apps.courier.models import Courier
from apps.order.models import Order
from django.contrib.postgres.fields import ArrayField
from django.db.models import Value, TimeField


def is_busy(courier: Courier) -> bool:
    return courier.orders.filter(is_completed=False).exists()


def get_assignment_order_ids(courier: Courier):
    possible_orders = Order.objects.filter(
        is_completed=False,
        delivery_hours__has_intersection=Value(
            courier.working_hours,
            output_field=ArrayField(ArrayField(TimeField()))),
        region__in=courier.regions,
    ).values('order_id', 'weight').order_by('weight')

    target = dict(Courier.COURIER_TYPES)[courier.courier_type]
    current_weight = 0
    order_ids = []

    for order in possible_orders:
        current_weight += order['weight']
        if current_weight>target:
            break
        order_ids.append(order['order_id'])

    return order_ids