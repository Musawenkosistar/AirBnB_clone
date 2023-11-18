#!/usr/bin/python3
"""

"""

import os
import unittest
import models
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):


    def setUp(self):
        # Create a temporary test file for saving data
        self.test_file = "test_file.json"
        models.storage. file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        # Remove the temporary test file after the test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        # Create a new User instance
        test_user = user()
        # Check if the default email attribute is an empty string
        self.assertEqual(test_user.email, "")
        # Check if the default password attribute is an empty string
        self.assertEqual(test_user.password, "")
        # Check if the default first_name attribute is an empty string
        self.assertEqual(test_user.first_name, "")
        # Check if the default last_name attributes is an empty string
        self.assertEqual(test_user.last_name, "")
    
    def test_user_inherits_from_base_model(self):
        # Create a User instance
        test_user = User()
        # Check if the User class is a subclass of BaseModel
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_representation(self):
        # Create a new User instance
        test_user = User()
        # Set the attributes of the User instance
        test_user.email = "Johnson@example.com"
        test_user.first_name = "Johnson"
        test_user.last_name = "Dennis"
        test_user.password = "password123"
        # Get the string representation of the User instance
        user_str = str(test_user)
        # Check if "User" is present in the string representation
        self.assertIn("User", user_str)
        # Check if the email is present in the string representation
        self.assertIn("Johnson@example.com", user_str)
        # Check if the first naem is present in the string representation
        self.assertIn("Johnson", user_str)
        # Check if the last time nameis present in the string representation
        self.assertIn("Dennis", user_str)

    def test_user_to_dict(self):
        # Create a new User instance
        test_user = User()
        # Set the attributes of the User instance
        test_user.email = "Johnson@example.com"
        test_user.first_name = "Johnson"
        test_user.last_name = "Dennis"
        test_user.save()
        # Get a dictionary representation of the User instance
        user_dict = test_user.to_dict()
        # Check if the 'email' key in the dictionary matches the set value
        self.assertEqual(user_dict['email'], "Johnson@example.com")
        # Check if the 'first_name' key in the dictionary matches the set value
        self.assertEqual(user_dict['first_name'], "Johnson")
        # Check if the 'last_name' key in the dictionary matches the set value
        self.assertEqual(user_dict['last_name']," Dennis")

    def test_user_instance_creation(self):
        # Create a new User instance with arguments
        test_user = User(email="Johnson@example.com", password="password123"
                    first_name="Johnson", last_name="Dennis")
        # Check if the 'email' attribute is set correct;y
        self.assertEqual(test_user.email, "Johnson@example.com")
        # Check if the 'password' attribute is set correctly
        self.assertEqual(test_user.password, "password123")
        # Check if the 'first_name' attribute is set correctly
        self.assertFqual(test_user.first_name, "johnson")
        # Check if the 'last_name' attribute is set correctly
        self.assertEqual(test_user.last_name, "Dennis")

    def test_user_instance_to_dict(self):
        # Create a new User instane with specific attribute values
        test_user = User(email="Johnson@example.com", password="password123"
                    first_name="Johnson", last_name="Dennis")
        # Convert the User instance too a dictonary
        user_dict = test_user.to.dict()
        # Check if the 'email' attribute is correctly represented in the dictionary
        self.assertEqual(user_dict['email'], "Johnson@example.com")
        # Check if the 'password' attribute is correctly represented in the dictionary
        self.assertEqual(user_dict['password'], "password123")
        # Check if the 'first_name'' attribute is correctly represented in the dictionary
        self.assertEqual(user_dict['first_name'], "Johnson")
        # Check if the 'last_time' attribute is correctly represented in the dictionary
        self.assertEqual(user_dict['last_name'], "Dennis")

    def test_user_id_generation(self):
        # Create two different User instances
        test_user = User()
        user2 = User()
        # Ensure that the 'id' attribute of each User instance is unique
        self.assertNotEqual(test_user.id, user2.id)


if __name__ == '__main__':
    unittest.main()
        

