ogr_no = int(input("Örenci numaranızı giriniz:"))
ad_soyad = input("Adınızı ve soyadınızı giriniz:")
teorik_saat = int(input("Aldığınız ilk dersin haftalık teorik ders saatini giriniz:"))
uygulama_saat = int(input("Aldığınız ilk dersin haftalık uygulama ders saatini giriniz:"))
akts = float(input("Aldığınız ilk dersin haftalık AKTS kredisini giriniz:"))
donem_sonu_not = float(input("Aldığınız ilk dersin dönem sonu notunu giriniz:"))


teorik_saat2 = int(input("Aldığınız ikinci dersin haftalık teorik ders saatini giriniz:"))
uygulama_saat2 = int(input("Aldığınız ikinci dersin haftalık uygulama ders saatini giriniz:"))
akts2 = float(input("Aldığınız ikinci dersin haftalık AKTS kredisini giriniz:"))
donem_sonu_not2 = float(input("Aldığınız ikinci dersin dönem sonu notunu giriniz:"))


yerel_kredi1 = float(teorik_saat+(uygulama_saat/2))
yerel_kredi2 = float(teorik_saat2 +(uygulama_saat2/2))
AGNO_yerel = float(((donem_sonu_not*yerel_kredi1)+(donem_sonu_not2*yerel_kredi2))/(yerel_kredi1+yerel_kredi2))
AGNO_akts = float(((donem_sonu_not*akts)+(donem_sonu_not2*akts2))/(akts+akts2))

print(f"Öğrenci numarası: {ogr_no}")
print(f"Adı ve soyadı: {ad_soyad}")
print(f"Bu dönem aldığı toplam yerel kredi miktarı: {yerel_kredi1+yerel_kredi2:.2f}")
print(f"Bu dönem aldığı toplam AKTS kredi miktarı: {akts+akts2:.2f}")
print(f"Yerel krediye göre bu dönem sonu AGNO: {AGNO_yerel:.2f}")
print(f"AKTS’ye göre bu dönem sonu AGNO: {AGNO_akts:.2f}")