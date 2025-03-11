def add(a, b):
    """Add two positive integers without using the '+' operator."""
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

# Example usage
print(add(5, 7))  # 12
