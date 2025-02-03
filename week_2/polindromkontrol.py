
def palkontrol(kelime) :
    for i in range(kelimeUzunluk , int(kelimeUzunluk / 2) , -1) :
        if kelime[kelimeUzunluk - i] != kelime[i - 1] :
            return "kelime palindrom değil"
    return "kelime palindrom"

kelime = input("Lütfen kontrol ettireceğiniz kelimeyi giriniz: ")
kelimeUzunluk = len(kelime)
print(palkontrol(kelime))