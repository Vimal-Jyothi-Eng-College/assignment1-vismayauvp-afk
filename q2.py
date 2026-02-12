m = int(input("Enter starting number (m): "))
n = int(input("Enter ending number (n): "))

square_dict = {}

for i in range(m, n + 1):
    square_dict[i] = i ** 2

print(square_dict)
