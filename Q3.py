n = int(input())
my_list = list(map(int, input().split()))
index = int(input())
del my_list[index - 1]
print(*my_list)
