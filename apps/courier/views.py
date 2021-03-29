# Django
from django.db.models import F
from django.utils import timezone, dateformat

# Django Rest Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.mixins import (
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin
)

# Project
from .models import Courier
from .serializers import CourierSerializer, CourierListSerializer
from .services import get_assignment_order_ids, is_busy
from apps.order.models import Order


class CourierViewSet(CreateModelMixin,
                     UpdateModelMixin,
                     RetrieveModelMixin,
                     GenericViewSet):
    queryset = Courier.objects.all()
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action == 'create':
            return CourierListSerializer

        return CourierSerializer

    @action(['POST'], detail=False)
    def assign(self, request, pk=None, *args, **kwargs):
        courier = Courier.objects.get(
            courier_id=request.data.get('courier_id'))
        if is_busy(courier):
            orders = courier.orders.filter(is_completed=False).values(
                'assign_time', 'order_id')
            print(orders)
            return Response(status=status.HTTP_200_OK, data={
                'orders': [{'id':i['order_id']}
                           for i in orders if i.get('order_id')],
                'assign_time': orders[0]['assign_time'].isoformat()
            })

        data = {}
        ids = get_assignment_order_ids(courier)
        data['orders'] = [{'id': i} for i in ids]
        if any(ids):
            data['assign_time'] = timezone.now().isoformat()


        Order.objects.filter(order_id__in=ids).update(
            courier=courier,
            assign_time = timezone.now()
        )

        return Response(status=status.HTTP_200_OK, data=data)
