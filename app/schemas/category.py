from pydantic import BaseModel, Field
from typing import Optional

class CategoryBase(BaseModel):
    """Basic schema with common fields."""
    name: str = Field(..., min_length=2, max_length=15, description="Category name")

class CategoryCreate(CategoryBase):
    """Schema to create (no ID yet)."""
    pass

class CategoryResponse(CategoryBase):
    """Schema for API responses (includes ID)."""
    id: int

    class Config:
        from_attributes = True