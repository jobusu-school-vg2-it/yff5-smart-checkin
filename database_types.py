from pydantic import BaseModel

class Visit(BaseModel):
    id: int
    name: str
    purpose: str
    in_time: str
    out_time: str | None = None