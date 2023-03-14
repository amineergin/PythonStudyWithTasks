#Verilen sözlük yapısı
# dct = {"Christian" : ["America",18],
#        "Daisy" : ["England",12],
#        "Antonio" : ["Spain",22],
#        "Dante" : ["Italy",25]}
#
# Adım 1: Key değerlerine erişiniz.
# Adım 2: Valuelara erişiniz.
# Adım 3: Daisy keyine ait 12 değerini 13 olarak güncelleyiniz.
# Adım 4: Key değeri Ahmet value değeri [Turkey, 24] olan yeni bir değer ekleyiniz.
# Adım 5: Antonio' dictionary'den siliniz.

dct = {"Christian" : ["America",18],
       "Daisy" : ["England",12],
       "Antonio" : ["Spain",22],
       "Dante" : ["Italy",25]}

print("Result of step 1: ", dct.keys())
print("*************************************")
print("Result of step 2: ", dct.values())
print("*************************************")
dct["Daisy"][1] = 13
print("Result of step 3: ", dct.items())
dct["Ahmet"] = ["Turkey",24]
print("*************************************")
print("Result of step 4: ", dct.items())
print("*************************************")
dct.pop("Antonio")
print("Result of step 5: ", dct.items())





