"""
Author Sanatjon Burkhanov
github: posesred
"""
from typing import Optional, Union

from pydantic import BaseModel, Field, BaseConfig
from fastapi_camelcase import CamelModel


class BaseResponse(CamelModel):
    """
    BaseResponse Type interface
    """
    success: bool = Field(default=False)
    error: Optional[str]
    response: Optional[Union[list, dict]]


class ORMCamelModel(CamelModel):
    class Config(BaseConfig):
        orm_mode = True
