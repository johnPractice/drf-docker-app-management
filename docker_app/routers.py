from rest_framework import generics, mixins, status, viewsets
from rest_framework.views import APIView
from docker_app.models import ContainerizedApp
from docker_app.serializers import CreateContainerizedAppSerializer, RetriveContainerizedAppSerializer,\
    RetriveContainerInfo, InputContainerizedAppSerializer
from rest_framework.response import Response
from utils.docker import Docker
from utils.docker_runner import DockerRunner


class DockerAppStatusViewset(viewsets.ViewSet):
    def retrieve(self, reques, pk=None):
        container_db_instance = ContainerizedApp.retrive_by_id(id=pk)
        retrive_container_serializer = RetriveContainerizedAppSerializer(
            instance=container_db_instance)
        return Response(data=retrive_container_serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        check_all_container: str = request.query_params.get(
            'all', 'True').lower()
        all_container: bool = True if check_all_container == 'true' else False
        serializer = RetriveContainerInfo(
            data=DockerRunner.get_all_container_info(all=all_container), many=True)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        input_serializer = InputContainerizedAppSerializer(
            data=request.data)
        input_serializer.is_valid(raise_exception=True)
        d = Docker(**input_serializer.data)
        dr = DockerRunner(docker_object=d)
        dr.run()
        save_container_serializer = CreateContainerizedAppSerializer(
            data={**input_serializer.data, 'envs': d.get_str_envs()})
        save_container_serializer.is_valid(raise_exception=True)
        container_db_instance = save_container_serializer.save()
        response_serializer = RetriveContainerizedAppSerializer(
            container_db_instance)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)
