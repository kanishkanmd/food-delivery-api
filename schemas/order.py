from pydantic import BaseModel
from typing import Optional

class OrderSchema(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    user_id:Optional[int]


    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "quantity":2,
            }
        }

class OrderStatusSchema(BaseModel):
    order_status:Optional[str]="PENDING"

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }