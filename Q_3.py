my_list = list(map(int, input().split()))
index = int(input())
del my_list[index]
print(*my_list)
