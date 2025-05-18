
class InvalidAgeError(Exception):
    """Raised when age is below 18"""
    pass

# Age validation function
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age {age} is below 18")
    print(f"Age {age} is valid")

# Test with exception handling
ages_to_test = [15, 20, 17, 25]

for age in ages_to_test:
    try:
        print(f"\nChecking age {age}:")
        check_age(age)
    except InvalidAgeError as e:
        print(f"Error: {e}")