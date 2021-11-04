from pydantic import BaseModel


class SettingsSchema(BaseModel):
    authjwt_secret_key: str = (
        "36f1f38e4b283ae4f5b4fd331ab6360b4b6487a3e55d73fd4b4a1ce6dbf7a418"
    )
