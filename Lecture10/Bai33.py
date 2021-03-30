lst = (value for value in range(3))
for value in lst:
	print(value)

###
def square(lst):
	sq_lst = []
	for num in lst:
		sq_lst.append(num**2) 
	return sq_lst
var = square([1,2,3])
for value in var:
	print(value)

###
def square(lst):
	for num in lst:
		yield num**2
var = square([1,2,3])
for value in var:
	print(value)
### 
def gen():
	for var in range(3):
		print('yield' ,var + 1,'time')
		yield var
for var in gen():
	print(var)

##
def kc():
	yield 'kimchi'
	print('bui thi kim chi')
	yield 'kimchi1'
	print('bui thi kim chi1')
	yield 'kimchi2'
	print('bui thi kim chi2')
for a in kc():
	print(a)

##send
def gen():
	while True:
		x = yield
		yield x ** 2
g = gen()
print(next(g))
print(g.send(2))
print(next(g))
print(g.send(10))