from utils.randome_name import generate_randome_app_name


class Docker:
    def __init__(self, envs: list[str], commands: list[str], image_name: str, container_name: str = generate_randome_app_name()) -> None:
        self.__envs: dict[str, str] = self.__prepare_envs(envs)
        self.__commands: list[str] = commands
        self.__image: str = image_name
        self.__container_name: str = container_name

    def __prepare_envs(self, input_envs: list[str] = []) -> dict[str, str]:
        """_summary_
        Prepare -e input in docker

        Returns:
            dict[str, str]: return docker env as string
        """
        if len(input_envs) == 0:
            return ''
        envs: dict[str, str] = {}
        for e in input_envs:
            _key, _value = e.split(':')
            envs[_key] = _value
        return envs

    def __prepare_commans(self, input_command: list[str]) -> str:
        """_summary_

        Args:
            input_command (list[str]): _description_

        Returns:
            str: _description_
        """
        if len(input_command) == 0:
            return ''
        command: str = ''
        for c in input_command:
            command += f"{c} "
        return command

    def get_container_name(self) -> str:
        return self.__container_name

    def get_str_envs(self) -> str:
        """_summary_
        Return envs as single string
        Returns:
            str: string env
        """
        envs: str = ''
        for _key, _value in self.__envs.items():
            envs += f'-e {_key}={_value} '
        return envs

    def get_envs(self) -> dict[str, str]:
        """_summary_

        Returns:
            dict[str, str]: docker env as string 
        """
        return self.__envs

    def get_commands(self) -> list[str]:
        """_summary_

        Returns:
            list[str]: docker command
        """
        return self.__commands

    def get_docker_command_for_run(self) -> tuple[str, list[str]]:
        """_summary_
        Return input for 'run docker' command
        Returns:
            tuple[str, list[str]]: image and commands string
        """
        # TODO:how to add -e to run docker command
        return (self.__image, [*self.__commands])
