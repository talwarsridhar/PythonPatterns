n = int(input())
for i in range(n):
  num = 1  
  pattern = ""
  for j in range(n):
    pattern = pattern + (str(num) + " ")
    num = num + 1
  print(pattern)
  
  
#Output:
"""
1 2 3
4 5 6
7 8 9
"""
