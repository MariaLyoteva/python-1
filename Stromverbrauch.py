stromvrb = (int)(input('Stromverbrauch'))
preis = 0.40
if(stromvrb <= 1000):
    print('Preis ist', preis)   
elif (stromvrb > 1000 and stromvrb <=2000):
     preis=0.35
     print('Preis ist', preis)   
else:
    preis=0.30
    print('Preis ist', preis)
