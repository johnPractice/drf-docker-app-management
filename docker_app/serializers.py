from rest_framework import serializers
from docker_app.models import ContainerizedApp
from utils.randome_name import generate_randome_app_name
from utils.base_serializer import BaseModelSerializer


class RetriveContainerInfo(serializers.Serializer):
    id = serializers.CharField()
    status = serializers.CharField()
    name = serializers.CharField()


class CreateContainerizedAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerizedApp
        fields = '__all__'


class InputContainerizedAppSerializer(serializers.Serializer):
    commands = serializers.ListField(child=serializers.CharField())
    envs = serializers.ListField(child=serializers.CharField())
    container_name = serializers.CharField(
        allow_blank=True, default=generate_randome_app_name())
    image_name = serializers.CharField()

    class Meta:
        fields = '__all__'


class RetriveContainerizedAppSerializer(BaseModelSerializer):
    # for better perfomance we can define every field with type
    def set_model(self, model=ContainerizedApp):
        return super().set_model(model)
