def common_divisors(a, b):
    """Find common divisors between two numbers."""
    return [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]

# Example usage
print(common_divisors(12, 18))  # [1, 2, 3, 6]
