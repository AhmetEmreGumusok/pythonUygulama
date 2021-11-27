
l=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
duzList=[]

def listemi(item): # bu fonksiyon recursive çalışır
    if isinstance(item,list): # item list mi diye kontrol eder
        for x in item: # list ise her biri için tekrar içine girer
            listemi(x)
    else:
        duzList.append(item) # item liste değilse duzList e ekler


for i in l: #input olan listenin her bir elemanını listemi fonksiyonuna gönderir
    listemi(i)
print(duzList)

