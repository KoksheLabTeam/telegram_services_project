from app.core.config import settings  # Импортируем настройки
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Отладочная информация
print("Loading database configuration...")
print("DB_URL:", settings.DB_URL)
print("DB_ECHO:", settings.DB_ECHO)

if not settings.DB_URL:
    raise ValueError("DB_URL is not set. Please check your .env file.")

# Создание движка SQLAlchemy
engine = create_engine(
    url=settings.DB_URL,
    echo=settings.DB_ECHO,
)

# Фабрика сессий
SessionLocal = sessionmaker(bind=engine)

# Функция для получения сессии
def get_session():
    with SessionLocal() as session:
        yield session