#N*N BOYUTLARINA SAHİP OLAN(İKİ BOYUTLU) BİR DİZİ OLUŞTURULACAK
#DIŞARDIAN İKİ KARAKTER GİRİLECEK
#SON OLARAK N*N BOYUTLU DİZİ EKRANA ÇIKTISI ALINACAK
print("\n")
boyut=int(input('Dizi boyutu giriniz:'))
isaret_1=input('1.karakteri giriniz:')
isaret_2=input('2.karakteri giriniz:')

for i in range(boyut):
    for k in range((boyut-i)):  #seklin sol taraf üst artısı
        print(isaret_1,end="")

    for m in range(i*2-1):
        print(isaret_2,end="")  #şeklin üsst ortası

    for i in range((boyut)-i):
        print(isaret_1,end="")  #şeklin sağ üst tarafı

    print()

#YUKARİDA YAZILAN KOD EKRANDA OLUŞACAK RESMİN ÜST KISMINI OLUŞTURUYO.

for i in range(boyut,0,-1):
    for k in range((boyut)-i):
        print(isaret_1,end="")     #sol alt

    for m in range(i*2-1):
        print(isaret_2,end="")  #alt orta

    for i in range((boyut)-i):
        print(isaret_1 ,end="")  #sağ alt
    print()

#YUKARIDA YAZAN KOD EKRANDA OLUŞACAK RESMİN ALT KISMINI OLUŞTURUYO.
