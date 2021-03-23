#tao mot tuple 
tup = (1,2,3,4,5,6)
print(tup)

tup0 = tuple('kimchi')
print(tup0)

tup1 = (i for i in range(10))
a = tuple(tup1)
print(a)

#toan tu cong
a = (2,3,4)
a += (5,6,7)
print(a)
#toan tu nhan
b = (1,2,3)
b *= 2
print(b)

#toan tu in
c = (7,8,9,0)
c = 7 in c 
print(c)
# lay phan tu trong tuple
e = (4,5,3,6)
d = e[1]
print(d)

#do dai phan tu trong tuple
r = (3,4,5,78,44,2)
e = len(r)
print(e)
#lay phan tu cuoi trong tuple
f = r[-1]
print(f)
#dao nguoc phan tu
t = r[::-1]
print(t)

#dem bao nhieu lan xuat hien cua mot phan tu
d = (2,3,4,3,2,2)
y = d.count(2)
print(y)
# lay ra vi tri xuat hien cua phan tu do
o = d.index(2)
print(o)

