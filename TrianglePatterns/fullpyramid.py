n = int(input())
for i in range(1, n+1):
  left_side = " " * (n-i)
  num = ""
  for j in range(1, i+1):
    num = num + (str(j) + " ")
  print(left_side + num)
  
  
#Input:5

"""
Output:

    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5    

"""
