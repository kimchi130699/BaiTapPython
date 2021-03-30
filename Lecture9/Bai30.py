def kimchi(a,b,c,d):
	print(a)
	print(b,c)
	print('end',d)
lst=['kimchi','hoc lop',12,'hihi']
kimchi (*lst)

##
def a (e,f,*,g):
	print(e)
	print(f)
	print(g)
lst = [13,'hihi']
a(*lst ,g = 'hoho')

## 
def chibui(*args, kter):
	print(args)
	print(kter)
chibui(*(x for x in range(20)) , kter='hello kter!')

##
def kc(name,age):
	print('name=>',name)
	print('age=>',age)
dic = {'name':'kimchi','age':22}
kc(**dic)

##
def f(**kwas):
	for key,value in kwas.items():
		print(key, '=>' , value)
f(name='buithikimchi', member=79)