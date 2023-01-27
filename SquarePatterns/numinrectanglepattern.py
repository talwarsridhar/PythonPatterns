m = int(input())
n = int(input())
num = 1
for i in range(m):
    empty = ""
    for j in range(n):
        empty = empty + str(num) + " "
        num += 1
    print(empty)

 
#Input:
"""
m = 2
n = 3
"""


"""
Output:

1 2 3
4 5 6

"""
