class Doktor:
    
    def __init__(self, isim):
        
        self.isim = isim
        
        self.randevular = []
    
    def randevu_ver(self, hasta):
        
        if isinstance(hasta, Hasta):
            
            self.randevular.append(hasta)
            
            print(f"{hasta.isim} adlı hasta {self.isim} doktoruna randevu aldı.")
        
        else:
            
            print("Randevu alınacak kişi hasta sınıfından türetilmemiş.")
      
    def randevu_sil(self, hasta):
        
        if hasta in self.randevular:
            
            self.randevular.remove(hasta)
            
            print(f"{hasta.isim} adlı hastanın {self.isim} ile olan randevusu iptal edilmiştir.")
            
        else:
            
            print("Böyle bir randevu zaten mevcut değildir")
    
    def randevulari_goster(self):
        
        for hasta in self.randevular:
            
            print(hasta.isim)
    

class Hasta:
    
    def __init__(self, isim,cinsiyet):
        
        self.isim = isim
        self.cinsiyet = cinsiyet
    
    def randevu_al(self, doktor):
       
        doktor.randevu_ver(self)
    
    def randevu_iptal_et(self, doktor):

        doktor.randevu_sil(self)
        
    def odaya_yat(self,oda):
        
        oda.hasta_ekle(self)
    
    def odadan_cık(self,oda):
        
        oda.hasta_cıkar(self)
    
class Oda:
    
    def __init__(self, oda_no):
        
        self.oda_no = oda_no
        
        self.hastalar = []
        
    def hasta_ekle(self,hasta):
        
        if isinstance(hasta, Hasta):
            
            self.hastalar.append(hasta)
        
            print(f"{hasta.isim}adlı hasta {self.oda_no} numaralı odaya yerleşti")
        else:    
            
            print("Odaya yerleşecek kişi hasta sınıfından türetilmemiş.")
            
    def hasta_cıkar(self,hasta):
        
        if hasta in self.hastalar:
            
            self.hastalar.remove(hasta)
            
            print(f"{hasta.isim} adlı hastanın {self.oda_no} numaralı odadan çıkışı yapılmıştır.")
            
        else:
            print("Böyle bir hasta zaten odada mevcut değildir")
class Tek_kisilik_Oda(Oda):
    
    kat = 1
    
    def __init__(self, oda_no, yatak_sayısı = 1):
        
        super().__init__(oda_no)
        
        self.yatak_sayısı = yatak_sayısı
        
        self.hastalar = []
        
    def hasta_ekle(self,hasta):
        
        if isinstance(hasta, Hasta):
            
            if len(self.hastalar) == 0:
                
                self.hastalar.append(hasta)
        
                print(f"{hasta.isim} adlı hasta {self.oda_no} numaralı odaya yerleşti")
            
            else:
                
                print(f"{self.oda_no} numralı oda dolu.")
        else:    
            
            print("Odaya yerleşecek kişi hasta sınıfından türetilmemiş.")
            
    def hasta_cıkar(self,hasta):
        
        if hasta in self.hastalar:
            
            self.hastalar.remove(hasta)
            
            print(f"{hasta.isim} adlı hastanın {self.oda_no} numaralı odadan çıkışı yapılmıştır.")
            
        else:
            print("Böyle bir hasta zaten odada mevcut değildir")
    def hastaları_goster(self):
        
        for hasta in self.hastalar:
            
            print(hasta.isim)            
class Iki_kisilik_Oda(Tek_kisilik_Oda):
    kat = 2
    
    def __init__(self,oda_no, yatak_sayısı = 2):
        
        super().__init__(oda_no)
        
        self.yatak_sayısı = yatak_sayısı
        
        self.hastalar = []
        
    def hasta_ekle(self,hasta):
        
        if isinstance(hasta, Hasta):
            
            if len(self.hastalar) < 2:
                
                self.hastalar.append(hasta)
                
                print(f"{hasta.isim} adlı hasta {self.oda_no} numaralı odaya yerleşti")
            else:
                
                print(f"{self.oda_no} numaralı oda dolu!!")
        else:
            
            print("Odaya yerleşecek kişi hasta sınıfından türetilmemiş.")
            
    def hasta_cıkar(self,hasta):
        
        if hasta in self.hastalar:
            
            self.hastalar.remove(hasta)
            
            print(f"{hasta.isim} adlı hastanın {self.oda_no} numaralı odadan çıkışı yapılmıştır.")
            
        else:
            print("Böyle bir hasta zaten odada mevcut değildir.") 
            
    def hastaları_goster(self):
        
        for hasta in self.hastalar:
            
            print(hasta.isim)            
