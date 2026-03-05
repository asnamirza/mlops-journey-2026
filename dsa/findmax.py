# Find the maximum number in a list

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Example
test_list = [10, 25, 7, 42, 13]
print("Max value:", find_max(test_list))