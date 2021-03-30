lamb = lambda a , b , c :(a+b+c)/3
print(lamb(1,2,3))

##
a = lambda x , a =2 : x ** a
print(a(3,3))

##
def kimchi():
	b = lambda x : x+' she is very crazy'
	return b
a_ = kimchi()
print(a_('chibui'))

##
lamb1 = [lambda x: x**2,	lambda x: x**3,lambda x: x**4]
for var in lamb1:
	print(var(4))

###
key = 'kteam'
print({'google': lambda :'hihi',
		'kteam': lambda: 'free education',
		'kimchi': lambda : 'haha'} [key]())
##
f = lambda x, y : x if x>y else y
print(f(3,5))

##
s = lambda x: (1 if not(x%3) else 0) if not (x%2) else 0
print(s(6))\

##
def d(st1):
	return lambda str2: st1 + str2
p = d('kimchi')
print(p('hoho'))