n = int(input()) 
counter=0
for i in range(1, n):
   if n%i == 0:
       counter+=1
      
if counter==1:
   print(n, 'ist eine Primzahl')
else:
   print(n, 'ist keine Primzahl')
