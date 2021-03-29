# Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Project
from apps.shared.tests import ViewSetTestCase
from apps.shared import messages


class OrderTest(APITestCase, ViewSetTestCase):
    fixtures = [

    ]

    url = 'order-%s'

    def setUp(self):
        pass

    def test_create(self):
        data = {
            "data": [
                {
                    "order_id": 288,
                    "weight": 4.5,
                    "region": 1,
                    "delivery_hours": [
                        "18:00-19:00", "20:00-21:00"
                    ]
                },
                {
                    "order_id": 298,
                    "weight": 4.5,
                    "region": 1,
                    "delivery_hours": [
                        "18:00-19:00", "20:00-21:00"
                    ]
                }
            ]
        }
        response = self._create(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data, {
                'orders': [
                    {'id': 288},
                    {'id': 298}
                ]}
        )

    def test_create_fail_required(self):
        response = self._create({'data': [{"order_id": 1}]})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {
                "validation_error": {
                    "orders": [
                        {
                            "id": "1",
                            "delivery_hours": [messages.INVALID_REQUIRED],
                            "region": [messages.INVALID_REQUIRED],
                            "weight": [messages.INVALID_REQUIRED]
                        }
                    ]
                }
            })
