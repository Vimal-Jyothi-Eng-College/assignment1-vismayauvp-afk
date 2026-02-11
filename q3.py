n = int(input())
my_list = list(map(int, input().split()))
index = int(input())

if 0 <= index < len(my_list):
    del my_list[index]

print(*my_list)
