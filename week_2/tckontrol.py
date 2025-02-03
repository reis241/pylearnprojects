while True :
    sayi = (input("Lütfen 11 haneli sayı giriniz (tc ye benzesin opsiyonel)\n: "))
    if len(sayi) == 11 :

        break
    else :
        print("sayıyı beğenmedim, düzgün bi sayı gir (11 haneli değil)")

if int(sayi[9]) == (sum(int(sayi[i]) for i in range(8 , -1 , -2))*7 - sum(int(sayi[j]) for j in range(7 , 0 , -2))) % 10 and int(sayi[10]) == sum(int(sayi[k]) for k in range(0 , 10)) % 10 :
    print("bu gerçek bir tc kimlik numarası olabilir")
else :
    print("al bu sayıyı bu gün eve erken git")
