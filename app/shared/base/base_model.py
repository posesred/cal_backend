"""
Author Sanatjon Burkhanov
gitHub: posesred
our base getting that is not specific just gets/grabs things
or checks/reads them query
"""
import logging
# needed so we can log
from typing import Optional, List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base
from sqlalchemy_mixins import AllFeaturesMixin

logger = logging.getLogger('base_model')

Base = declarative_base()


class ModelMixin(AllFeaturesMixin):
    """
    there is an abstract true here meaning it can not be instatiated direly it is intended to be subclasses
    """
    __abstract__ = True

    @classmethod
    def get_or_create(cls, *args, **kwargs) -> Optional[Base]:
        """
        getter create
       this here pops or pulls out a data from the database and makes it a variable data_id
       first it checks if its there if it is there if it is it will return blank if it not
       it will create a new instance using whatever arguments are left aka kwargs
        """
        data_id = kwargs.pop('id', None)
        if _data := cls.where(id=data_id).first():
            return _data
        try:
            new_data = cls(**kwargs)
            cls.session.add(new_data)
            cls.session.commit()
            return new_data
        except IntegrityError as e:
            logger.error(str(e))
            cls.session.rollback()
            return

    # decorator that can make things class level like this function you can call it like a class
    # using ModelMixin.data_id like you dont have to use its instance
    @classmethod
    def read(cls, *_, **kwargs) -> Optional[Base]:
        """
        gets the first argument with equals sign aka kwargs
        """
        return cls.where(**kwargs).first()

    @classmethod
    def read_all(cls, *_, **kwargs) -> List[Optional[Base]]:
        """
        gets all the arguments in the database
        """
        return cls.where(**kwargs).all()
