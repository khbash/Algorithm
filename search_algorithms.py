# Linear search
array = [5, 9, 0, -2, 12, 14, 9, 4, 7, 8]
key = int(input())
is_found = False
for item in array:
    if item == key:
        is_found = True
        break
if is_found:
    print("Success")
else:
    print("Not Found")

# Complexity - 0(n)
