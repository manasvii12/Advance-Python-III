import functools
import datetime

# 1. Login Authentication Decorator
logged_in = False  # Change to True to simulate a logged-in user
def login_required(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        if not logged_in:
            print("Access denied: User not logged in.")
            return
        return func(*args, **kwargs)
    return wrapper

@login_required
def protected_function():
    print("You have accessed a protected function!")

# -------------------------------
# 2. Function Call Logger Decorator
# -------------------------------
def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function'{func.__name__}'called at {datetime.datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def sample_function():
    print("Function is running...")

# 3. Input Validation Decorator
def validate_positive_integers(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                print("Error: All arguments must be positive integers.")
                return
        return func(*args, **kwargs)
    return wrapper

@validate_positive_integers
def add_numbers(a, b):
    print(f"Sum = {a + b}")

# 4. Function Call Counter Decorator

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function'{func.__name__}'has been called{wrapper.call_count} times.")
        return func(*args,**kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # 1. Login Authentication
    protected_function()  # Will deny access unless logged_in = True

    # 2. Function Call Logger
    sample_function()

    # 3. Input Validation
    add_numbers(5, 10)   # Valid
    add_numbers(-3, 7)   # Invalid

    # 4. Function Call Counter
    greet("Manasvi")
    greet("Manasvi")
    greet("Manasvi")
