import datetime,os
count=1
path=input("(DİKKAT BU BELİRTİLEN YOL YANLIŞ GİRİLDİĞİ TAKDİRDE İSTENMEYECEK SONUÇLARA YOL AÇABİLİR LÜTFEN İŞLEMİN SAĞLANACAĞI KLASOR YOLUNU BİR KEZ DAHA KONTROL EDEREK GİRİNİZ)\nKlasör yolunu giriniz:")
os.chdir(path)
bulunanlar=os.listdir()
tarih_ile_bulunanlar={}
for i in bulunanlar:
    tarih_ile_bulunanlar[i]=datetime.datetime.strftime(datetime.datetime.fromtimestamp(os.stat(f"{i}").st_ctime),"%c")

sorted_list=sorted(tarih_ile_bulunanlar.items(), key=lambda x:x[1])
sorted_dict=dict(sorted_list)
for i in sorted_dict.keys():
    os.rename(i,f"{count}-{i}")
    count+=1
