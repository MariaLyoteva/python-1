n = (int)(input())
counter=0
while(abs(n)>0):
    n = (int)(n/10)
    counter+=1
print(counter)
