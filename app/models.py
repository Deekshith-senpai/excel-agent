from pydantic import BaseModel
from typing import List, Optional


class ParsedCell(BaseModel):
    row: int
    col: int
    param_name: Optional[str]
    asset_name: Optional[str]
    raw_value: Optional[str]
    parsed_value: Optional[float]
    confidence: str


class ParseResponse(BaseModel):
    status: str
    header_row: int
    parsed_data: List[ParsedCell]
    unmapped_columns: list
    warnings: list