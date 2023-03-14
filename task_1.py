#String ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine
#space koyunuz, kelime kelime ayırınız.

#VERİLEN TEXT
#text = "The goal is to turn data into information, and information into insight.

#BEKLENEN ÇIKTI
#["THE", "GOAL", "IS", "TO", "TURN", "DATA","INTO","INFORMATION","AND","INFORMATION","INTO","INSIGHT"]

text = "The goal is to turn data into information,and information into insight."
result = []
#büyük harfe çevirmek
text = text.upper()
#virgül ve nokta yerine boşluk koymak
text = text.replace(',', '')
text = text.replace('.', '')
#boşluklara göre kelime kelime ayırmak ve bunu bir dizi haline getirmek
result = text.split(" ")
#sonucun görüntülenmesi
print(result)
