from pydantic import BaseModel, Field
from typing import Optional
from .category import CategoryResponse

class QuestionCreate(BaseModel):
    """Schema for creating a new question with validation."""
    text: str = Field(..., min_length=12, description="The content of the question")
    category_id: int = Field(..., description="ID of the assigned category")

class QuestionResponse(BaseModel):
    """Schema for returning question details."""
    id: int
    text: str
    category: Optional[CategoryResponse] = None

    class Config:
        from_attributes = True

class MessageResponse(BaseModel):
    """Simple schema for consistent API feedback messages."""
    message: str