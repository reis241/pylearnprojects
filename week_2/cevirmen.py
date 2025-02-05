#ultimate çevirmen database
sozluk ={"elma" : "apple" , "bilgisayar" : "computer" , "çeviri" : "translate" , "klavye" : "keyboard" , "masa" : "table"}

#ultimate çevirmen türkceden ingilizceye sorgu
def turEng(sozcuk) :
    return sozluk.get(sozcuk.lower() , "bu kelimeyi bulamadım")

#ultimate çevirmen ingilizceden türkceye sorgu
def engTur(sozcuk) :
    for tur , eng in sozluk.items() :
        if eng == sozcuk.lower() :
            return tur
    return "bu kelimeyi bulamadım"

print("ultimate prof über düber çevirmene hoşgeldiniz\ntürkçeden ingilizceye için: 1\ningilizceden türkçeye için: 2")
chose = int(input(":"))
if chose == 1 :
    print("sözcüğün ingilizcesi : " , turEng(input("aratacağınız sözcüğü giriniz: ")))
elif chose == 2 :
    print("sözcüğün türkçesi : " , engTur(input("aratacağınız sözcüğü giriniz: ")))