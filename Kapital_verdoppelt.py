kapital = (int)(input())
zin=(int)(input())
kap_zin = kapital
counter=0
while(kap_zin<kapital*2):
    kap_zin = kap_zin + kap_zin*(zin/100)
    counter+=1
print(counter)
