# Flatten a nested list using list comprehension.
nested_list = [[1,2,3],4,5,[6,7,8],9]
flattened_list = [num for sublist in nested_list for num in (sublist if isinstance(sublist, list) else [sublist])]
print(flattened_list)
