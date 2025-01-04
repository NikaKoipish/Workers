from django.urls import path

from workers.apps import WorkersConfig
from workers.views import (
    WorkerListAPIView,
    WorkerRetrieveAPIView,
    BrigadeWorkerListAPIView,
)

app_name = WorkersConfig.name

urlpatterns = [
    path("", WorkerListAPIView.as_view(), name="worker_list"),
    path("worker/<int:pk>/", WorkerRetrieveAPIView.as_view(), name="worker_retrieve"),
    path(
        "brigade/<int:brigade_number>/workerslist/",
        BrigadeWorkerListAPIView.as_view(),
        name="brigade_workers_list",
    ),
]
