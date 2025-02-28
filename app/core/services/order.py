from app.core.models.order import Order
from app.core.schemas.order import OrderCreate, OrderUpdate
from app.core.repos.order import OrderRepo, OrderCreateException, OrderNotFoundException
from fastapi import HTTPException


class OrderService:
    def __init__(self, repository: OrderRepo) -> None:
        self.repository = repository

    def create(self, data: OrderCreate) -> Order:
        instance = Order(
            customer_id=data.customer_id,
            executor_id=data.executor_id,
            city_id=data.city_id,
            category_id=data.category_id,
            description=data.description,
            price=data.price,
            status=data.status,
        )

        try:
            order = self.repository.create(instance)
            return order
        except OrderCreateException as e:
            raise HTTPException(status_code=500, detail=f"Error while creating order: {e}")

    def get_by_id(self, order_id: int) -> Order:
        order = self.repository.get_by_id(order_id)
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order

    def update(self, order_id: int, update_data: OrderUpdate) -> Order:
        try:
            return self.repository.update(order_id, update_data)
        except OrderNotFoundException:
            raise HTTPException(status_code=404, detail="Order not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while updating order: {e}")

    def delete(self, order_id: int) -> None:
        try:
            self.repository.delete(order_id)
        except OrderNotFoundException:
            raise HTTPException(status_code=404, detail="Order not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error while deleting order: {e}")
