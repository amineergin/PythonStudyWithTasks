#VERİLEN LİSTE
# lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: listenin eleman sayısına bakınız.
# Adım 2: Sıfırıncı ve onuncu indksteki elemanları çağırınız.
# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturunuz.
# Adım 4: Sekizinci indeksteki elemanı siliniz.
# Adım 5: Yeni bir eleman ekleyiniz.
# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst = ["D","A","T","A","S","C","I","E","N","C","E"]
print("The number of elements in the list :", len(lst))
print("*************************************")
print("0 the element in the index :", lst[0], "\nand 10th the element in the index :", lst[10])
print("*************************************")
print("Result of task 3 :", lst[0:4])
print("*************************************")
lst.pop(8)
print("Without element in 8th index",lst)
print("*************************************")
lst.append("E")
print("List with new element :", lst)
print("*************************************")
lst.insert(8,"N")
print("Result of every task :",lst)