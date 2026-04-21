# def suma(n):
#     if n==1:
#         return 1
#     return n+suma(n-1)
#
# print(suma(10))

# cotrl slesh

# S = 0
# n = 10
# for i in range(1,n+1):
#     S += i
# print(S)

# def fib(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(25))

def reverse_list(arr):
    if len(arr) == 1:
        return arr
    else:
        return [arr[-1]] + reverse_list(arr[:len(arr)-1])

print(reverse_list([5, 4, 8, 9]))