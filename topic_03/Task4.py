def find_insert_position(sorted_list, value):
    left = 0
    right = len(sorted_list)

    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < value:
            left = mid + 1
        else:
            right = mid
    return left

my_list = [1, 3, 5, 7, 9]
new_value = 6
position = find_insert_position(my_list, new_value)
print(f"Новий елемент {new_value} слід вставити на позицію {position + 1}")

my_list.insert(position, new_value)
print("Список після вставки:", my_list)
