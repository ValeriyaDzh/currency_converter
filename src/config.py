from pydantic import SecretStr

from pydantic_settings import BaseSettings, SettingsConfigDict


class CurrecyAPISettings(BaseSettings):

    KEY: SecretStr

    model_config = SettingsConfigDict(env_prefix="API_", extra="ignore")

    @property
    def URL(self):
        return SecretStr(
            f"https://v6.exchangerate-api.com/v6/{self.KEY.get_secret_value()}/latest/"
        )


class Settings(BaseSettings):
    api: CurrecyAPISettings = CurrecyAPISettings()


settings = Settings()
