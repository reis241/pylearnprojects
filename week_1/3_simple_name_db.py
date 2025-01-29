names =["enes" , "taha" , "eyüp" , "melih" , "özlem"]
print("Names veriable is \"",names,"\"")
answer = 0
while answer != 4 :
    print("add new name       : 1\nremove name        : 2\nsee names veriable : 3\nquit               : 4")
    answer = int(input("what do you want : "))

    if answer >= 1 and answer <= 4 :
        if answer == 1 :
            addname = input("Please Type the name to be added to the array : ")
            names.append(addname)
            print("added! New array is",names)
        if answer == 2 :
            removename = input("please enter the name to be deleted : ")
            names.remove(removename)
            print("removed! New array is",names)
        if answer == 3 :
            print(names)

print("Program finished Last array is",names)