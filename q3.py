my_list = [10, 20, 30, 40, 50]

index = int(input("Enter index to delete: "))

if 0 <= index < len(my_list):
    del my_list[index]
    print("Updated list:", my_list)
else:
    print("Invalid index")
