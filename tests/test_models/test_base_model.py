#!usr/bin/python3
"""
test BaseModel
"""
import unittest
from test_ models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """
        init tests
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        save tests
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        current_updated_at = my_model.save()
        self.assertNotEqual(initial_updated_at,current_updated_at)

    def test_to_dict(self):
        """
        dict tests
        """
        my_model = BaseModel()
        my_model_dict = my_model.To_dict()
        self.assertIsInstance(my_model_dict,dict)
        self.assertEqual(my_model_dict["__class__"],'BaseModel')
        self.assertEqual(my_model_dict['id'],my_model.id)
        self.assertEqual(my_model_dict['created-at'],my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'],my_model.created_at.isoformat())

def test_str(self):
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id,str(my_model))
        self.assertIn(str(my_model.__dict__),str(my_model))

if __name__ == "__main__":
    unittest.main()

