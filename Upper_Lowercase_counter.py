def count_up_down(a):
    counter=0
    counter_low=0
    for i in a:
        
        if i.isupper():
            counter+=1
        else:
            counter_low+=1
    print( 'Uppercase ',counter, 'Lowercase', counter_low )   

