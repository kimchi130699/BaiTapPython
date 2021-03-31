#getter  la lay ra
class kter:
	def __init__(self,ho,ten):
		self.ho_ = ho
		self.ten_ = ten
		# self.emails = ho + ten + '@gmail.com'
	@property #bien no thanh thuoc tinh (ko con la phuong thuc)
	def ho_ten(self):
		return '{}{}'.format(self.ho_,self.ten_)
	@property
	def email(self):
		return self.ho_ + self.ten_ + '@gmail.com'

#Setter la gan vo gia tri moi
	@ho_ten.setter
	def ho_ten(self,ten_moi):
		homoi, tenmoi = ten_moi.split(' ')
		self.ho_ = homoi
		self.ten_ = tenmoi
#deleter
	@ho_ten.deleter
	def ho_ten(self):
		self.ho_= None
		self.ten_ = None
		print('da xoa')

kter_ = kter('Kim' ,'Chi')
kter_.ho_ten = 'Chi Bui'
kter_.ho ='Chi'
kter_.ten = 'Kim'
print(kter_.ho_)
print(kter_.ten_)
print(kter_.email)
print(kter_.ho_ten)
print(kter_.ho_ten)
del kter_.ho_ten
