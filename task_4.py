#Argüman alarak bir liste alan, liste içerisindeki tek ve çift sayıları ayrı listeye atayan
# ve bu listeleri return eden fonksiyon yazınız.

def func(list):
    even_list = []
    odd_list = []
    for value in list:
        if value % 2 == 0:
            even_list.append(value)
        else:
            odd_list.append(value)
    return even_list, odd_list

a = [1,2,3,4,5,6,7,8,9]
func(a)
