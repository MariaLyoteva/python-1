x = (int)(input('Please input a number between 1 and 6'))
t = (float)(input('Please input the curr temp'))

def cel_kel(t):
     t-= 273.15
     print(' Celsius to Kelvin', t)
     
def cel_fahr(t):
     t = t*1.8 + 32
     print(' Celsius to Fahrenheit', t)
def kel_cel(t):
     t+= 273.15
     print('Kelvin to Celsiuis', t) 
def kel_fahr(t):
     t+= 273.15000000000003
     t = t*1.8 + 32
     print('Kelvin to Fahrenheit', t) 
    
def fahr_cel(t):
     t = 5/9 *(t-32)
     print('Fahrenheit to Celsius', t)
def fahr_kel(t):
     t = 5/9 *(t-32)
     t+= 273.15000000000003
     print('Fahrenheit to Kelvin', t)
     
     
 
if(x==1 and t>= -273.15):
   cel_kel(t)
elif(x==2 and t>= -273.15):
     kel_cel(t)
elif(x==3 and t>= 0):
    kel_fahr(t)
elif(x==4  and t>= 0):
  fahr_cel(t) 
elif(x==5 and t >= -459.67):
   fahr_cel(t)
elif(x==6 and t >= -459.67):
     fahr_kel(t)
else:
    print('Error')    
