# Number of rows
n=(int)(input())

# Loop over number of rows 
for i in range(n, 0, -1):
    
    # Nested reverse loop to handle number of columns
    for k in range(i,0,-1):
       if k>1:
           print(k, end=' ')
       else:
           print(k)
     
