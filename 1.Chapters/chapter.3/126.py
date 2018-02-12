a = [10,10,10]
soldout = 1
e = 1
change = -1
while soldout :
    print("Welcome~! This is the newest banding meachine.")
    print("What kind of drink do you want?")
    print("Coffee : 1, Orange Juice : 2, Hot Choco : 3, Exit Banding Meachine : 4")
    b = int(input())
    if b == 4 : break
    elif a[b-1] == 0 :
        print("Sold out.")
    else :
        print("Plese insert coins.")
        c = int(input())
        change = c - 300
    if change >= 0 :
        if (b == 1 and a[0] > 0) :
            a[0] = a[0] - 1
            print("Here is change %d." %change)
            # print(a[0])
        if b == 2 and a[1] > 0 :
            a[1] = a[1] - 1
            print("Here is change %d." %change)
            # print(a[1])
        if b == 3 and a[2] > 0 :
            a[2] = a[2] - 1
            print("Here is change %d." %change)
            # print(a[2])
    else : print("You didn't insert enough money.")

    print("Coffee : %d Orange Juice : %d Hot Choco : %d left\n" %(a[0], a[1], a[2]))

    if a[0] ==0 and a[1] == 0 and a[2] == 0 :
        print("Every drink is sold out. Sorry.")
        break
