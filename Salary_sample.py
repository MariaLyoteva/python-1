x = (int)(input('Please input a number' ))
if x < 100 :
    print('kleiner als 100')
else:
    print('großer als 100')

alter= (int)(input('Please input your age'))
geschlecht = input('Please input M for a male or F for a female')
if geschlecht != ('M'or 'F') and alter <18:
    print('false')
else:
    if(alter<30):
        if(geschlecht == 'M'):
            print(4000)
        else:
            print(4500)
    elif(geschlecht == 'M'):
         print(6000)
    else: 
        print(6500)
