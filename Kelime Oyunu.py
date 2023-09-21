import time 
import random

def oyun():

    list1 = ("bina" , "sıfat" , "kelime" , "keman" , "telefon" , "görüş" , "harf" , "hayvan" , "köpek" , "şemsiye" , "leblebi" , "kemik" , "kitap" , "araba" , )



    word = random.choice(list1)

    print("küçük harfle yazmaya özen gösterin")
    time.sleep(1)
    print(word[0])
    time.sleep(1)

    tahmin = input("tahmininizi yazınız:")


    if tahmin == word:
        print("TEBRİKLER DOĞRU BİLDİNİZ")
        time.sleep(1)
        print("puanınız 100")
        time.sleep(3)
        return
        
        

    else:
        print("YANLIŞ CEVAP")
        print(word[0:2])

        tahmin = input("tahmininizi yazınız:")


    if tahmin == word:
        print("TEBRİKLER DOĞRU BİLDİNİZ")
        time.sleep(1)
        print("PUANINIZ 50")
        time.sleep(3)
        return
        
    else:
        print("YANLIŞ CEVAP son hak")
        time.sleep(1)
        print(word[0:3])

        tahmin = input("tahmininizi yazınız:")

    if tahmin == word:
            print("TEBRİKLER DOĞRU BİLDİNİZ")
            time.sleep(1)
            print("PUANINIZ 25")
            time.sleep(3)
            return
            

    else:
        print("YANLIŞ CEVAP")
        time.sleep(1)
        print("OYUNU KAYBETTİNİZ")
        time.sleep(1)
        print("doğru kelime: " + word)
        
        time.sleep(3)

    
oyun()


print("Tekrar oynamak istermisiniz") 
print("E / H")

yanıt = input("")

cevap = "E"

if yanıt == cevap: 
    oyun()

else: 
    print("kapatılıyor")
    time.sleep(1)
    exit()

    print("Tekrar oynamak istermisiniz") 
print("E / H")

yanıt = input("")

cevap = "E"

if yanıt == cevap: 
    oyun()

else: 
    print("kapatılıyor")
    time.sleep(1)
    exit()

    print("Tekrar oynamak istermisiniz") 
print("E / H")

yanıt = input("")

cevap = "E"

if yanıt == cevap: 
    oyun()

else: 
    print("kapatılıyor")
    time.sleep(1)
    exit()

    print("Tekrar oynamak istermisiniz") 
print("E / H")

yanıt = input("")

cevap = "E"

if yanıt == cevap: 
    oyun()

else: 
    print("kapatılıyor")
    time.sleep(1)
    exit()

    print("Tekrar oynamak istermisiniz") 
print("E / H")

yanıt = input("")

cevap = "E"

if yanıt == cevap: 
    oyun()

else: 
    print("kapatılıyor")
    time.sleep(1)
    exit()
