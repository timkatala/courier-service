# Rest Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Project
from apps.shared.tests import ViewSetTestCase
from apps.order.models import Order
from apps.shared import messages


class CourierTest(APITestCase, ViewSetTestCase):
    fixtures = [
        'courier.yaml',
        'order.yaml'
    ]

    url = 'courier-%s'

    def setUp(self):
        pass

    def test_create(self):
        data = {
            "data": [
                {
                    "courier_id": 288,
                    "courier_type": "foot",
                    "regions": [
                        1
                    ],
                    "working_hours": [
                        "18:00-19:00", "20:00-21:00"
                    ]
                },
                {
                    "courier_id": 298,
                    "courier_type": "foot",
                    "regions": [
                        1
                    ],
                    "working_hours": [
                        "18:00-19:00", "20:00-21:00"
                    ]
                }
            ]
        }
        response = self._create(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data, {
                'couriers': [
                    {'id': 288},
                    {'id': 298}
                ]}
        )

    def test_create_fail_required(self):
        response = self._create({'data': [{"courier_id": 1}]})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {
                "validation_error": {
                    "couriers": [
                        {
                            "id": "1",
                            "working_hours": [messages.INVALID_REQUIRED],
                            "courier_type": [messages.INVALID_REQUIRED],
                            "regions": [messages.INVALID_REQUIRED]
                        }
                    ]
                }
            })

    def test_assign(self):
        response = self._create({"courier_id": 1}, kwargs={'method': 'assign'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, {
                'orders': [{'id': 3}, {'id': 4}, {'id': 5}],
                'assign_time': response.data['assign_time']
            })

        # Checking idempotent
        response = self._create({"courier_id": 1}, kwargs={'method': 'assign'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, {
                'orders': [{'id': 3}, {'id': 4}, {'id': 5}],
                'assign_time': response.data['assign_time']
            })

    def test_assign_empty(self):
        Order.objects.all().update(is_completed=True)
        response = self._create({"courier_id": 1},
                                kwargs={'method': 'assign'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, {
                'orders': [],
            })