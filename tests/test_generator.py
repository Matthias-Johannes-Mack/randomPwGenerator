import unittest
from password_generator.generator import PasswordGenerator
import string

class TestPasswordGenerator(unittest.TestCase):
    """
    Test suite for the PasswordGenerator class.

    This suite contains a set of tests to verify the functionality
    of the PasswordGenerator class, ensuring that it generates passwords
    with the expected characteristics based on user-defined settings.
    """

    def test_default_settings(self):
        """
        Checks that a new instance of PasswordGenerator has the default
        settings with a length of 12 characters, including uppercase
        letters, lowercase letters, digits, and no special characters.
        """
        password_gen = PasswordGenerator()
        self.assertEqual(password_gen.length, 16)
        self.assertTrue(password_gen.include_uppercase)
        self.assertTrue(password_gen.include_lowercase)
        self.assertTrue(password_gen.include_digits)
        self.assertFalse(password_gen.include_special_chars)

    def test_generate_password(self):
        """
        Checks that the generated password has the correct length and
        contains at least one uppercase letter, one lowercase letter,
        and one digit. Additionally, ensures that no special characters
        are included by default.
        """
        password_gen = PasswordGenerator()
        password = password_gen.generate_password()
        self.assertEqual(len(password), password_gen.length)
        self.assertTrue(any(c.isupper() for c in password))  # At least one uppercase letter
        self.assertTrue(any(c.islower() for c in password))  # At least one lowercase letter
        self.assertTrue(any(c.isdigit() for c in password))  # At least one digit
        self.assertFalse(any(c in string.punctuation for c in password))  # No special characters by default
    
    def test_generate_password_mssql_policy(self):
        """
        Checks that the password follows the mssql policy
        """
        password_gen = PasswordGenerator()
        password_gen.set_mssql_policy(True)
        password = password_gen.generate_password()
        self.assertEqual(len(password), max(8, password_gen.length))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in "!$#%" for c in password))
        
    def test_set_length(self):
        """
        Checks that the length of the generated password is updated
        after setting a new length using the set_length method.
        """
        password_gen = PasswordGenerator()
        password_gen.set_length(16)
        self.assertEqual(password_gen.length, 16)

    def test_set_include_uppercase(self):
        """
        Checks that the include_uppercase attribute is updated
        after using the set_include_uppercase method.
        """
        password_gen = PasswordGenerator()
        password_gen.set_include_uppercase(False)
        self.assertFalse(password_gen.include_uppercase)

    def test_set_include_lowercase(self):
        """
        Checks that the include_lowercase attribute is updated
        after using the set_include_lowercase method.
        """
        password_gen = PasswordGenerator()
        password_gen.set_include_lowercase(False)
        self.assertFalse(password_gen.include_lowercase)

    def test_set_include_digits(self):
        """
        Checks that the include_digits attribute is updated
        after using the set_include_digits method
        """
        password_gen = PasswordGenerator()
        password_gen.set_include_digits(False)
        self.assertFalse(password_gen.include_digits)

    def test_set_include_special_chars(self):
        """
        Checks that the include_special_chars attribute is updated
        after using the set_include_special_chars method
        """
        password_gen = PasswordGenerator()
        password_gen.set_include_special_chars(True)
        self.assertTrue(password_gen.include_special_chars)
        
    def test_set_mssql_policy(self):
        """
        Checks that the mssql_policy attribute is updated
        after using the set_mssql_policy method
        """
        password_gen = PasswordGenerator()
        password_gen.set_mssql_policy(True)
        self.assertTrue(password_gen.mssql_policy)

if __name__ == '__main__':
    unittest.main()
