n = int(input("N = ? "))
spaces_beginning = 0
spaces_middle = 2 * n
points = n

while(spaces_beginning < 2 * n):
    print(spaces_beginning*'  ', points*'* ', spaces_middle*'  ', points*'* ', sep = "")
    spaces_beginning += 1
    if (spaces_middle != 0):
        spaces_middle -= 2
    if (spaces_beginning > n):
        points -= 18
