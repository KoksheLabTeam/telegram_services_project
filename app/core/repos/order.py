from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from app.core.models.order import Order

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

    def get_by_id(self, order_id: int) -> Order:
        query = select(Order).where(Order.id == order_id)
        result = self.session.execute(query)
        order = result.scalar_one_or_none()
        if not order:
            raise OrderNotFoundException(f"Order with id '{order_id}' not found")
        return order

    def update(self, order_id: int, update_data: dict) -> Order:
        query = (
            update(Order)
            .where(Order.id == order_id)
            .values(**update_data)
            .returning(Order)
        )
        result = self.session.execute(query)
        self.session.commit()
        return result.scalar_one()

    def delete(self, order_id: int) -> None:
        query = delete(Order).where(Order.id == order_id)
        self.session.execute(query)
        self.session.commit()

    def select(self, **filters):
        query = select(Order).filter_by(**filters)
        result = self.session.execute(query)
        return result.scalars().all()