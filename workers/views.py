from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from workers.models import Worker
from workers.serializer import WorkerSerializer


class WorkerListAPIView(ListAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class BrigadeWorkerListAPIView(ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def get_queryset(self):
        brigade_number = self.kwargs.get("brigade_number")
        if brigade_number is not None:
            return Worker.objects.filter(brigade_number=brigade_number)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class WorkerRetrieveAPIView(RetrieveAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
