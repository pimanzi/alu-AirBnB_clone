from uuid import uuid4
from datetime import datetime

class BaseModel():
    """This class is the parent class where all other classes to be created will inherit from"""
    def __init__(self, *args, **kwargs):
        """This is a constructor called every single time an instance is created"""
        if kwargs:
            for (key, value) in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    def __str__(self):
        """This is a function that will deal with string representation of the instance"""
        return f"{type(self).__name__} {self.id} {self.__dict__}"

    def save(self):
        """This function will automatically updates the time for attribute updated_at once an instance is updated"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """This function is responsible for dictionary representation form of an instance"""
        updated_dict = self.__dict__.copy()
        updated_dict["__class__"] = type(self).__name__
        updated_dict["created_at"] = self.created_at.isoformat()
        updated_dict["updated_at"] = self.updated_at.isoformat()
        return updated_dict



my_model= BaseModel(created_at= "2004-07-12T12:06:07.5000",updated_at="2004-08-12T12:06:07.5000")
result=my_model.to_dict()
print(result)