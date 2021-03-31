#__str__
#__repr__
#neu co ca 2 phuong thuc nay cung mot lop thi se uu tien in __str__ truoc
class kimchi:
	crazy = 50
	def __init__(self,name,age,like):
		self.ten = name
		self.tuoi = age
		self.thich = like
	def __str__(self):
		return 'toi la:{},toi:{},sothich:{}'.format(self.ten,self.tuoi,self.thich)
	def __repr__(self):
		return 'toi:{},kimchi {},like {}'.format(self.ten,self.tuoi,self.thich)
	
kim_chi= kimchi('Buithikimchi','22 tuoi','nghe nhac')
print(kim_chi)
print('%s' %kim_chi) #__str__
print('%r' %kim_chi)#__repr__

#__len__
s = 'buithikimchi'
print(s.__len__())

#toan tu cx la nhung special method
print(2+3)
print(int.__add__(2,3))

print('Kim' + 'Chi')
print(str.__add__('Kim','Chi'))