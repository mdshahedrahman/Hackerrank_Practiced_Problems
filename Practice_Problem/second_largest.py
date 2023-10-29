# Example unsorted array
unsorted_array = [5, 2, 9, 1, 7, 9, 3, 7]

sorted_array = sorted(list(unsorted_array))

max_value = max(sorted_array)

second_highest_value = None

for num in sorted_array:
    if num != max_value:
        if second_highest_value is None or num > second_highest_value:
            second_highest_value = num

if second_highest_value is not None:
    print(second_highest_value)
else:
    print("There is no second highest value in the array.")