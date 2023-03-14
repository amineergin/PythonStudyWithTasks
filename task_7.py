# 2 adet set verilmiştir. Sizden istenilen eğer 1.küme 2.kümeyi kapsıyorsa ortak elemanlarını,
# kapsamıyorsa 2.kümenin 1.kümeden farkını yazdıracak fonksiyonu tanımlayınız.

kume1 = set(["data", "python"])
kume2 = set(["data","function","qcut","lambda","python","miuul"])

#issubset fonksiyonu bir kümenin başka bir kümenin alt kümesi olup olmadığını sorgulayan metotdur.
#instersection fonksiyonu kümelerin kesişen elemanlarına sahip bir set döndürür.

def func(kume1, kume2):
    if kume1.issubset(kume2):
        return kume1.intersection(kume2)
    else:
        return kume2.difference(kume1)

func(kume1,kume2)