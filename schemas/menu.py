from pydantic import BaseModel

class MenuSchema(BaseModel):
    id: int
    dish: str
    cuisine: str