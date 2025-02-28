from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.schemas.order import OrderResponse
from app.core.models.order import Order, OrderStatus


class OrderCreateException(Exception):
    """Raise exception when there is an error during order creation."""


class OrderNotFoundException(Exception):
    """Raise exception when no order is found."""


class OrderRepo:
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, instance: Order) -> Order:
        self.session.add(instance)
        try:
            self.session.commit()
            self.session.refresh(instance)
            return instance
        except Exception as e:
            self.session.rollback()
            raise OrderCreateException(str(e))

    def get_by_id(self, order_id: int) -> OrderResponse:
        query = select(Order).where(Order.id == order_id)
        try:
            result = self.session.execute(query)
            order = result.scalar_one_or_none()
            if order is None:
                raise OrderNotFoundException(f"Order with id '{order_id}' not found")
            return order
        except Exception as e:
            self.session.rollback()
            raise OrderNotFoundException(str(e))