import os
import shutil

def dosyalari_kopyala():
    # Kopyalanacak kaynak dosyalar
    kaynak_dosyalar = ['page_2.jpg', 'page_3.jpg']
    
    # Scriptin çalıştığı dizin (root)
    root_dizin = os.getcwd()
    
    # Mevcut dizindeki klasörleri listele
    icerik = os.listdir(root_dizin)
    
    for dosya_adi in kaynak_dosyalar:
        kaynak_yolu = os.path.join(root_dizin, dosya_adi)
        
        # Kaynak dosya gerçekten var mı kontrol et
        if not os.path.exists(kaynak_yolu):
            print(f"Hata: {dosya_adi} ana dizinde bulunamadı!")
            continue
            
        for klasor in icerik:
            hedef_yolu = os.path.join(root_dizin, klasor)
            
            # Sadece klasörleri hedef al ve kaynak dosyanın kendisini klasör sanma
            if os.path.isdir(hedef_yolu):
                try:
                    # shutil.copy2 hem veriyi kopyalar hem de üzerine yazar
                    shutil.copy2(kaynak_yolu, hedef_yolu)
                    print(f"Başarılı: {dosya_adi} -> {klasor} klasörüne kopyalandı.")
                except Exception as e:
                    print(f"Hata: {klasor} klasörüne kopyalanırken sorun oluştu: {e}")

if __name__ == "__main__":
    dosyalari_kopyala()