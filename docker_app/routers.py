from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from docker_app.models import ContainerizedApp
from docker_app.serializers import CreateContainerizedAppSerializer, RetriveContainerizedAppSerializer
from rest_framework.response import Response
from utils.docker import Docker
from utils.docker_runner import DockerRunner


class DockerContainrizeAppRouter(APIView):
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        input_serializer = CreateContainerizedAppSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        d = Docker(**input_serializer.data)
        dr = DockerRunner(docker_object=d)
        dr.run()

        response_serializer = RetriveContainerizedAppSerializer(
            data={**input_serializer.data, 'envs': d.get_str_envs()})
        response_serializer.is_valid(raise_exception=True)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)
