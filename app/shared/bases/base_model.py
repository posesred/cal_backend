"""
Author Sanatjon Burkhanov
github: posesred
"""
import logging
from typing import Optional, List

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base
from sqlalchemy_mixins import AllFeaturesMixin


logger = logging.getLogger('base_model')
Base = declarative_base()


class ModelMixin(AllFeaturesMixin):
    __abstract__ = True

    @classmethod
    def create(cls, *args, **kwargs) -> Optional[Base]:
        """
        args list of arguments postional arguments
        keywords arguments kwargs any arguemnt that has equals
        :return: Optional[cls]

        """
        object_id = kwargs.pop('id')
        if _object := cls.where(id=object_id).first():
            return
        try:
            new_object = cls(**kwargs)
            cls.session.add(new_object)
            cls.session.commit()
            return new_object
        except IntegrityError as e:
            logger.error(str(e))
            cls.session.rollback()
            return

    @classmethod
    def read(cls, *_, **kwargs) -> Optional[Base]:
        """
        reads/gets the first matching row to a given predicate
        :return: Optional[Base]
        """
        return cls.where(**kwargs).first()

    @classmethod
    def read_all(cls, *_, **kwargs) -> List[Optional[Base]]:
        """
        read/gets all objects matching a keyword critiria/ predicate
        :return: list[Optional[Base]]
        """
        return cls.where(**kwargs).all()
