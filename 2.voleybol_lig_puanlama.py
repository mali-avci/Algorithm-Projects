takim_ad = input("İlk takımın adını giriniz:")
ilk_takim_kazandigi_set = int(input("İlk takımın kazandığı set adedini giriniz:"))
takim_ad_2 = input("İkinci takımın adını giriniz:")
ikinci_takim_kazandigi_set = int(input("İkinci takımın kazandığı set adedini giriniz:"))

kazanan_takim = 3
kaybeden_takim = 0
kazanan_takim2 = 2
kaybeden_takim2 = 1
""" 
if (ilk_takim_kazandigi_set-ikinci_takim_kazandigi_set) >= 2:
   print(f"Maçı kazanan takımın adı:{takim_ad}, kazandığı puan: {kazanan_takim} ")
   print(f"Maçı kaybeden takımın adı: {takim_ad_2}, kazandığı puan: {kaybeden_takim}")
if (ilk_takim_kazandigi_set-ikinci_takim_kazandigi_set) <= (-2):
    print(f"Maçı kazanan takımın adı:{takim_ad_2}, kazandığı puan: {kazanan_takim} ")
    print(f"Maçı kaybeden takımın adı: {takim_ad}, kazandığı puan: {kaybeden_takim}")
if (ilk_takim_kazandigi_set-ikinci_takim_kazandigi_set) == 1:
    print(f"Maçı kazanan takımın adı:{takim_ad}, kazandığı puan: {kazanan_takim2} ")
    print(f"Maçı kaybeden takımın adı: {takim_ad_2}, kazandığı puan: {kaybeden_takim2}")
if (ilk_takim_kazandigi_set-ikinci_takim_kazandigi_set) == -1:
    print(f"Maçı kazanan takımın adı:{takim_ad_2}, kazandığı puan: {kazanan_takim2} ")
    print(f"Maçı kaybeden takımın adı: {takim_ad}, kazandığı puan: {kaybeden_takim2}") 
"""
if (ilk_takim_kazandigi_set > ikinci_takim_kazandigi_set):
    kazanan = takim_ad
    kaybeden = takim_ad_2
else:
    kazanan = takim_ad_2
    kaybeden = takim_ad
if (ilk_takim_kazandigi_set-ikinci_takim_kazandigi_set) == (1 or -1):
    kazananin_puani = kazanan_takim2
    kaybedenin_puani = kaybeden_takim2
else:
    kazananin_puani = kazanan_takim
    kaybedenin_puani = kaybeden_takim

print(f"Maçı kazanan takımın adı:{kazanan}, kazandığı puan: {kazananin_puani} ")
print(f"Maçı kaybeden takımın adı: {kaybeden}, kazandığı puan: {kaybedenin_puani}")
