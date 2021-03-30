class mother:
	suc_manh = 50
	def __init__(self,name,age,color):
		self.name_ = name
		self.age_ = age
		self.color_ =color

class daughter(mother):
	suc_manh = 40
	def __init__(self,name,age,color,nick):
		super().__init__(name,age,color)
		self.nick_ = nick

kimchi = daughter('chi','22 tuoi','mau hong','monkey')
print(kimchi.__dict__)
print(kimchi.suc_manh)

#constructor
