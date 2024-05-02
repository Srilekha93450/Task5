
import re  # Import the regular expression module

# Function to validate email addresses
def validate_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Match the input email against the pattern and return True if it matches, False otherwise
    return bool(re.match(pattern, email))

# Function to validate mobile numbers of Bangladesh
def validate_bangladesh_mobile(mobile_number):
    # Regular expression pattern for validating mobile numbers of Bangladesh
    pattern = r'^01[3-9]\d{8}$'
    # Match the input mobile number against the pattern and return True if it matches, False otherwise
    return bool(re.match(pattern, mobile_number))

# Function to validate telephone numbers of USA
def validate_usa_telephone(telephone_number):
    # Regular expression pattern for validating telephone numbers of USA
    pattern = r'^\(\d{3}\)\s?\d{3}-\d{4}$'
    # Match the input telephone number against the pattern and return True if it matches, False otherwise
    return bool(re.match(pattern, telephone_number))

# Function to validate a 16 character alpha-numeric password
def validate_password(password):
    # Regular expression pattern for validating a 16 character alpha-numeric password
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    # Match the input password against the pattern and return True if it matches, False otherwise
    return bool(re.match(pattern, password))

# Example usage:
email = "example@email.com"
mobile_number = "01712345678"
telephone_number = "(123) 456-7890"
password = "Abcdef@1234567890"
# Print the validation results for each case
print("Email:", validate_email(email))
print("Bangladesh Mobile:", validate_bangladesh_mobile(mobile_number))
print("USA Telephone:", validate_usa_telephone(telephone_number))
print("Password:", validate_password(password))
