from pydantic import BaseModel, Field

class QuestionCreate(BaseModel):
    """Schema for creating a new question with validation."""
    text: str = Field(..., min_length=12, description="The content of the question")

class QuestionResponse(BaseModel):
    """Schema for returning question details."""
    id: int
    text: str

class MessageResponse(BaseModel):
    """Simple schema for consistent API feedback messages."""
    message: str