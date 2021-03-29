# Django Rest Framework
from rest_framework import serializers

# Project
from .models import Courier
from .swagger_schemas import schema


class CourierSerializer(serializers.ModelSerializer):
    courier_id = serializers.IntegerField()
    working_hours = serializers.ListField(child=serializers.ListField(
        child=serializers.TimeField(),
        min_length=2,
        error_messages={'min_length': 'Ensure this field has 2 timestamps'}
    ), write_only=True)

    class Meta:
        swagger_schema_fields = schema
        model = Courier
        fields = [
            'courier_id',
            'working_hours',
            'courier_type',
            'regions'
        ]
        extra_kwargs = {
            "regions": {"write_only": True},
            "courier_type": {"write_only": True}
        }

    def to_internal_value(self, data):
        if working_hours := data.pop('working_hours', None):
            data['working_hours'] = [i.split('-') for i in working_hours if i]
        return super().to_internal_value(data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = data.pop('courier_id')
        return data


class CourierListSerializer(serializers.Serializer):
    data = CourierSerializer(many=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['couriers'] = data.pop('data')
        return data

    @property
    def errors(self):
        errors = self._errors
        if data := errors.pop('data', None):
            errors['couriers'] = [{
                'id': self.initial_data['data'][index].get('courier_id'),
                **data[index]
            } for index, _ in enumerate(data) if _]

        if errors:
            return {
                'validation_error': errors
            }
        return errors

    def save(self):
        items = [Courier(**item) for item in self.validated_data.get('data')]
        return Courier.objects.bulk_create(items)
