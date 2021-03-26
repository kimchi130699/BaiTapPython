#c1: khoi tao range
k = range(7)
print(type(k))
print(k[3])

#c2 : khoi tao range
print(list(range(2,5)))

print(list(range(5,2,-1)))  #range = stop - step <=> 2 - (-1)

#toan tu in
k = range(999)
print(100 in k )

#
lst = [5 , (1,2,3),{'kimchi' , 'Buithi'}]
for i in range(len(lst)):
	print(lst[i])

#range
lst1 = [2,3,4]
for value in range(len(lst1)):
	lst1[value] += 1
print(lst1)

#phep toan dich bit i = 0 ; c <<3;
#
lst2 = ['--'.join((a.capitalize(),b.upper() +c.lower()))
for a , b , c in [('Bui','thi','chi'),('lop','cong','nghe')]]
print(lst2)

# 
lst3 = []
for a,b,c in [('le','minh','tuan'),('hoc','lop','mang')]:
	a = a.capitalize()
	b = b.upper()
	c = c.lower()
	lst3.append('--'.join((a,b+c)))
print(lst3)

#
lst5 = {key: value + 1 for key,value in (('kimchi',12),('minhtuan',13)) if value % 2 !=0}
print(lst5)

#enumerate
std = ['Chi','Tuan','Anh','Cuong']
gen = enumerate(std)
print(list(gen))

#
std1 = ['Chi','Tuan','Anh','Cuong']
for idx , stu in enumerate(std1,9):
	print(idx, '=>',stu)