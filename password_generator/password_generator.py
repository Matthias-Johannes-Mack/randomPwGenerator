import argparse
from password_generator import PasswordGenerator

def main():
    # Set up the argument parser for command-line options
    parser = argparse.ArgumentParser(description='Generate random passwords.')
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password')
    parser.add_argument('-u', '--include-uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('-d', '--include-digits', action='store_true', help='Include digits')
    parser.add_argument('-s', '--include-special-chars', action='store_true', help='Include special characters')
    parser.add_argument('-m', '--mssql-policy', action='store_true', help='Use the  mssql password policy')
    

    # Parse command-line arguments
    args = parser.parse_args()

    # Create an instance of the PasswordGenerator class
    password_gen = PasswordGenerator()

    # Set the password criteria based on command-line arguments
    password_gen.set_length(args.length)
    password_gen.set_include_uppercase(args.include_uppercase)
    password_gen.set_include_digits(args.include_digits)
    password_gen.set_include_special_chars(args.include_special_chars)
    password_gen.set_mssql_policy(args.mssql_policy)

    # Generate and print the password
    generated_password = password_gen.generate_password()
    print(generated_password)

if __name__ == "__main__":
    main()
