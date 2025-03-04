from fastapi import FastAPI
from app.apis.api_v1.category import router as category_router
from app.apis.api_v1.city import router as city_router
from app.apis.api_v1.offer import router as offer_router
from app.apis.api_v1.order import router as order_router
from app.apis.api_v1.user import router as user_router
from app.apis.api_v1.review import router as review_router
from app.core.database.helper import engine  # Импортируем engine
from app.core.models.base import Base  # Импортируем Base для metadata
from app.core.models import category, user, city  # Импортируем модели
from app.core.models.association import user_categories  # Импортируем промежуточную таблицу, если она в association.py

# Создаём таблицы в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(category_router)
app.include_router(city_router)
app.include_router(offer_router)
app.include_router(order_router)
app.include_router(user_router)
app.include_router(review_router)