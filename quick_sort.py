def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        less = [i for i in arr[1:] if i < arr[0]]
        more = [i for i in arr[1:] if i >= arr[0]]
        return quick_sort(less)+[arr[0]] + quick_sort(more)


