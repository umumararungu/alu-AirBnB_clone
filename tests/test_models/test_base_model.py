#!/usr/bin/python3
"""
testing BaseModel
"""
import unittest
from models.base_model import BaseModel

class Testbasemodel(unittest.TestCase):
    def init_Test(self):
        """
        init tests
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def save_Test(self):
        """
        save tests
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        current_updated_at = my_model.save()
        self.assertNotEqual(initial_updated_at,current_updated_at)

    def To_dict_test(self):
        """
        dict tests
        """
        my_model = BaseModel
        my_model_dict = my_model.To_dict()
        self.assertIsInstance(my_model_dict,dict)
        self.assertEqual(my_model_dict["__class__"],'BaseModel')
        self.assertEqual(my_model_dict['id'],my_model.id)
        self.assertEqual(my_model_dict['updated_at'],my_model.updated_at)
        self.assertEqual(my_model_dict['created_at'],my_model.created_at)

    def __str__(self):
        """
        str tests
        """
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith('BaseModel'))
        self.assertIn(my_model.id,str(my_model))
        self.assertIn(str(my_model.__dict__),str(my_model))

    if __name__ == "__main__":
        unittest.main()
