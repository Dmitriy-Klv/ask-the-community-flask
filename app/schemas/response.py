from pydantic import BaseModel, Field

class ResponseCreate(BaseModel):
    """Schema for submitting a vote on a question."""
    question_id: int = Field(..., description="The ID of the question being answered")
    is_agree: bool = Field(..., description="User's agreement or disagreement with the question")

class StatisticResponse(BaseModel):
    """Schema for aggregated response statistics."""
    question_id: int
    agree_count: int
    disagree_count: int