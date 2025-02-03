#fonksiyonlar başlangıç

def ebob(num1 , num2) :
     #ebob hesaplama
    for i in range(num2 , 0 , -1) :    
        if num1 % i == 0 and num2 % i == 0 :
            result = i
            break
    print("sayıların ebobu = " , result)

def ekok(num1 , num2) :
    #ekok hesaplama
    found = 0
    j = 0
    while found == 0 :
        j += 1
        if num1*j % num2 == 0 :
            found = 1
            result = num1*j
    print("sayıların ekoku= " , result)

#fonksiyonlar bitiş

num1 = int(input("Lütfen ilk sayıyı giriniz: "))
num2 = int(input("Lütfen ikinci sayıyı giriniz: "))

if num2 > num1 :
    chgvalue = num1
    num1 = num2
    num2 = chgvalue
    
ebob(num1 , num2)
ekok(num1 , num2)

