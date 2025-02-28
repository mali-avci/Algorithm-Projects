#Bir emlak acentesinin sayısı bilinmeyen satış temsilcilerinin brüt maaş tutarlarını kullanıcıdan alan ve her satış temsilcisi için istenilen birtakım bilgileri veren programdır

DUSUK_VERGI_ORANI = 0.15   #maaşı 10000 ve altında olanlara uygulanan vergi oranı
ORTA_VERGI_ORANI = 0.20   #maaşı 10000den büyük 25000den büyük olanlara uygulanan vergi oranı
YUKSEK_VERGI_ORANI = 0.25   #maaşı 25000den büyük olanlara uygulanan vergi oranı
dusuk_temsilci_sayisi = 0
orta_temsilci_sayisi = 0
yuksek_temsilci_sayisi = 0
toplam_temsilci_sayisi = 0
toplam_brut_maas = 0
toplam_gelir_vergisi = 0
toplam_net_maas = toplam_brut_maas - toplam_gelir_vergisi
brut_maas_50k_ust_temsilci_sayisi = 0 #brüt maaşı 50000'den fazla olan temsilci sayısını ifade eder.
brut_maas = int(input("brüt maaş miktarınızı giriniz:"))
while brut_maas > 0:

    if brut_maas <= 10000:
        gelir_vergisi = brut_maas * DUSUK_VERGI_ORANI
        net_maas = brut_maas - gelir_vergisi
        dusuk_temsilci_sayisi += 1

    elif 10000 < brut_maas < 25000:
        gelir_vergisi = brut_maas * ORTA_VERGI_ORANI
        net_maas = brut_maas - gelir_vergisi
        orta_temsilci_sayisi += 1
    else:
        gelir_vergisi = brut_maas * YUKSEK_VERGI_ORANI
        net_maas = brut_maas - gelir_vergisi
        yuksek_temsilci_sayisi += 1
        if brut_maas > 50000:
            brut_maas_50k_ust_temsilci_sayisi += 1
    print(f"devlete ödenecek gelir vergisi tutarı:{gelir_vergisi:.2f}")
    print(f"satış temsilcisine ödenecek net maaş tutarı:{net_maas:.2f}")
    toplam_gelir_vergisi += gelir_vergisi
    toplam_net_maas += net_maas
    toplam_brut_maas += brut_maas
    toplam_temsilci_sayisi = dusuk_temsilci_sayisi + orta_temsilci_sayisi + yuksek_temsilci_sayisi
    brut_maas = int(input("brüt maaş miktarınızı giriniz:"))
print(f"brüt maaş seviyesi düşük olan satış temsilcisi sayısı:{dusuk_temsilci_sayisi}"
      f"\nbrüt maaş seviyesi orta olan satış temsilcisi sayısı:{orta_temsilci_sayisi}"
      f"\nbrüt maaş seviyesi yüksek olan satış temsilcisi sayısı:{yuksek_temsilci_sayisi} ")
print(f"brüt maaş tutarı 50000 TL’den çok olan satış temsilcilerinin brüt maaş seviyesi yüksek olan satış temsilcileri içindeki yüzdesi:{brut_maas_50k_ust_temsilci_sayisi / yuksek_temsilci_sayisi * 100:.2f}%")
print(f"tüm satış temsilcilerinin net maaş tutarı ortalaması: {toplam_net_maas / toplam_temsilci_sayisi:.2f} TL")
print(f"devlete ödenecek toplam gelir vergisi tutarı:{toplam_gelir_vergisi:.2f} TL")
print(f"devlete ödenecek toplam gelir vergisi tutarı ve bu tutarın toplam brüt maaşı tutarı içindeki yüzdesi:{toplam_gelir_vergisi / toplam_brut_maas * 100:.2f}%")