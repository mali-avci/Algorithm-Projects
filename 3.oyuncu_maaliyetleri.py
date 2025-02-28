"""Yaşı, son yıllık ücreti,takımının normal sezon sonundaki sırası ve takımı playoff sezonuna kalmışsa, playoff sezonunda oynadığı maç sayısı bilgilerini oyuncudan alan
ve turnuvada oynadığı maç başına takımına maliyetiyle, serbest kalma (takımından ayrılma) hakkı olup olmadığını, hakkı varsa serbest kalma  bedelini oyuncuya veren programdır."""
CIFT_DEVRE_MAC_SAYISI = 26  #turnuvada bir takımın oynadığı toplam maç sayısı.
yas = int(input("Yaşınızı giriniz:"))
son_yillik_ucret = int(input("Son yıllık ücretinizi giriniz (TL):"))
takiminin_normal_sezon_sirasi = int(input("Takımınızın normal sezon sonundaki sırasını giriniz:"))

if 0 < takiminin_normal_sezon_sirasi < 9:
    playoff_oynadigi_mac_sayisi = int(input("Takımınızın playoff sezonunda oynadığı maç sayısını giriniz:"))
    maliyet = son_yillik_ucret / (CIFT_DEVRE_MAC_SAYISI+playoff_oynadigi_mac_sayisi)
else:
    maliyet = son_yillik_ucret/CIFT_DEVRE_MAC_SAYISI
print(f"Oynadığınız maç başına takımınıza maliyetiniz: {maliyet:.2f} TL")
if yas == 22:
    serbest_bedeli = son_yillik_ucret*2
    print(f"Serbest kalma (takımınızdan ayrılma) hakkınız bulunmaktadır, serbest kalma bedeliniz: {serbest_bedeli:.2f} TL")
elif yas == 23:
    serbest_bedeli = son_yillik_ucret
    print(f"Serbest kalma (takımınızdan ayrılma) hakkınız bulunmaktadır, serbest kalma bedeliniz: {serbest_bedeli:.2f} TL")
elif yas == 24:
    serbest_bedeli = son_yillik_ucret/2
    print(f"Serbest kalma (takımınızdan ayrılma) hakkınız bulunmaktadır, serbest kalma bedeliniz: {serbest_bedeli:.2f} TL")
elif yas >= 25:
    serbest_bedeli = 0
    print(f"Serbest kalma (takımınızdan ayrılma) hakkınız bulunmaktadır, serbest kalma bedeliniz: {serbest_bedeli:.2f} TL")
else:
    serbest_bedeli = "Serbest kalma (takımınızdan ayrılma) hakkınız bulunmamaktadır."
    print(serbest_bedeli)