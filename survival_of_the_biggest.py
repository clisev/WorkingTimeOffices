str_numbers = input().split()
numbers = [int(num) for num in str_numbers]
num_to_remove = int(input())

sorted_numbers = sorted(numbers)
numbers_to_remove = sorted_numbers[:num_to_remove]
remaining_numbers = [num for num in numbers if num not in numbers_to_remove]

result = ", ".join(map(str, remaining_numbers))
print(result)
