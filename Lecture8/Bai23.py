print(10<9)
print( 1 > 0 & 1<3 )
print(30 == 18+12)
print((3*2) != 0)
print(ord('a'))
print(ord('A'))
print('KimChi' == 'KimAnh ')
print('aaa' > 'aaab ')

lst = [1,2,3]
lst1 = [1,2,3]
lst2 = lst
print(lst == lst1)
print(lst is lst1)
print(lst2 is lst)

#toan tu is se dung id de so sanh
#tu -5 den 256  hoac mot chuoi co so ki tu duoi 20 thi id se ko thay doi 
a = -5
b = -5
print(a is b)

c = 699
d = 699
print(id(c))
print(id(d))
print(c is d)

# 1 la True 1 la False 
true = True + 1
false = False + 1
print(true)
print(false)

n = 5 
print(n>1 and n<6)

#trong python
c = 9
r = 4
print(-1<2<r<c)

k = 4 
print(k in (4,7))