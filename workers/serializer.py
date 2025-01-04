from rest_framework.serializers import ModelSerializer, SerializerMethodField
from workers.models import Worker


class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"
        read_only_fields = ("id",)
