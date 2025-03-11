def all_unique(numbers):
    """Check if all numbers in a sequence are unique."""
    return len(numbers) == len(set(numbers))

# Example usage
nums = [1, 2, 3, 4, 5]
print(all_unique(nums))  # True

nums = [1, 2, 3, 4, 1]
print(all_unique(nums))  # False
