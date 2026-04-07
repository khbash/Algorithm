def bin_search(arr: list, key : int) -> bool:
    """
    This function is useful for searching items in sorted array (with binary search algorithms).
    :param arr: your sorted array
    :return: True if items found or False if not.
    """

#array = [-4, 2, 5, 8, 19, 23, 35, 36, 48, 49, 67, 72, 85, 105, 107]

    L = 0
    R = len(arr) - 1
    mid = (R + L) // 2
    while L < R:
        if key == arr[mid]:
            return True
        elif key < arr[mid]:
            R = mid - 1
        else:
            L = mid + 1
        mid = (R + L) // 2
    if arr[L] == key:
        return True
    else:
        return False

array = [-4, 2, 5, 8, 19, 23, 35, 36, 48, 49, 67, 72, 85, 105, 107]

print(bin_search(array, 8))
    #print(bin_search(array))





