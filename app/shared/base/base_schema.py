"""
Author Sanatjon Burkhanov
github: posesred

"""
from typing import Optional, Union
from fastapi_camelcase import CamelModel
from pydantic import Field, BaseConfig


class BaseResponse(CamelModel):
    success: bool = Field(default=False)
    error: Optional[str]
    response: Optional[Union[list, dict]]


class ORMCamelCase(CamelModel):
    class Config(BaseConfig):
        orm_mode = True
