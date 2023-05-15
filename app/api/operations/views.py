"""
Author Sanatjon Burkhanov
github: posesred
"""
from fastapi import APIRouter
from fastapi_sqlalchemy import db

from app.api.operations.models import OperationHistory
from app.api.operations.schemas import GetCalculatorOperationResponse, GetCalculatorOperation, \
    GetCalculatorOperationHistoryResponse

router = APIRouter(
    prefix='/api/operation',
    tags=['operation']
)

@router.post('/get/operation', response_model=GetCalculatorOperationResponse)
def get_operation(context: GetCalculatorOperation):
    """

    :param context:
    :return:
    """
    OperationHistory.set_session(db.session)
    exec_string = f'{context.left_number} {context.operation} {context.right_number}'
    if context.operation == '/':
        if context.right_number == 0:
            return GetCalculatorOperationResponse(error="Can not divide by zero twat")
    result = eval(exec_string)

    operation = OperationHistory.create(**context.dict(), result=result, execution_string=exec_string)
    return GetCalculatorOperationResponse(success=True, response=operation)


@router.get('/read/all', response_model=GetCalculatorOperationHistoryResponse)
def get_operation_history():
    """

    :param context:
    :return:
    """
    OperationHistory.set_session(db.session)
    history = OperationHistory.read_all()
    return GetCalculatorOperationHistoryResponse(success=True, response=history)
