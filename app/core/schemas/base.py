from pydantic import BaseModel, ConfigDict

class BaseSchema(BaseModel):
    """Базовая схема для всех моделей Pydantic."""
    model_config = ConfigDict(from_attributes=True)