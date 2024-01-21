import random
import string
from constants import DEFAULT_PASSWORD_LENGTH, EMPTY_STRING, MSSQL_SPECIAL_CHARS


class PasswordGenerator:
    def __init__(self):
        # Default settings for the password generator
        self.length = DEFAULT_PASSWORD_LENGTH
        self.include_uppercase = True
        self.include_lowercase = True
        self.include_digits = True
        self.include_special_chars = False
        self.mssql_policy = False

    def generate_password(self):
        # Build the character set based on user preferences
        characters = self.build_character_set()
        # Generate a random password using the selected character set
        if self.mssql_policy:
            return self.generate_mssql_compelling_password(characters)
        else:
            password = EMPTY_STRING.join(
                random.choice(characters) for _ in range(self.length)
            )
            return password

    def generate_mssql_compelling_password(self, characters):
        if self.length < 8:
            self.length = 8
        uppercase = random.choice(string.ascii_uppercase)
        lowercase = random.choice(string.ascii_lowercase)
        digit = random.choice(string.digits)
        special_char = random.choice(MSSQL_SPECIAL_CHARS)

        # Generate additional characters to meet the desired length
        additional_characters = random.choices(characters, k=max(0, self.length - 4))

        # Shuffle all the characters to randomize the order
        all_characters = [
            uppercase,
            lowercase,
            digit,
            special_char,
        ] + additional_characters
        random.shuffle(all_characters)

        return EMPTY_STRING.join(all_characters)

    def build_character_set(self):
        # Initialize an empty character set
        char_set = EMPTY_STRING

        # Handle the special case mssql policy
        if self.mssql_policy:
            self.include_lowercase = True
            self.include_uppercase = True
            self.include_digits = True
            self.include_special_chars = False

        # Add uppercase letters if selected
        if self.include_uppercase:
            char_set += string.ascii_uppercase

        # Add lowercase letters if selected
        if self.include_lowercase:
            char_set += string.ascii_lowercase

        # Add digits if selected
        if self.include_digits:
            char_set += string.digits

        # Add special characters if selected and mssql policy is enabled
        if self.include_special_chars:
            char_set += string.punctuation

        return char_set

    def set_length(self, length):
        # Set the length of the password
        self.length = length

    def set_include_uppercase(self, include_uppercase):
        # Set whether to include uppercase letters
        self.include_uppercase = include_uppercase

    def set_include_lowercase(self, include_lowercase):
        # Set whether to include lowercase letters
        self.include_lowercase = include_lowercase

    def set_include_digits(self, include_digits):
        # Set whether to include digits
        self.include_digits = include_digits

    def set_include_special_chars(self, include_special_chars):
        # Set whether to include special characters
        self.include_special_chars = include_special_chars

    def set_mssql_policy(self, mssql_policy):
        # Set whether to apply the mssql_policy
        self.mssql_policy = mssql_policy
