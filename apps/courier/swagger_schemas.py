from drf_yasg import openapi
from .models import Courier

schema = swagger_schema_fields = {
    "type": openapi.TYPE_OBJECT,
    "title": "couriers",
    "properties": {
        "courier_id": openapi.Schema(
            title="Courier id",
            type=openapi.TYPE_INTEGER,
        ),
        "courier_type": openapi.Schema(
            title="Courier type",
            type=openapi.TYPE_STRING,
            enum=[Courier.FOOT, Courier.BIKE, Courier.CAR]
        ),
        "regions": openapi.Schema(
            title="Courier's regions",
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(type=openapi.TYPE_INTEGER)
        ),
        "working_hours": openapi.Schema(
            title="Courier type",
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(type=openapi.TYPE_STRING)
        )
    },
}
