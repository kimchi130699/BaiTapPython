n = 69 
print(n)
print(n + 1)
print(n.__add__(1))
print(n.__sub__(1))
print(n.__mul__(2))
print(n.__neg__())

#Hashable
s1 = 'BuiThi'
s2 = 'KimChi'

s1 = s1 + 'hihi'
s2 += 'hihi'

print(id(s1))
print(id(s2))

#unhashable
s3 = [3,4]
s4 = [1,2]

print(id(s3))
print(id(s4))

s3 = s3 +[0]
s4 += [0]
print(id(s3))
print(id(s4))