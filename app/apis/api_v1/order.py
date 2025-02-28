from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.schemas.order import OrderCreate, OrderUpdate, OrderResponse
from app.core.services.order import OrderService
from app.core.repos.order import OrderRepo
from app.core.database.helper import get_session

router = APIRouter()

@router.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_session)):
    order_service = OrderService(OrderRepo(db))
    return order_service.create(order)

@router.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_session)):
    order_service = OrderService(OrderRepo(db))
    order = order_service.get_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/orders/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_session)):
    order_service = OrderService(OrderRepo(db))
    return order_service.update(order_id, order)

@router.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_session)):
    order_service = OrderService(OrderRepo(db))
    order_service.delete(order_id)
    return {"detail": "Order deleted successfully"}
