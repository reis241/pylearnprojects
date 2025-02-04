maxLong = int(input("Lütfen maximum uzunluğun kaç olacağını belirleyin(tek sayı olmazsa en büyük tek sayıya yuvarlanır): "))
for i in range(1 , maxLong + 1 , 2) :
    space = (maxLong - i) // 2
    for j in range(0 , space) :
        print(" " , end="")
    for k in range(0 , i) :
        print("*" , end="")
    for u in range(0 , space) :
        print(" " , end="")
    print("")
for a in range(maxLong , 0 , -2) :
    space = (maxLong + 2 - a) // 2
    for j in range(0 , space) :
        print(" " , end="")
    for k in range(2 , a) :
        print("*" , end="")
    for u in range(0 , space) :
        print(" " , end="")
    print("")