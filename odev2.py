l=[9,[1, 2], [3, 4], 8,[5, 6, 7]]  # verilenden farklı olsa da çalışır 9 ve 8 ekledim
#ilk sorudaki yapı gibi yaptım. yani bir liste elemanının içinde de liste olsa çalışır

def listemi(item): # bu fonksiyon recursive çalışır
    if isinstance(item,list): # item list mi diye kontrol eder
        item.reverse() # list olan item ters çevrilir
        for x in item: # alt item lar liste mi diye fonksiyon kendini çağırır
            listemi(x)

for i in l: #input olan listenin her bir elemanını listemi fonksiyonuna gönderir
    listemi(i)

l.reverse() # en son listenin kendisi ters çevrilir
print(l)
