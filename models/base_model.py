#!usr/bin/python3
#Basemode class
'''base model'''

import uuid
from datetime import datetime
<<<<<<< HEAD
import models  
=======
import models
 
>>>>>>> 62620570d84bba2199ec862aa0c1f6efcba2e9ab
class BaseModel:
    def __init__(self, *args, **kwargs):
        """new instances"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key,value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self,key,datetime.strptime(value,time_format))
                else:
                    setattr(self,key,value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
<<<<<<< HEAD
            
            models.storage.new (self )
=======
        models.storage.new(self)
>>>>>>> 62620570d84bba2199ec862aa0c1f6efcba2e9ab
    
    def save(self):
        """
        saving
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        dictionary
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["updated_at"] = self.updated_at.isoformat()
        inst_dict["created_at"] = self.created_at.isoformat()

        return inst_dict

    def __str__(self):
        """
        print
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

if __name__ == "__main__":

    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
