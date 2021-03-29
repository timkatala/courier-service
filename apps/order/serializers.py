# Django Rest Framework
from rest_framework import serializers

# Project
from .models import Order
from .swagger_schemas import schema


class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField()
    delivery_hours = serializers.ListField(child=serializers.ListField(
        child=serializers.TimeField(),
        min_length=2,
        error_messages={'min_length': 'Ensure this field has 2 timestamps'}
    ), write_only=True)

    class Meta:
        swagger_schema_fields = schema
        model = Order
        fields = [
            'order_id',
            'delivery_hours',
            'weight',
            'region'
        ]
        extra_kwargs = {
            "region": {"write_only": True},
            "weight": {"write_only": True}
        }

    def to_internal_value(self, data):
        if delivery_hours := data.pop('delivery_hours', None):
            data['delivery_hours'] = [i.split('-')
                                      for i in delivery_hours if i]
        return super().to_internal_value(data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = data.pop('order_id')
        return data


class OrderListSerializer(serializers.Serializer):
    data = OrderSerializer(many=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['orders'] = data.pop('data')
        return data

    @property
    def errors(self):
        errors = self._errors
        if data := errors.pop('data', None):
            errors['orders'] = [{
                'id': self.initial_data['data'][index].get('order_id'),
                **data[index]
            } for index, _ in enumerate(data) if _]

        if errors:
            return {
                'validation_error': errors
            }
        return errors

    def save(self):
        items = [Order(**item) for item in self.validated_data.get('data')]
        return Order.objects.bulk_create(items)
