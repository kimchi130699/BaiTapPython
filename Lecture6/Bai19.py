#open file
file = open('Bai19.txt')
print(file)

#read file
data = file.read() 
print(data)

#muon doc file thi close file roi open file
file.close()
file = open('Bai19.txt')

data = file.read(2) # doc den ki tu 2 trong chuoi , neu ma nhap nhieu ki tu thi se doc het file
data1 = file.read(6)
print(data)
print(data1)

#khi thuc hien doc xong thi dong file lai
file.close()

file = open('Bai19.txt')
data3 = file.readline() #doc tung dong
data4 = file.readlines() #doc nhieu dong
print(data3)
print(data4)
file.close()

file = open('Bai19.txt')
data5 = list(file) # tuple cung tuong tu list
print(data5)
file.close()
#ghi them ki tu vao file
file = open('Bai19.txt', mode ='a+')
data6 = file.write('\n see you later')
print(data6)
file.close()
#doc lai file
file = open('Bai19.txt' , mode='r')
data7 = file.read()
file.seek(0)
data8 =file.read()
file.close()
print(data8)
