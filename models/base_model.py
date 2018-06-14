#!/usr/bin/env pytohn3
import uuid
from datetime import datetime
import models
import json


class BaseModel:

    def __init__(self, *args, **kwargs):
        """ sets up BaseModel class
        """
        if kwargs:
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            for i, x in kwargs.items():
                if i != "__class__":
                    setattr(self, i, x)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Prints str magic method (prints class info)
        """
        return ('[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__))

    def __repr__(self):
        return self.__str__()

    def save(self):
        """ This saves the update time of the module
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = type(self).__name__
        new_dict['updated_at'] = datetime.now().isoformat()
        new_dict['created_at'] = datetime.now().isoformat()
        return new_dict
