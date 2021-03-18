a = 'hello everybody how are you Today'
#tach tung tu trong chuoi
b = a.split(' ')
c = a.split('y')
d = a.split(' ',2)
#rsplit la cat tu ben phai
#lsplit la cat tu ben trai
#cat chuoi truoc va sau
e = a.partition('everybody')
#rpartition la been phai
#lpartition la ben trai
#dem chuoi
g = a.count('l')
#dem chuoi co diem bat dau va diem cuoi
i = a.count('o',0,20)
#kiem tra xem chuoi co bat dau la chu 'hello' khong
k = a.startswith('hello')
#kiem tra xem o vi tri so 6 co phai la chu 'e' khong
j = a.startswith('e',6)
j1 = a.startswith('l', 4,8)
#endswith dung nhu starswith
#tim kiesm tu trong chuoi
#find tuong tu nhu index , nhung index ma tim ko ra thi se hien loi
p = a.find('how')
#co phai chuoi viet thuong hay khong
z = a.islower()
#kiem tra chuoi co viet hoa hay khong
x = a.isupper()
#kiem tra cos phai la so hay khong
f = a.isdigit()
#kiem tra co khoang trang hay khong
o = a.isspace()
print(a)
print(b)
print(c)
print(d)
print(e)
print(g)
print(i)
print(k)
print(j)
print(j1)
print(p)
print(z)
print(x)
print(f)
print(o)