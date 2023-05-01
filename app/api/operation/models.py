"""
Author Sanatjon Burkhanov
github: posesred
"""
from datetime import datetime

import pytz
from sqlalchemy import Column, Text, Integer, DateTime, Float

from app.shared.bases.base_model import ModelMixin


class OperationHistory(ModelMixin):
    __tablename__ = 'operation_history'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    timestamp = Column(DateTime, default=lambda: datetime.now(pytz.utc))
    operation = Column(Text, nullable=False)
    left_number = Column(Float, nullable=False)
    right_number = Column(Float, nullable=False)
    result = Column(Float)
