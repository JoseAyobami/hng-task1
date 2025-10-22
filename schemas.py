from pydantic import BaseModel, Field
from typing import Optional, List, Dict


class StringCreate(BaseModel):
    value: str = Field(..., description="String to be analyzed")


class StringProperties(BaseModel):
    length: int
    is_palindrome: bool
    unique_characters: int
    word_count: int
    sha256_hash: str
    character_frequency_map: Dict[str, int]


class StringResponse(BaseModel):
    id: str
    value: str
    properties: StringProperties
    created_at: str


class QueryParams(BaseModel):
    is_palindrome: Optional[bool] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    word_count: Optional[int] = None
    contains_character: Optional[str] = None


class NaturalLanguageResult(BaseModel):
    data: List[StringResponse]
    count: int
    interpreted_query: Dict[str, object]





