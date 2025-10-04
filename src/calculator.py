"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    # Validate input types
    for val in (a, b):
        if not isinstance(val, (int, float)):
            raise TypeError("Both arguments must be numbers")
    
    # Perform calculation with logging
    print(f"Operation: {a} × {b}")
    result = a * b
    print(f"Answer: {result}")
    return result

def divide(a, b):
    """Divide a by b with enhanced error handling."""
    # Type validation
    for val, name in [(a, 'dividend'), (b, 'divisor')]:
        if not isinstance(val, (int, float)):
            raise TypeError("Division requires numeric inputs")
    
    # Zero division check
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")
    
    # Execute division with logging
    print(f"Operation: {a} ÷ {b}")
    result = a / b
    print(f"Answer: {result}")
    return result

# TODO: Students will add multiply, divide, power, sqrt functions


if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")