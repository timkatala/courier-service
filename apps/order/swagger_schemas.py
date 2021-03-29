from drf_yasg import openapi


schema = swagger_schema_fields = {
    "type": openapi.TYPE_OBJECT,
    "title": "orders",
    "properties": {
        "order_id": openapi.Schema(
            title="Courier id",
            type=openapi.TYPE_INTEGER,
        ),
        "weight": openapi.Schema(
            title="Courier type",
            type=openapi.TYPE_INTEGER
        ),
        "region": openapi.Schema(
            title="Courier's regions",
            type=openapi.TYPE_INTEGER
        ),
        "delivery_hours": openapi.Schema(
            title="Courier type",
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(type=openapi.TYPE_STRING)
        )
    },
}
