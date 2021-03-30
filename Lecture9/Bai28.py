#ham
def kimchi():
	print('hello kim chi !')
	print('a nhon se dozz !')
kimchi()
kimchi()

###

def kchi(text,age): #text,age : param
	print(text)
	print(age)
kchi('hello kteam!',99) #'hello',99 :Args

#default phai nam o cuoi
def kc(lop,ten='kimchi'):
	print(lop)
	print(ten)
kc(12)
kc(10,'Chibui')

##

a = 'chibui102'
def fc(tuoi,a = a):
	print(tuoi)
	print(a)
fc(22)

####

def c(kimchi=[]):
	kimchi.append('C')
	print(kimchi)
c()
c()
c()