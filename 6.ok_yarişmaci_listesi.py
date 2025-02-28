# Bir ok yarışmasına dair bilgileri alıp bu bilgileri işleyip
# tablo oluşturarak kullanıcıya veren bu program Mehmet Ali AVCI tarafından yapılmıştır!
def kullanicidan_bilgi_al_ve_tablo_olustur():
    PUAN_SAY = 11
    MIN_SPORCU_SAY = 3

    try: # kullanıcıdan alınan sporcu sayısı için hata kontrolü.
        sporcu_say = int(input("Sporcu sayısını giriniz:"))

    except ValueError:
        sporcu_say = 0

    while sporcu_say < MIN_SPORCU_SAY:
        print("Lütfen tekrar deneyiniz! 9'dan büyük bir tam sayı giriniz!")

        try:
            sporcu_say = int(input("Sporcu sayısını giriniz:"))

        except ValueError:
            print("Hatalı giriş!")

    try: # kullanıcıdan alınan atış sayısı için hata kontrolü.
        atis_say = int(input("Tüm sporcular için verilen atış hakkını giriniz:"))

    except ValueError:
        atis_say = 0

    while atis_say < 1:
        print("Lütfen tekrar deneyiniz.Pozitif bir tam sayı giriniz!")

        try:
            atis_say = int(input("Tüm sporcular için verilen atış hakkını giriniz:"))

        except ValueError:
            print("Hatalı giriş!")

    sporcu_liste = []
    toplam_puan = []
    puan_sayilari_toplami =[]
    toplam_iska = 0
    ruzgarlar = {"Yıldız": 0, "Poyraz": 0, "Gündoğusu": 0, "Keşişleme": 0,
                 "Kıble": 0, "Lodos": 0, "Günbatısı": 0, "Karayel": 0}

    for sporcu_no in range(sporcu_say):
        puanlar = [0] * PUAN_SAY
        sporcu_liste.append(puanlar)

    for i in range(atis_say):
        toplam_puan = [0] * sporcu_say
        puan_sayilari_toplami = [0] * PUAN_SAY

        for sporcu_no in range(sporcu_say):
            try: # kullanıcıdan alınan puan için hata kontrolü.
                puan = int(input(f"{sporcu_no + 1}. sporcunun {i + 1}. atıştaki puanını giriniz:"))

            except ValueError:
                puan = -1

            while puan < 0:
                print("Lütfen tekrar deneyiniz! 0'dan 10'a kadar (10 dahil) bir sayı giriniz!")

                try:
                    puan = int(input(f"{sporcu_no + 1}. sporcunun {i + 1}. atıştaki puanını giriniz:"))

                except ValueError:
                    print("Hatalı giriş!")
            sporcu_liste[sporcu_no][puan] += 1 # listedeki uygun indeksteki adedi 1 artırır.

            if puan == 0:
                try:  # kullanıcıdan alınan rüzgar adı için hata kontrolü.
                    ruzgar_adi = input("esen rüzgarın adını giriniz:")

                except KeyError:
                    ruzgar_adi = ""

                while not ruzgar_adi in ruzgarlar:
                    print("Lütfen tekrar deneyiniz! Rüzgar adını ilk harfi büyük olacak şekilde giriniz!")

                    try:
                        ruzgar_adi = input("esen rüzgarın adını giriniz:")

                    except KeyError:
                        print("Hatalı giriş!")

                toplam_iska += 1
                ruzgarlar[ruzgar_adi] += 1

            for j in range(PUAN_SAY):
                toplam_puan[sporcu_no] += sporcu_liste[sporcu_no][j] * j # her sporcunun toplam puanı toplam puan listesine eklenir.

        for idx in range(PUAN_SAY):
            for sporcu_no in range(sporcu_say):
                puan_sayilari_toplami[idx] += sporcu_liste[sporcu_no][idx] # her puanın sayılarının toplamı puan sayıları toplamı listesine eklenir.

    print("Okçu Kayıt No", "   0p  ", "   1p  ", "   2p  ", "   3p  ", "   4p  ", "   5p  ", "   6p  ",
          "   7p  ", "   8p  ", "   9p  ", "   10p  ", "Toplam Puan")
    print("-------------", "-------", "-------", "-------", "-------", "-------", "-------", "-------",
          "-------", "-------", "-------", "--------", "-----------")

    for sporcu_no in range(sporcu_say):
        print(f"{sporcu_no+1:12}", end="")

        for i in range(PUAN_SAY):
            print(f"{sporcu_liste[sporcu_no][i]:8}", end="")
        print(f"{toplam_puan[sporcu_no]:10}")
    print("Tüm Okçular(%)", end="")

    for j in range(PUAN_SAY):
        yuzde = puan_sayilari_toplami[j] / sum(puan_sayilari_toplami) * 100
        print(f"{yuzde:8.2f}", end="")

    print()
    print("Rüzgar Adı", "     Iska Atış Oranı(%)")
    print("----------", "     ------------------")

    for a, b in ruzgarlar.items():
        print(f"{a:10}", f"{b / toplam_iska * 100:15.2f}")

def main():
    kullanicidan_bilgi_al_ve_tablo_olustur()

main()