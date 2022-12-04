import docker
from utils.docker import Docker
# TODO:replace print with log


class DockerRunner:
    def __init__(self, docker_object: Docker = None) -> None:
        self.docker_object = docker_object

    def run(self):
        client = docker.from_env()
        image, command = self.docker_object.get_docker_command_for_run()
        container = client.containers.run(
            image,
            command,
            environment=self.docker_object.get_envs(),
            name=self.docker_object.get_container_name(),
            detach=True)
        print('run container', container.id)
