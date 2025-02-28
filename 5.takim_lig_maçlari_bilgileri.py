MAX_SET_SAYISI = 5
KAZANMA_SET_SAYISI = 3
kazandigi_set_sayisi = 0
kaybettigi_set_sayisi = 0
toplam_set_sayisi = 0
kazandigi_toplam_sayi = 0
kaybettigi_toplam_sayi = 0
sezon_toplam_sayisi = 0
kazandigi_mac_adedi = 0
kaybettigi_mac_adedi = 0
kaybetmeden_kazandigi_mac_sayisi = 0
bes_sette_biten_mac_sayisi = 0
en_yuksek_fark = 0
fark_rakip_ad = "a"
toplam_mac_adedi = int(input("Toplam maç adedini giriniz:"))
for i in range(1, toplam_mac_adedi+1):
    rakip_ad = input("Rakibinizin adını giriniz:")
    while toplam_set_sayisi <= MAX_SET_SAYISI:
        kazandigi_sayi_adedi = int(input("Takımınızın sette kazandığı sayı adedini giriniz:"))
        kaybettigi_sayi_adedi = int(input("Takımınızın sette kaybettiği sayı adedini giriniz:"))
        if kazandigi_sayi_adedi > kaybettigi_sayi_adedi:
            kazandigi_set_sayisi += 1
        else:
            kaybettigi_set_sayisi += 1
        toplam_set_sayisi = kazandigi_set_sayisi + kaybettigi_set_sayisi #Toplam set sayısı kazanılan ve kaybedilen setlerin toplamına eşittir.
        kazandigi_toplam_sayi += kazandigi_sayi_adedi
        kaybettigi_toplam_sayi += kaybettigi_sayi_adedi
        kazandigi_sayi_ort = kazandigi_toplam_sayi / toplam_set_sayisi
        kaybettigi_sayi_ort = kaybettigi_toplam_sayi / toplam_set_sayisi
        sezon_toplam_sayisi += kazandigi_sayi_adedi
        if kazandigi_set_sayisi == KAZANMA_SET_SAYISI or kaybettigi_set_sayisi == KAZANMA_SET_SAYISI: # or bağlacı iki koşuldan birinin doğru olması halinde True verilmesini sağlar.
            print(f" Takımınızın maçta kazandığı toplam sayi:{kazandigi_toplam_sayi}"
                  f"\n Takımınızın maçta kaybettiği toplam sayi:{kaybettigi_toplam_sayi}"
                  f"\n Takımınızın kazandığı toplam set adedi:{kazandigi_set_sayisi}"
                  f"\n Takımınızın kaybettiği toplam set adedi:{kaybettigi_set_sayisi}"
                  f"\n Takımınızın set başına kazandığı sayı ortalaması:{kazandigi_sayi_ort:.2f}"
                  f"\n Takımınızın set başına kaybettiği sayı ortalaması:{kaybettigi_sayi_ort:.2f}")
            if kazandigi_set_sayisi > kaybettigi_set_sayisi:
                kazandigi_mac_adedi += 1
                if kaybettigi_set_sayisi == 0:
                    kaybetmeden_kazandigi_mac_sayisi += 1
            else:
                kaybettigi_mac_adedi += 1
            if toplam_set_sayisi == MAX_SET_SAYISI:
                bes_sette_biten_mac_sayisi += 1
            if kazandigi_toplam_sayi > kaybettigi_toplam_sayi:
                fark = kazandigi_toplam_sayi - kaybettigi_toplam_sayi
            else:
                fark = kaybettigi_toplam_sayi - kazandigi_toplam_sayi
            if fark > en_yuksek_fark:
                en_yuksek_fark = fark
                fark_rakip_ad = rakip_ad
            kazandigi_set_sayisi = 0
            kaybettigi_set_sayisi = 0
            kazandigi_toplam_sayi = 0
            kaybettigi_toplam_sayi = 0
            break
print(f"Takımınızın sezon boyunca kazandığı toplam sayı adedi:{sezon_toplam_sayisi}")
print(f"Takımınızın maç başına kazandığı sayı ortalaması:{sezon_toplam_sayisi / toplam_mac_adedi:.2f}")
print(f"Takımınızın kazandığı maç adedi:{kazandigi_mac_adedi} "
      f"\nTakımınızın kaybettiği maç adedi:{kaybettigi_mac_adedi}")
print(f"Takımınızın set kaybetmeden kazandığı maçların adedi:{kaybetmeden_kazandigi_mac_sayisi}"
      f"\nTakımınızın set kaybetmeden kazandığı maçların tüm kazandığı maçlar içindeki oranı(%):"
      f"{kaybetmeden_kazandigi_mac_sayisi / kazandigi_mac_adedi * 100:.2f}%")
print(f"Takımınızın 5 sette biten maçların sayısı:{bes_sette_biten_mac_sayisi}"
      f"\nTakımınızın 5 sette biten maçların sayısının tüm maçlar içindeki oranı(%):"
      f"{bes_sette_biten_mac_sayisi / toplam_mac_adedi * 100:.2f}%")
print(f"Takımınızın kazandığı toplam sayı ile kaybettiği toplam sayı arasındaki farkın en yüksek olduğu maçtaki "
      f"\nkazandığı toplam sayı ile kaybettiği toplam sayı arasındaki fark:{en_yuksek_fark}"
      f"\nTakımınızın kazandığı toplam sayı ile kaybettiği toplam sayı arasındaki farkın en yüksek olduğu maçtaki"
      f"\nrakip takımın adı:{fark_rakip_ad}")