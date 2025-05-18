def log_function_call(func):
    """Decorator that logs when a function is called"""
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Apply the decorator to a function
@log_function_call
def say_hello():
    print(f"Hello!")

# Test the decorated function
say_hello()