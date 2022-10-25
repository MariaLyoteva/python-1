x = (int)(input('Please input a number between 1 and 6'))
t = (float)(input('Please input the curr temp'))
 
if(x==1 and t>= -273.15):
    t-= 273.15
    print(' Celsius to Kelvin', t)
elif(x==2 and t>= -273.15):
    t = t*1.8 + 32
    print(' Celsius to Fahrenheit', t)
elif(x==3 and t>= 0):
    t+= 273.15
    print('Kelvin to Celsiuis', t) 
elif(x==4  and t>= 0):
   t+= 273.15000000000003
   t = t*1.8 + 32
   print('Kelvin to Fahrenheit', t) 
elif(x==5 and t >= -459.67):
   t = 5/9 *(t-32)
   print('Fahrenheit to Celsius', t)
elif(x==6 and t >= -459.67):
      t = 5/9 *(t-32)
      t+= 273.15000000000003
      print('Fahrenheit to Kelvin', t)
else:
    print('Error')
