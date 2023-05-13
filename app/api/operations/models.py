"""
Author Sanatjon Burkhanov
gitHub: posesred
this is the getter its gets the info we need
such as at the numbers and the operation
we put each thing in a table called operation history and colum it using names left_number
we also give each colum its own attribute and specify what is it
"""
import pytz
from datetime import datetime
from sqlalchemy import Column, Text, Integer, DateTime, Float
from app.shared.base.base_model import ModelMixin


class OperationHistory(ModelMixin):
    __tablename__ = 'operation_history'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(pytz.utc))
    operation = Column(Text, nullable=False)
    left_number = Column(Float, nullable=False)
    right_number = Column(Float, nullable=False)
    execution_string = Column(Text, nullable=False)
    result = Column(Float)

