#Listede mühendislik ve tıp fakültelerinde dereceye giren öğrencilerin isimleri bulunmaktadır.
#İlk 3 öğrenci mühendislik, son 3 öğrenci de tıp fakültesi öğrencisidir.
#Öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, value in enumerate(ogrenciler):
    if index < 3:
        print("Mühendislik fakültesi {0}. öğrenci: {1}:".format(index,value))
    else:
        print("Tıp fakültesi {0}. öğrenci: {1}".format(index, value))