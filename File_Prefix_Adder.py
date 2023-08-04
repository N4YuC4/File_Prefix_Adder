import datetime,os

count=1 #index numaraları için sayma sayacı

path=input("(DİKKAT BU BELİRTİLEN YOL YANLIŞ GİRİLDİĞİ TAKDİRDE İSTENMEYECEK SONUÇLARA YOL AÇABİLİR LÜTFEN İŞLEMİN SAĞLANACAĞI KLASOR YOLUNU BİR KEZ DAHA KONTROL EDEREK GİRİNİZ)\nKlasör yolunu giriniz:")
os.chdir(path) #belirtilen dizine gidilir

bulunanlar=os.listdir() #dizinde bulunanların listesi

#dizinde bulunanları değeri oluşturulma tarihi olucak sekilde bir sozluk oluşturulur
tarih_ile_bulunanlar={}
for i in bulunanlar:
    tarih_ile_bulunanlar[i]=datetime.datetime.strftime(datetime.datetime.fromtimestamp(os.stat(f"{i}").st_ctime),"%c")

sorted_list=dict(sorted(tarih_ile_bulunanlar.items(), key=lambda x:x[1]))#olusturlan sozluk tarihe gore sıralanır


#sozlukteki her bir elemana prefix numaraları yerleştirilir
for i in sorted_list.keys():
    os.rename(i,f"{count}-{i}")
    count+=1
