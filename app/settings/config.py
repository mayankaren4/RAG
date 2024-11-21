from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configuration settings for the application.

    Attributes:
        app_name (str): The name of the application.
        debug (bool): Flag indicating whether debug mode is enabled or not. Defaults to False.
        app_host (str): The host address for the application. Defaults to "0.0.0.0".
        app_port (int): The port number for the application.
        app_base_path (str): The base path for the application. Defaults to "/".

    Config:
        env_file (str): The path to the environment file.
    """

    app_name: str
    debug: bool = False
    app_host: str
    app_port: int
    app_base_path: str

    class Config:
        env_file = ".env"
