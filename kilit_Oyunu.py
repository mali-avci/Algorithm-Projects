def main():
    index_dict = {}  # boş dict
    devam = "e"
    while True:
        try:
            oyuncu1_fake_simgesi = input("1. oyuncuyu temsil edecek simgeyi giriniz: ")
            oyuncu1_simgesi = oyuncu1_fake_simgesi.upper()
            while len(oyuncu1_simgesi) != 1 or oyuncu1_simgesi == " ":  # OYUNCU 1
                print("Hatalı giriş yaptınız! Lütfen tek karakter giriniz.")
                oyuncu1_fake_simgesi = input("1. oyuncuyu temsil edecek simgeyi giriniz: ")
                oyuncu1_simgesi = oyuncu1_fake_simgesi.upper()
        except ValueError:
            print("hatalı giriş yaptınız! Lütfen tekrar deneyiniz.")
        else:
            break
    while True:
        try:
            oyuncu2_fake_simgesi = input("2. oyuncuyu temsil edecek simgeyi giriniz: ")
            oyuncu2_simgesi = oyuncu2_fake_simgesi.upper()
            while len(oyuncu2_simgesi) != 1 or oyuncu2_simgesi == " " or oyuncu2_simgesi == oyuncu1_simgesi:  # OYUNCU 2
                print("Hatalı giriş yaptınız! Lütfen tek karakter giriniz veya 1. oyuncuyla aynı simgeyi girmeyiniz.")
                oyuncu2_fake_simgesi = input("2. oyuncuyu temsil edecek simgeyi giriniz: ")
                oyuncu2_simgesi = oyuncu2_fake_simgesi.upper()
        except ValueError:
            print("Hatalı giriş yaptınız!")
        else:
            break
    while devam == "e" or devam == "E":
        while True:
            try:
                tablo_buyuklugu = int(input("Oyun alanının satır/sütun sayısını giriniz(4-8): "))
                while tablo_buyuklugu < 4 or tablo_buyuklugu > 8:  # TABLO BUYUKLUGU
                    print("Hatalı girdi! Lütfen 4 ile 8 arasında bir sayı giriniz.")
                    tablo_buyuklugu = int(input("Oyun alanının satır/sütun sayısını giriniz(4-8): "))
            except ValueError:
                print("Yabancı karakter girdiniz! Lütfen 4 ile 8 arasında bir sayı giriniz.")
            else:
                break
        harf_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
        tablo_list = []
        eleman_list = [" "] * tablo_buyuklugu

        for i in range(tablo_buyuklugu):  # boş dictionary'i burada tablo büyüklüğüne göre oluştur.
            for j in range(tablo_buyuklugu):
                index_dict[f"{j + 1}{harf_list[i]}"] = [i, j]  # örn key-value = '1A': [0,0], '2C': [2,1] gibi..

        oyuncu1_sayaci = tablo_buyuklugu  # sayaçlar tablo büyüklüğünden başlat 2 den az kaldığında oyunu bitir.
        oyuncu2_sayaci = tablo_buyuklugu
        oyun_sira_sayaci = 0
        for i in range(tablo_buyuklugu):
            tablo_list.append(eleman_list.copy())

        for j in range(tablo_buyuklugu):  # taşların oyun dizimi
            for k in range(tablo_buyuklugu):
                if (k == 0):
                    tablo_list[j][k] = f"{oyuncu2_simgesi}"
                elif (k == tablo_buyuklugu - 1):
                    tablo_list[j][k] = f"{oyuncu1_simgesi}"
                else:
                    tablo_list[j][k] = " "
        tablo_ciz(tablo_list=tablo_list, tablo_buyuklugu=tablo_buyuklugu, harf_list=harf_list)
        while oyuncu1_sayaci > 1 and oyuncu2_sayaci > 1:  # iki simgeden birinin 1 taşı kalana kadar devam et.
            if (oyun_sira_sayaci == 0):
                hamle1 = str(input(
                    "1. oyuncu lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: "))
                hamle = hamle1.upper()
                oyun_sira_sayaci += 1
            else:
                hamle1 = str(input(
                    "2. oyuncu lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: "))
                hamle = hamle1.upper()
                oyun_sira_sayaci -= 1

            # kuralları kontrol ettirip kurallardan herhangi biri tutmassa false döndür.
            kural1 = kural_kontrol(index_dict=index_dict, tablo_list=tablo_list, hamle=hamle,
                                   oyuncu1_simgesi=oyuncu1_simgesi, \
                                   oyuncu2_simgesi=oyuncu2_simgesi, tablo_buyuklugu=tablo_buyuklugu,
                                   oyun_sira_sayaci=oyun_sira_sayaci)
            if (kural1 == False):
                if (oyun_sira_sayaci == 0):
                    oyun_sira_sayaci += 1
                else:
                    oyun_sira_sayaci -= 1

            while (kural1 == False):  # hatalı hamle yapıldığında tekrar oynaması gerekir.

                if (oyun_sira_sayaci == 0):
                    print("Hatalı hamle! Lütfen tekrar deneyiniz.")
                    hamle1 = str(input(
                        "1. oyuncu lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: "))
                    hamle = hamle1.upper()
                    oyun_sira_sayaci += 1
                else:
                    print("Hatalı hamle! Lütfen tekrar deneyiniz.")
                    hamle1 = str(input(
                        "2. oyuncu lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: "))
                    hamle = hamle1.upper()
                    oyun_sira_sayaci -= 1
                kural1 = kural_kontrol(index_dict=index_dict, tablo_list=tablo_list, hamle=hamle,
                                       oyuncu1_simgesi=oyuncu1_simgesi, \
                                       oyuncu2_simgesi=oyuncu2_simgesi, tablo_buyuklugu=tablo_buyuklugu,
                                       oyun_sira_sayaci=oyun_sira_sayaci)
                if (kural1 == False):
                    if (oyun_sira_sayaci == 0):
                        oyun_sira_sayaci += 1
                    else:
                        oyun_sira_sayaci -= 1
            for i in range(tablo_buyuklugu - 2):  # yatay 3lük kontrol
                for j in range(tablo_buyuklugu):
                    if (oyun_sira_sayaci == 1):
                        if (tablo_list[i][j] == f"{oyuncu1_simgesi}"):
                            if (tablo_list[i + 1][j] == f"{oyuncu2_simgesi}") and (
                                    tablo_list[i + 2][j] == f"{oyuncu1_simgesi}"):
                                tablo_list[i + 1][j] = " "
                                print(f"{j + 1}{harf_list[i + 1]} konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                                oyuncu2_sayaci -= 1
                    if (oyun_sira_sayaci == 0):
                        if (tablo_list[i][j] == f"{oyuncu2_simgesi}"):
                            if (tablo_list[i + 1][j] == f"{oyuncu1_simgesi}") and (
                                    tablo_list[i + 2][j] == f"{oyuncu2_simgesi}"):
                                tablo_list[i + 1][j] = " "
                                print(f"{j + 1}{harf_list[i + 1]} konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                                oyuncu1_sayaci -= 1

            for i in range(tablo_buyuklugu - 2):  # dikey 3lük kontrol
                for j in range(tablo_buyuklugu):
                    if (oyun_sira_sayaci == 1):
                        if (tablo_list[j][i] == f"{oyuncu1_simgesi}"):
                            if (tablo_list[j][i + 1] == f"{oyuncu2_simgesi}") and (
                                    tablo_list[j][i + 2] == f"{oyuncu1_simgesi}"):
                                tablo_list[j][i + 1] = " "
                                print(f"{i + 2}{harf_list[j]} konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                                oyuncu2_sayaci -= 1
                    if (oyun_sira_sayaci == 0):
                        if (tablo_list[j][i] == f"{oyuncu2_simgesi}"):
                            if (tablo_list[j][i + 1] == f"{oyuncu1_simgesi}") and (
                                    tablo_list[j][i + 2] == f"{oyuncu2_simgesi}"):
                                tablo_list[j][i + 1] = " "
                                print(f"{i + 2}{harf_list[j]} konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                                oyuncu1_sayaci -= 1

            if (oyun_sira_sayaci == 0):
                if (tablo_list[0][0] == f"{oyuncu1_simgesi}"):  # OYUNCU1
                    if (tablo_list[1][0] == f"{oyuncu2_simgesi}" and tablo_list[0][1] == f"{oyuncu2_simgesi}"):
                        tablo_list[0][0] = " "
                        print(f"1A konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                        oyuncu1_sayaci -= 1

                if (tablo_list[tablo_buyuklugu - 1][tablo_buyuklugu - 1] == f"{oyuncu1_simgesi}"):  # OYUNCU1
                    if (tablo_list[tablo_buyuklugu - 2][tablo_buyuklugu - 1] == f"{oyuncu2_simgesi}" \
                            and tablo_list[tablo_buyuklugu - 1][tablo_buyuklugu - 2] == f"{oyuncu2_simgesi}"):
                        tablo_list[tablo_buyuklugu - 1][tablo_buyuklugu - 1] = " "
                        print(
                            f"{tablo_buyuklugu}{harf_list[tablo_buyuklugu - 1]} konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                        oyuncu1_sayaci -= 1

                if (tablo_list[tablo_buyuklugu - 1][0] == f"{oyuncu1_simgesi}"):  # OYUNCU1
                    if (tablo_list[tablo_buyuklugu - 2][0] == f"{oyuncu2_simgesi}" and tablo_list[tablo_buyuklugu - 1][
                        1] == f"{oyuncu2_simgesi}"):
                        tablo_list[tablo_buyuklugu - 1][0] = " "
                        print(f"1{harf_list[tablo_buyuklugu - 1]} konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                        oyuncu1_sayaci -= 1

                if (tablo_list[0][tablo_buyuklugu - 1] == f"{oyuncu1_simgesi}"):  # OYUNCU1
                    if (tablo_list[0][tablo_buyuklugu - 2] == f"{oyuncu2_simgesi}" \
                            and tablo_list[1][tablo_buyuklugu - 1] == f"{oyuncu2_simgesi}"):
                        tablo_list[0][tablo_buyuklugu - 1] = " "
                        print(f"{tablo_buyuklugu}A konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                        oyuncu1_sayaci -= 1
            if (oyun_sira_sayaci == 1):
                if (tablo_list[0][0] == f"{oyuncu2_simgesi}"):  # OYUNCU2
                    if (tablo_list[1][0] == f"{oyuncu1_simgesi}" and tablo_list[0][1] == f"{oyuncu1_simgesi}"):
                        tablo_list[0][0] = " "
                        print(f"1A konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                        oyuncu2_sayaci -= 1

                if (tablo_list[0][tablo_buyuklugu - 1] == f"{oyuncu2_simgesi}"):  # OYUNCU2
                    if (tablo_list[0][tablo_buyuklugu - 2] == f"{oyuncu1_simgesi}" \
                            and tablo_list[1][tablo_buyuklugu - 1] == f"{oyuncu1_simgesi}"):
                        tablo_list[0][tablo_buyuklugu - 1] = " "
                        print(f"{tablo_buyuklugu}A konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                        oyuncu2_sayaci -= 1

                if (tablo_list[tablo_buyuklugu - 1][0] == f"{oyuncu2_simgesi}"):  # OYUNCU2
                    if (tablo_list[tablo_buyuklugu - 2][0] == f"{oyuncu1_simgesi}" and tablo_list[tablo_buyuklugu - 1][
                        1] == f"{oyuncu1_simgesi}"):
                        tablo_list[tablo_buyuklugu - 1][0] = " "
                        print(f"1{harf_list[tablo_buyuklugu - 1]} konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                        oyuncu2_sayaci -= 1

                if (tablo_list[tablo_buyuklugu - 1][tablo_buyuklugu - 1] == f"{oyuncu2_simgesi}"):  # OYUNCU2
                    if (tablo_list[tablo_buyuklugu - 2][tablo_buyuklugu - 1] == f"{oyuncu1_simgesi}" \
                            and tablo_list[tablo_buyuklugu - 1][tablo_buyuklugu - 2] == f"{oyuncu1_simgesi}"):
                        tablo_list[tablo_buyuklugu - 1][tablo_buyuklugu - 1] = " "
                        print(
                            f"{tablo_buyuklugu}{harf_list[tablo_buyuklugu - 1]} konumundaki taş kilitlendi ve dışarı çıkarıldı.")
                        oyuncu2_sayaci -= 1

            tablo_ciz(tablo_list, tablo_buyuklugu, harf_list)
        if (oyuncu1_sayaci == 1):
            print(f"OYUNCU {oyuncu2_simgesi} KAZANDI!")
        else:
            print(f"OYUNCU {oyuncu1_simgesi} KAZANDI!")
        while True:
            try:
                devam = input("Tekrar oynamak istiyor musunuz?[e/E/h/H]")
                while (devam not in ["e", "E", "H", "h"]):
                    print("yalnızca e ve h harfleri kullanılmalıdır.")
                    devam = input("Tekrar oynamak istiyor musunuz?[e/E/h/H]")
            except ValueError:
                print("Hatalı girdi!")
            else:
                break


def tablo_ciz(tablo_list, tablo_buyuklugu, harf_list):  # tabloyu çizdirme işlevi
    print("     ", end="")
    for i in range(tablo_buyuklugu):
        print(harf_list[i], end="    ")
    print()
    print("   ", end="")
    for j in range(tablo_buyuklugu):
        print("-----", end="")
    print()
    for sutun in range(tablo_buyuklugu):
        print(f"{sutun + 1}  | ", end="")
        for satir in range(tablo_buyuklugu):
            print(tablo_list[satir][sutun], end="  | ")
        print(f"{sutun + 1}", end="")
        print()
        print("   ", end="")
        print("-----" * tablo_buyuklugu)
    print("     ", end="")
    for i in range(tablo_buyuklugu):
        print(harf_list[i], end="    ")
    print()


def kural_kontrol(index_dict, tablo_list, hamle, oyuncu1_simgesi, oyuncu2_simgesi, tablo_buyuklugu, oyun_sira_sayaci):
    # bu fonksiyon hatalı hamle yapıldığında false döndürecek şekilde ayarlandı.

    ilk_konum = hamle[:2]  # girdiden istenileni slicing ile çek
    hedef_konum = hamle[3:]  # girdiden hedefi slicing ile çek
    while True:
        try:
            ilk_konum_valuesi = index_dict[f'{ilk_konum}'[:]]  # dict value'sunu değiştirebilmek için kopyasını al
            hedef_konum_valuesi = index_dict[f'{hedef_konum}'[:]]  # dict value'sunu değiştirebilmek için kopyasını al

        except KeyError:  # eğer oluşturulan key ler dışında bir değer bulunursa exception fırlatır.
            print(
                "Yanlış veya hatalı giriş yaptınız! Lütfen (1A 3A) formatında veya tablo sınırları içinde tekrar deneyiniz.")
            if (oyun_sira_sayaci == 1):
                hamle1 = str(input(
                    "1. oyuncu lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: "))
                hamle = hamle1.upper()
            else:
                hamle1 = str(input(
                    "2. oyuncu lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: "))
                hamle = hamle1.upper()
            ilk_konum = hamle[:2]  # girdiden istenileni slicing ile çek
            hedef_konum = hamle[3:]  # girdiden hedefi slicing ile çek
        else:
            break

    ilk_satir_index1 = ilk_konum_valuesi[
        0]  # dictionaryden seçilen key'in değerlerini al. örn. 2C: [2,1] --> 0. index elemanı 2
    ilk_satir_index2 = ilk_konum_valuesi[1]  # 1. index

    hedef_satir_index1 = hedef_konum_valuesi[0]  # hedef 0. index
    hedef_satir_index2 = hedef_konum_valuesi[1]  # hedef 1. index

    degisecek_tas1 = tablo_list[ilk_satir_index1][ilk_satir_index2]
    degisecek_tas2 = tablo_list[hedef_satir_index1][hedef_satir_index2]

    if (degisecek_tas1 == " "):  # taş olmayan yer oynanılamaz.
        print("Seçtiğiniz konumda taşınız bulunmuyor!")
        return False

    if (oyun_sira_sayaci == 1):
        if (degisecek_tas1 != f"{oyuncu1_simgesi}"):  # kural > kendi taşlarını oynayabilirsin.
            print("Sadece kendi taşlarınızı oynatabilirsiniz!")
            return False
    else:
        if (degisecek_tas1 != f"{oyuncu2_simgesi}"):  # kural > kendi taşlarını oynayabilirsin.
            print("Sadece kendi taşlarınızı oynatabilirsiniz!")
            return False

    if (degisecek_tas1 == oyuncu1_simgesi and degisecek_tas2 == oyuncu2_simgesi) or \
            (degisecek_tas2 == oyuncu1_simgesi and degisecek_tas1 == oyuncu2_simgesi):  # kural > taş üst üste gelemez.
        print("Oynamak istediğiniz hedefte başka bir taş bulunuyor!")
        return False

    if (degisecek_tas1 == oyuncu1_simgesi and degisecek_tas2 == oyuncu1_simgesi) or \
            (
                    degisecek_tas1 == oyuncu2_simgesi and degisecek_tas2 == oyuncu2_simgesi):  # kural > aynı olan taşlar yer değiştiremez.
        print("Hedefteki taş size ait!")
        return False

    ilk_konum_sayisi = ilk_konum[0]
    ilk_konum_harfi = ilk_konum[1]

    hedef_konum_sayisi = hedef_konum[0]
    hedef_konum_harfi = hedef_konum[1]

    if (ilk_konum_sayisi != hedef_konum_sayisi):  # KURAL > sadece düz ilerle.
        if (ilk_konum_harfi != hedef_konum_harfi):
            print("Sadece yatay ve dikey olarak ilerleyebilirsiniz!")
            return False

    if (ilk_satir_index2 < hedef_satir_index2):
        for i in range(1, (tablo_buyuklugu - ilk_satir_index2 - 1)):
            if (tablo_list[ilk_satir_index1][i + ilk_satir_index2] == f"{oyuncu1_simgesi}" or \
                    tablo_list[ilk_satir_index1][i + ilk_satir_index2] == f"{oyuncu2_simgesi}"):
                alt_index2_siniri = i + ilk_satir_index2
                break
        else:
            alt_index2_siniri = hedef_satir_index2
        if (hedef_satir_index2 > alt_index2_siniri):  # sınırdan büyük olmamalı.
            print("Taşınız başka bir taşın üzerinden atlayamaz!")
            return False

    if (ilk_satir_index2 > hedef_satir_index2):
        for j in range(1, (ilk_satir_index2) + 1):
            if (tablo_list[ilk_satir_index1][ilk_satir_index2 - j] == f"{oyuncu1_simgesi}" or \
                    tablo_list[ilk_satir_index1][ilk_satir_index2 - j] == f"{oyuncu2_simgesi}"):
                ust_index2_siniri = ilk_satir_index2 - j
                break
        else:
            ust_index2_siniri = hedef_satir_index2

        if (hedef_satir_index2 < ust_index2_siniri):  # sınırdan büyük olmamalı.
            print("Taşınız başka bir taşın üzerinden atlayamaz!")
            return False

    if (ilk_satir_index1 < hedef_satir_index1):
        for k in range(1, (tablo_buyuklugu - ilk_satir_index1 - 1)):
            if (tablo_list[ilk_satir_index1 + k][ilk_satir_index2] == f"{oyuncu1_simgesi}" or \
                    tablo_list[ilk_satir_index1 + k][ilk_satir_index2] == f"{oyuncu2_simgesi}"):
                sag_index1_siniri = k + ilk_satir_index1
                break
        else:
            sag_index1_siniri = hedef_satir_index1

        if (hedef_satir_index1 > sag_index1_siniri):  # sınırdan büyük olmamalı.
            print("Taşınız başka bir taşın üzerinden atlayamaz!")
            return False

    if (ilk_satir_index1 > hedef_satir_index1):
        for k in range(1, ilk_satir_index1 + 1):
            if (tablo_list[ilk_satir_index1 - k][ilk_satir_index2] == f"{oyuncu1_simgesi}" or \
                    tablo_list[ilk_satir_index1 - k][ilk_satir_index2] == f"{oyuncu2_simgesi}"):
                sol_index1_siniri = ilk_satir_index1 - k
                break
        else:
            sol_index1_siniri = hedef_satir_index1
        if (hedef_satir_index1 < sol_index1_siniri):  # sınırdan büyük olmamalı.
            print("Taşınız başka bir taşın üzerinden atlayamaz!")
            return False

    tablo_list[ilk_satir_index1][ilk_satir_index2], tablo_list[hedef_satir_index1][hedef_satir_index2] = \
        tablo_list[hedef_satir_index1][hedef_satir_index2], tablo_list[ilk_satir_index1][
            ilk_satir_index2]  # yer değiştir.


main()