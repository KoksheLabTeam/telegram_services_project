from fastapi import HTTPException
from app.core.models.order import Order
from app.core.schemas.order import OrderCreate, OrderUpdate, OrderRead
from app.core.repos.order import OrderRepo, OrderCreateException, OrderNotFoundException

class OrderService:
    def __init__(self, repository: OrderRepo) -> None:
        self.repository = repository

    def create(self, data: OrderCreate) -> OrderRead:
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
            return OrderRead.from_orm(order)
        except OrderCreateException as e:
            raise HTTPException(status_code=500, detail=f"Error while creating order: {e}")

    def get_by_id(self, order_id: int) -> OrderRead:
        try:
            order = self.repository.get_by_id(order_id)
            if not order:
                raise HTTPException(status_code=404, detail="Order not found")
            return OrderRead.from_orm(order)
        except OrderNotFoundException:
            raise HTTPException(status_code=404, detail="Order not found")

    def update(self, order_id: int, update_data: OrderUpdate) -> OrderRead:
        try:
            order = self.repository.update(order_id, update_data.dict(exclude_unset=True))
            return OrderRead.from_orm(order)
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

    def select(self, **filters):
        orders = self.repository.select(**filters)
        if not orders:
            raise HTTPException(status_code=404, detail="No orders found")
        return [OrderRead.from_orm(order) for order in orders]