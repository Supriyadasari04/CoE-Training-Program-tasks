def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_lst = remove_duplicates(lst)
print(unique_lst)
