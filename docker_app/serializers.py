from rest_framework import serializers
from docker_app.models import ContainerizedApp
from utils.randome_name import generate_randome_app_name


class CreateContainerizedAppSerializer(serializers.Serializer):
    commands = serializers.ListField(child=serializers.CharField())
    envs = serializers.ListField(child=serializers.CharField())
    container_name = serializers.CharField(
        allow_blank=True, default=generate_randome_app_name())
    image_name = serializers.CharField()

    class Meta:
        fields = '__all__'


class RetriveContainerizedAppSerializer(serializers.ModelSerializer):
    # for better perfomance we can define every field with type
    class Meta:
        model = ContainerizedApp
        fields = '__all__'
