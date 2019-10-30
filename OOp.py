class Manusia:
    jmlActivity = 0

    def __init__(self, nama):
        self.nama = nama
        Manusia.jmlActivity += 1

    def dCount(self):
        print ("Total Activity %d" % Manusia.jmlActivity)
        
    def berjalan(self):
        print ("Nama :", self.nama, ", Actifity : Berjalan")
        
    def berlari(self, speed):
        print ('Nama :', self.nama, ', Activity : Berlari , Kecepatan :', speed)

    def berbicara(self):
        print ('Nama :', self.nama, ', Activity : Berbicara')

for i in range(100):
    x = input('activity :')
    if x == "":
        break
    else:
        y = input('Nama :')
        oManusia = Manusia(y)
        if x == "berjalan":
            print(oManusia.berjalan())
        elif x == "berlari":
            z = int(input("Masukkan Kecepatan :"))
            print(oManusia.berlari(z))
        elif x == "berbicara":
            print(oManusia.berbicara())
        else:
            print("Menu terdiri dari : 'berjalan', 'berlari',' berbicara', dan ''")
            Manusia.jmlActivity -= 1
            break
print ("Total Activity %d" % Manusia.jmlActivity)
              
    

