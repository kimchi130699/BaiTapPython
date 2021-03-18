a = 4 #gán  cho biến a giá trị là 4. với 4 là kiểu số nguyên (Interger)
print (a)
#in ra kiểu dữ liệu của a
print (type(a))
b = 6.9 #gán cho biến b giá trị là 6.9 . với  6.9 là kiểu số thực (Float )
print (b)
print (type(b)) #in ra kiểu dữ liệu của b
#lấy toàn bộ nội dung trong thư viện Decimal
from decimal import* 
getcontext().prec = 30 #lấy tối đa 30 chữ số nguyên và phần thâp phân của Decimal
print (Decimal(10)/(Decimal(3)))
#phân số 
from fractions import*
frac = Fraction(6,9)
frac2 = Fraction(10,5)
frac3 = (frac + frac2)
print (frac3)
print(type(frac3))
#số thực ảo
c = complex(2,5)
print (c)
print(c.real)
print(c.imag)