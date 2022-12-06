from typing import Optional
import docker
from docker_app.models import ContainerizedApp
from utils.docker import Docker
from docker.models.containers import Container
from utils.http_exception import DockerApiException, NotFoundItem
# TODO:replace print with log


class DockerRunner:
    def __init__(self, docker_object: Docker = None) -> None:
        self.docker_object = docker_object

    def run(self):
        """_summary_
        """
        client = docker.from_env()
        image, command = self.docker_object.get_docker_command_for_run()
        container = client.containers.run(
            image,
            command,
            environment=self.docker_object.get_envs(),
            name=self.docker_object.get_container_name(),
            detach=True)
        print('run container', container.id)

    @staticmethod
    def get_all_container_info(all: bool = True) -> list[dict[str, str]]:
        """_summary_

        Args:
            all (bool, optional): check for return all containers or not. Defaults to True.

        Returns:
            list[dict[str, str]]: list of containers data
        """
        result: list[dict[str, str]] = list()
        client = docker.from_env()
        all_containers = client.containers.list(all=all)
        for container in all_containers:
            result.append(
                {'name': container.name, 'status': container.status, 'container_id': container.id})
        return result

    @staticmethod
    def retive_container_with_name(container_name: str) -> Optional[Container]:
        """_summary_
        Get Container with name
        Args:
            container_name (str): name of container
        Raises:
            NotFoundItem: _description_
            DockerApiException: _description_

        Returns:
            Optional[Container]: Container Object

        """
        client = docker.from_env()
        try:
            container: Container = client.containers.get(container_name)
            return container

        except docker.errors.NotFound:
            raise NotFoundItem()
        except docker.errors.APIError:
            raise DockerApiException()

    @staticmethod
    def update_container(container_name: str) -> None:
        container = DockerRunner.retive_container_with_name(container_name)

    @staticmethod
    def remove_container(container_name: str) -> None:
        """_summary_
        Stop and Remove Container
        Args:
            container_name (str): name of container
        """
        container = DockerRunner.retive_container_with_name(container_name)
        container.stop()
        container.remove()