class Uc_kisilik_Oda(Iki_kisilik_Oda):
    kat = 3
    
    def __init__(self, oda_no, yatak_sayısı = 3):
        
        super().__init__(oda_no)
        
        self.yatak_sayısı = yatak_sayısı
        
        self.hastalar = []
        
    def hasta_ekle(self,hasta):
            
        if isinstance(hasta, Hasta):
            if len(self.hastalar) < 3:
                self.hastalar.append(hasta)
                    
                print(f"{hasta.isim} adlı hasta {self.oda_no} numaralı odaya yerleşti")
                
            else:
                    
                print(f"{self.oda_no} numaralı oda dolu!!")
        else:
            print("Odaya yerleşeecek kişi hasta sınıfından türetilmemiş.")
    def hasta_cıkar(self,hasta):
        
        if hasta in self.hastalar:
            
            self.hastalar.remove(hasta)
            
            print(f"{hasta.isim} adlı hastanın {self.oda_no} numaralı odadan çıkışı yapılmıştır")
            
        else:
            
            print("Böyle bir hasta zaten odada mevcut değildir.")
                
    def hastaları_goster(self):
        
        for hasta in self.hastalar:
            
            print(hasta.isim)
class Pskiyatri_Doktoru(Doktor):
    
    def __init__(self, isim, bölüm):
        
        super().__init__(isim)
        
        self.bölüm = bölüm
        
   
    def randevu_ver(self, hasta):
        
        if isinstance(hasta, Hasta):
           
            self.randevular.append(hasta)
            
            print(f"{hasta.isim} adlı hasta {self.isim} adlı pskiyatri doktoruna randevu aldı.")
        
        else:
            
            print("Randevu alınacak kişi hasta sınıfından türetilmemiş.") 
class KulakBurunBogaz_Doktoru(Doktor):
    
    def __init__(self, isim, bölüm):
        
        super().__init__(isim)
        
        self.bölüm = bölüm
        
    def randevu_ver(self, hasta):
        
        if isinstance(hasta, Hasta):
            
            self.randevular.append(hasta)
            
            print(f"{hasta.isim} adlı hasta {self.isim} adlı kulak burun boğaz doktoruna randevu aldı.")
        
        else:
            
            print("Randevu alınacak kişi hasta sınıfından türetilmemiş.")          
class KalpHastalıkları_Doktoru(Doktor):
    
    def __init__(self, isim, bölüm):
        
        super().__init__(isim)
        
        self.bölüm = bölüm
        
    def randevu_ver(self, hasta):
        
        if isinstance(hasta, Hasta):
            
            self.randevular.append(hasta)
            
            print(f"{hasta.isim} adlı hasta {self.isim} adlı kalp hastalıkları doktoruna randevu aldı.")
        
        else:
            
            print("Randevu alınacak kişi hasta sınıfından türetilmemiş.")
doktor1 = Pskiyatri_Doktoru("Bünyamin Genç", "Pskiyatri")
doktor2 = KalpHastalıkları_Doktoru("Ümit Kaan Arzuoğlu","Kalp Hastalıkları")
doktor3 = KulakBurunBogaz_Doktoru("Metin Fırat","Kulak Burun Boğaz")
doktor4 = KulakBurunBogaz_Doktoru("Enes Cüreoğlu","Kulak Burun Boğaz")
doktor5 = KulakBurunBogaz_Doktoru("Salih Sevim","Kulak Burun Boğaz")


hasta1 = Hasta("Eray Yeşilnacar ","Erkek")
hasta2 = Hasta("Furkan Bekar","Erkek")
hasta3 = Hasta("Salih Demir","Erkek")


doktor1.randevu_ver(hasta1)
doktor1.randevulari_goster()
hasta2.randevu_al(doktor1)
doktor1.randevulari_goster()
hasta1.randevu_al(doktor2)
doktor3.randevu_ver(hasta3)
doktor3.randevulari_goster()

doktor3.randevu_sil(hasta3)

doktor3.randevulari_goster()
oda102 = Uc_kisilik_Oda(102,3)

hasta2.odaya_yat(oda102)

oda102.hastaları_goster()
hasta2.odadan_cık(oda102)
oda102.hastaları_goster()


oda103 = Iki_kisilik_Oda(103,2)
hasta3.odaya_yat(oda103)
oda103.hastaları_goster()
hasta3.odadan_cık(oda103)
oda103.hastaları_goster()

oda101 = Tek_kisilik_Oda(101,1)
hasta1.odaya_yat(oda101)
oda101.hastaları_goster()
hasta1.odadan_cık(oda101)
oda101.hastaları_goster()