numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtering even and odd numbers using lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print("Even:", even_numbers)
print("Odd:", odd_numbers)
