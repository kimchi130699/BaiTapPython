def kc():
	kimchi = 'kimchibuithi'
	print('my name',kimchi)
kc()

##
num = 23
name = 'kimchi'
born = 1999
tup = tuple('BuiThiKimChi')

def hi(a):
	a='ahihi'
	print('changed successfully!')
hi(num)
hi(name)
hi(born)
hi(tup)
print('-'*20)
print('{}\n{}\n{}\n{}\n'.format(num,name,born,tup))

###
lst = ['kimchi' , 22 ,'tuoi']

def a (var):
	var[0] = 'minhtuan'
	print('changed successfully')
print(lst)
a(lst)
print(lst)

##
def b():
	global kimchi #khoi tao global khong co gia tri
	kimchi = 'ahihi' #sau khi khoi tao global thi gan gia tri
b() #sau do nho chay ham
print(kimchi)

###
def m_local():
	global x
	x = 1
def local():
	x = 5
	print('x local:',x)

m_local()
print(x)
local()
print(x)
