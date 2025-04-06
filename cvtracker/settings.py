from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )
    API_VERSION: str
    ENVIROMENT: str


def get_settings():
    """
    Função para obter as configurações do projeto.
    Retorna uma instância da classe Settings.
    """
    return Settings()  # type: ignore
