f_last =1
f_cur =1

 
while(f_cur<10000):
    f_temp = f_cur + f_last
    f_last = f_cur
    f_cur =f_temp
print(f_last)    
