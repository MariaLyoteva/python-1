year = (int)(input('Jahr'))
if (year % 400 == 0) and (year % 100 == 0):
        print(year, 'ist Schaltjahr')
elif (year % 4 ==0) and (year % 100 != 0):
     print(year, 'ist Schaltjahr')
else:
    print(year, 'ist kein Schaltjahr')
