"""
Author Sanatjon Burkhanov
github: posesred
"""
from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel
from pydantic import Field, validator

from app.shared.bases.base_schema import BaseResponse, ORMCamelModel


class GetCalculatorOperation(CamelModel):
    """
    get operation input
    """

    @validator('operation')
    def check_valid_operation(cls, v):
        """
        check if operation is in the list of valid operations
        :param v: value of the operation
        :return: value error operation
        """
        valid_operations = ['+', '-', '/', '*']
        if v not in valid_operations:
            raise ValueError(f'Operation must be one of {valid_operations}')
        return v

    left_number: float
    right_number: float
    operation: str


class GetCalculatorOperationResponseDetail(ORMCamelModel):
    """
    get response operation detail
    """
    id: int
    timestamp: datetime
    result: Optional[float]


class GetCalculatorOperationResponse(BaseResponse):
    """
    Get response operation
    """
    response: GetCalculatorOperationResponseDetail
