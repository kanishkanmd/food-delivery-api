from database import Base
from sqlalchemy import Column,Integer,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

class OrderModel(Base):

    ORDER_STATUSES=(
        ('PENDING','pending'),
        ('IN-TRANSIT','in-transit'),
        ('DELIVERED','delivered')

    )


    __tablename__='orders'
    id=Column(Integer,primary_key=True)
    quantity=Column(Integer,nullable=False)
    order_status=Column(ChoiceType(choices=ORDER_STATUSES),default="PENDING")
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship('User',back_populates='orders')

    def __repr__(self):
        return f"<Order {self.id}>"