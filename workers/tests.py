from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from workers.models import Worker


class WorkerTestCase(TestCase):
    def setUp(self):
        # Create a worker for testing
        self.worker = Worker.objects.create(
            full_name="Коровин",
            brigade_number=1,
            salary=15000,
            specialization="Чистовая отделка",
        )

    def test_worker_retrieve(self):
        url = reverse("workers:worker_retrieve", args=(self.worker.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["full_name"], self.worker.full_name)

    def test_BrigadeWorkerList(self):
        url = reverse("workers:brigade_workers_list", args=(self.worker.brigade_number,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
