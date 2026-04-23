import os

class Point:
    """Nokta geometrilerini ve özniteliklerini temsil eden sınıf."""
    def __init__(self, point_id, x, y, label):
        self.id = int(point_id)
        self.x = float(x)
        self.y = float(y)
        self.label = str(label).strip()

    def __str__(self):
        return f"Nokta {self.id}: {self.label} (X: {self.x}, Y: {self.y})"


class Line:
    """Çizgi geometrilerini ve özniteliklerini temsil eden sınıf."""
    def __init__(self, line_id, name):
        self.id = int(line_id)
        self.name = str(name).strip()
        self.coordinates = []  # Çizgiyi oluşturan x, y koordinat çiftleri

    def add_coordinate(self, x, y):
        """Çizgiye yeni bir kırılma noktası (vertex) ekler."""
        self.coordinates.append((float(x), float(y)))

    def __str__(self):
        return f"Çizgi {self.id}: {self.name} ({len(self.coordinates)} kırılma noktası)"


def dosyadan_oku(dosya_yolu):
    """
    Verilen metin dosyasını okur ve içeriğine göre Point veya Line nesneleri listesi döndürür.
    """
    geometriler = []
    
    # Dosyanın var olup olmadığını kontrol et
    if not os.path.exists(dosya_yolu):
        print(f"Hata: {dosya_yolu} bulunamadı.")
        return geometriler

    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        # Boş satırları atlayarak tüm satırları oku ve temizle
        satirlar = [satir.strip() for satir in dosya.readlines() if satir.strip()]

    if not satirlar:
        return geometriler

    # İlk satır geometri tipini (point veya line), ikinci satır eleman sayısını verir
    geometri_tipi = satirlar[0].lower()
    
    if geometri_tipi == 'point':
        # Nokta formatı: X,Y,Etiket
        for i in range(2, len(satirlar)):
            veriler = satirlar[i].split(',')
            if len(veriler) >= 3:
                x = veriler[0]
                y = veriler[1]
                # Eğer etiketin içinde virgül varsa diye kalanı birleştiriyoruz
                etiket = ",".join(veriler[2:])
                # Nokta ID'si olarak okuma sırasını kullanıyoruz (1, 2, 3...)
                yeni_nokta = Point(i - 1, x, y, etiket)
                geometriler.append(yeni_nokta)

    elif geometri_tipi == 'line':
        # Çizgi formatı: Önce Ad, sonra koordinat çiftleri (X,Y)
        aktif_cizgi = None
        cizgi_id = 1
        
        for i in range(2, len(satirlar)):
            satir_metni = satirlar[i]
            
            # İçinde virgül yoksa bu bir çizgi ismidir (örn: Ana yol)
            if ',' not in satir_metni:
                # Eğer halihazırda okuduğumuz bir çizgi varsa onu listeye ekle
                if aktif_cizgi is not None:
                    geometriler.append(aktif_cizgi)
                
                # Yeni bir çizgi nesnesi başlat
                aktif_cizgi = Line(cizgi_id, satir_metni)
                cizgi_id += 1
            else:
                # Virgül varsa koordinattır, aktif çizgiye ekle
                if aktif_cizgi is not None:
                    koordinatlar = satir_metni.split(',')
                    if len(koordinatlar) == 2:
                        aktif_cizgi.add_coordinate(koordinatlar[0], koordinatlar[1])
        
        # Dosya bittiğinde son kalan çizgiyi de listeye ekle
        if aktif_cizgi is not None:
            geometriler.append(aktif_cizgi)

    return geometriler


# Eğer bu dosya doğrudan çalıştırılırsa test etmek için:
if __name__ == "__main__":
    print("--- Geometri Modülü Testi ---")
    
    # Basit bir test: Point nesnesi oluşturma
    p1 = Point(1, 400500.5, 4423000.1, "Nirengi Noktası")
    print(p1)
    
    # Dosya okuma testleri (dosyalar aynı klasörde olmalı)
    # ornek_noktalar = dosyadan_oku('points2.txt')
    # for n in ornek_noktalar:
    #     print(n)