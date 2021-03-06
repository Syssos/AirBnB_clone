#!/usr/bin/python3
'''
Defines unittests for BaseModel Class
'''
import unittest
import json
import sys
import pep8
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    '''Testing BaseModel class'''

    @classmethod
    def setUpClass(cls):
        """ creates instance of class and tests
        """
        cls.bas1 = BaseModel()
        cls.bas1.name = "Holberton"
        cls.bas1.number = 90

    @classmethod
    def tearDown(cls):
        """ Deletes instances after each test
        """
        del cls.bas1

    def test_basemodel_docstring(self):
        """ Tests BaseModel for all docstrings
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def Pep8_test(self):
        """Pep8 style test"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_file(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_basemodel_str(self):
        """ tests str functiionality
        """
        self.assertEqual(str(self.bas1), "[{}] ({}) {}".format(self.bas1.__class__.__name__,self.bas1.id,str(self.bas1.__dict__)))

    def test_str_funtion(self):
        self.assertTrue(isinstance(self.bas1, BaseModel))

    def Test_for_all_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def Test_attr_save(self):
        self.bas1.save()
        self.assertNotEqual(self.bas1.created_at, self.bas1.uodated_at)

    def test_to_dict(self):
        bas1_dict = self.bas1.to_dict()
        self.assertIsInstance(bas1_dict['created_at'], str)
        self.assertIsInstance(bas1_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
