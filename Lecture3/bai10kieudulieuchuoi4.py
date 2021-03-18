a = 'Hello every body, How are you?'
#viet hoa chu cai dau dong 
b = a.capitalize()
#viet hoa tat ca cac chu trong chuoi
c = a.upper()
#viet thuong tac ca chu trong chuoi
d = a.lower()
#chu viet thuong se thanh viet hoa , va nguoc lai
e = a.swapcase()
#viet hoa tu dau trong mot chu
f = a.title()
#can giua
g = a.center(100, '*')
#can phai
h = a.rjust(50, '-')
#can trai
i = a.ljust(50, '-')
#ma hoa
s = 'nhìn gì mà nhìn '
k = s.encode()
#cong mot danh sach vao mot chuoi
j = s.join(['1','2','3'])
#thay chuoi cu bang mot chuoi moi
l = s.replace('nh' , 'mk' , 1)
#xoa ki tu dau va cuoi cua chuoi
n = s.strip('n')
#rstrip la xoa ben phai
#lstrip la xoa ben trai
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(k)
print(j)
print(l)
print(n)