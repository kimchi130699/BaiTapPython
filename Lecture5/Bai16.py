set_1 = {34,56}
print(set_1)
print(type(set_1))

set_2 = {'kimchi'}
print(set_2)

#kieu du lieu tuple
#set ko luu duoc unhashable ,list
set_3 = {('kimchi'),(2,3,4)}
print(set_3)

set_4 ={ i for i in range(3)}
print(set_4)
print(type(set_4))

set_5 = set((1,2,3))
print(set_5)
print(type(set_5))

set_6 = set('kimchi')
print(set_6)
print(type(set_6))

#toan tu in
print(1 in {1,2,3})
print ((1,2) in {(1,2),3})
print(1,2 in {1,2,3})

#toan tu tru
print({1,2,3} - {2,3}) 

#toan tu and
print ({1,2,3} & {1,2,4,5}) #lay cai 2 ben deu co


#toan tu or
print({1,2,3,4} | {2,3,4,5}) #lay toan bo 2 ben

#phep so
print({1,2,3} ^ {3,4}) #nhu toan tu tru

set1 = {2,3,4}
set1.clear()
print(set1)

#pop la boc ra phan tu trong set, va no se khong con trong set do
set2 = {3,4,5,6}
set2.pop() #lay so lieu dau tien
print(set2)

#remove la xoa phan tu ma ban muon , neu ko co phan tu trong set thi bao loi
set3 = {6,7,8,9}
set3.remove(8)
print(set3)

#discard hiong nhu remove , nhung neu ko co phan tu trong set thi se ko bao loi

set3.discard(10)
print(set3)
#phuong thuc copy
set4  = set3.copy()
print(set4)

#phuong thuc add , se them gia tri vao set . neu da ton tai thi se ko them vao
set5 = {1,2,3,4,5,6,77,8}
set5.add(11)
print(set5)