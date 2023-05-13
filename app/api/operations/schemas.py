"""
Author Sanatjon Burkhanov
github: posesred
"""

from datetime import datetime
from typing import Optional, List
from fastapi_camelcase import CamelModel
from pydantic import Field, validator
from app.shared.base.base_schema import BaseResponse, ORMCamelCase


class GetCalculatorOperation(CamelModel):

    @validator('operation')
    def check_valid_operation(cls, v):
        """
        checks for a valid operation using plus minus multi and divide
        :param v:
        :return:
        """
        valid_operations = ['+', "-", "*", "/"]
        if v not in valid_operations:
            raise ValueError(f'Operation must be one of the following {valid_operations}')
        return v

    left_number: float
    right_number: float
    operation: str



class GetCalculatorOperationResponseDetail(ORMCamelCase):
    id: int
    timestamp: datetime
    result: Optional[float]
    execution_string: str


class GetCalculatorOperationResponse(BaseResponse):
    response: Optional[GetCalculatorOperationResponseDetail]


class GetCalculatorOperationHistoryResponse(BaseResponse):
    response: Optional[List[GetCalculatorOperationResponseDetail]]

