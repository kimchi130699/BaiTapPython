#ddem xem so luong phan tu xuat hien bao nhieu lan 
a = [1,1,2,3,4,5,6]
b = a.count(1)
print(b)

#tim vi tri phan tu trong chuoi
c = a.index(3)
print(c)

#tao ban sao 
d = a.copy()
d[1] = 'kim chi'
print(d)

#lam sach list
e  = a.clear()
print(e)

#them mot phan tu vao list
s = [1,2,3,4,5,6,7,8]
s.append(9)
print(s)

#them mot list vao 1 list(tung phan tu ben trong)
s.extend([9,10,11])
print(s)

#them 1 phan tu vao vi tri trong list
e = [0,2,1,2,4]
e.insert(1,4) #them so 4 tai vi tri 1
print(e)

#lay ra mot so trong list
w = [1,2,3,4,5]
r = w.pop(3) 
print(r)

#xoa di 1 phan tu trong list
t = [1,2,3]
t.remove(1)
print(t)

#dao nguoc list
m = [1,2,3,4,5]
m.reverse()
print(m)

#SAP XEP LIST 	
n = [6,3,4,9,0,1]
n.sort()
# n.sort(reverse=true)
print(n)

p =[6,53,8,0]
p.sort(reverse=True) #(reverse=False)
print(p)

