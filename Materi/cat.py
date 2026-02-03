# definisikan class nama class
class cat:
    # #INI class kosongan masih
    # pass
    
    #defisinikan atribut didlm kostruktor
    #__init__=yg pertama kali diakses
    def __init__(self , color , height , width):
        self.color = color
        self.height = height
        self.width = width
#uat objek dr classs cat
garfield = cat("Orange", 25 , 50)
persia = cat("black" , 30 , 50.5)
# cek objek di memory kita, muncul adress 0*1*****
print("Obj garfield:", garfield)
print("Obj persia:", persia)
# panggil nama atribute dr objek
print(f" Warna persia: {persia.color}")
print(f" tinggi persia: {persia.height}")
print(f" lebar persia: {persia.width}")