from pydantic import BaseModel, Field
from datetime import datetime, timezone

class ErrorDetail(BaseModel):
    type: str
    message: str
    timestamp: str

class ErrorResponse(BaseModel):
    detail: list[ErrorDetail]