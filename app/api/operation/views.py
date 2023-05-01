"""
Author Sanatjon Burkhanov
github: posesred
"""
from fastapi import APIRouter

from app.api.operation.models import OperationHistory
from app.api.operation.schemas import GetCalculatorOperationResponse, GetCalculatorOperation

router = APIRouter(
    prefix='/api/operation',
    tags=['operation']
)


@router.post('/get_operation', response_model=GetCalculatorOperationResponse)
def get_operation(context: GetCalculatorOperation):
    """
    gets the operation result and stores in database
    :param context: GetCalculatorOperation
    :return: GetCalculatorOperationResponseDetail
    """
    result: float = 0.0
    eval(f'result = {context.left_number} {context.operation} {context.right_number}')
    operation = OperationHistory.create(**context.dict(), result=result)
    return GetCalculatorOperationResponse(success=True, response=operation)
