n = int(input())
for i in range(n):
    pattern = ""
    second = n - i
    for j in range(1, second+1):
        pattern = pattern + (str(j) + " ")
    print(pattern)
    
#Output:
"""
1 2 3 4 5
1 2 3 4
1 2 3 
1 2 
1 
"""
