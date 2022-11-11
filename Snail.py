# Snail
h_tree = 90
h_snail = 0
day = 0

while True:
    day += 1
    if day % 7 == 0:
        h_snail -= 4
    else:
        h_snail += 3
        if h_snail >= h_tree:
            break
        h_snail -= 2

print('Die Schnecke erreicht nach', day, 'Tag(en) die Spitze des', h_tree, 'm hohen Baums')
