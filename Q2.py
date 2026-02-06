m = int(input("Enter m: "))
n = int(input("Enter n: "))

squares = {}

for i in range(m, n + 1):
    squares[i] = i * i

print(squares)
