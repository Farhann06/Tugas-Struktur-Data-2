def intersection(arr1, arr2):
    set2 = set(arr2)
    return [x for x in arr1 if x in set2]