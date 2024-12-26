# Merge Dictionary

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)

# Other Way

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

merged_dict = dict1 | dict2
print(merged_dict)