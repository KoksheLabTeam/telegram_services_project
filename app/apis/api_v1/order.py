from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.schemas.order import OrderCreate, OrderUpdate, OrderRead
from app.core.services.order import OrderService
from app.core.repos.order import OrderRepo
from app.core.database.helper import get_session

router = APIRouter(prefix="/orders", tags=["orders"])

def parse_filters(customer_id: int = Query(None), status: str = Query(None)) -> dict:
    filters = {}
    if customer_id:
        filters["customer_id"] = customer_id
    if status:
        filters["status"] = status
    return filters

@router.post("/", response_model=OrderRead)
def create_order(order: OrderCreate, db: Session = Depends(get_session)):
    order_service = OrderService(OrderRepo(db))
    return order_service.create(order)

@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: int, db: Session = Depends(get_session)):
    order_service = OrderService(OrderRepo(db))
    return order_service.get_by_id(order_id)

@router.put("/{order_id}", response_model=OrderRead)
def update_order(order_id: int, order: OrderUpdate, db: Session = Depends(get_session)):
    order_service = OrderService(OrderRepo(db))
    return order_service.update(order_id, order)

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_session)):
    order_service = OrderService(OrderRepo(db))
    order_service.delete(order_id)
    return {"detail": "Order deleted successfully"}

@router.get("/select/", response_model=list[OrderRead])
def select_orders(filters: dict = Depends(parse_filters), db: Session = Depends(get_session)):
    order_service = OrderService(OrderRepo(db))
    return order_service.select(**filters)