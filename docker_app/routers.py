from rest_framework import generics, mixins, status, viewsets
from rest_framework.views import APIView
from docker_app.models import ContainerizedApp
from docker_app.serializers import CreateContainerizedAppSerializer, RetriveContainerizedAppSerializer, RetriveContainerInfo
from rest_framework.response import Response
from utils.docker import Docker
from utils.docker_runner import DockerRunner


class DockerAppStatusViewset(viewsets.ViewSet):
    def retrieve(self, reques, pk=None):
        pass

    def list(self, request):
        check_all_container: str = request.query_params.get(
            'all', 'True').lower()
        all_container: bool = True if check_all_container == 'true' else False
        serializer = RetriveContainerInfo(
            data=DockerRunner.get_all_container_info(all=all_container), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        input_serializer = CreateContainerizedAppSerializer(
            data=request.data)
        input_serializer.is_valid(raise_exception=True)

        d = Docker(**input_serializer.data)
        dr = DockerRunner(docker_object=d)
        dr.run()

        response_serializer = RetriveContainerizedAppSerializer(
            data={**input_serializer.data, 'envs': d.get_str_envs()})
        response_serializer.is_valid(raise_exception=True)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)
