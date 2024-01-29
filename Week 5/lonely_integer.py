def lonelyinteger(a):
    # Write your code here
    element_counts = {}
    for element in a:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    for element, count in element_counts.items():
        if count == 1:
            return element


# Example usage:
my_array = [1, 2, 2, 3, 4, 4, 5]
result = lonelyinteger(my_array)
print(result)