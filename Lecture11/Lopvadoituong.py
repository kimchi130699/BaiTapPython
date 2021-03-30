#khoi tao class
class kimchi:
	pass
kim_chi =kimchi()
print(kim_chi)

##
class sieunhan:
	pass
sieu_nhan = sieunhan()
sieu_nhan.ten = 'sieu nhan hong'
sieu_nhan.vukhi ='sung va kiem'

print('toi la:',sieu_nhan.ten)
print('toi choi:',sieu_nhan.vukhi)

##
class kimchi:
	def __init__(kc,ten,tuoi,lop):
		kc.ten_ = 'Bui Thi' +ten
		kc.tuoi_ = tuoi
		kc.lop_ = lop
	def xinchao(kc):
		return " xin chao!!" + kc.ten_
kim_chi = kimchi('kimchi',22,'IT17A1.11')
print('Ten:',kim_chi.ten_)
print('Age:',kim_chi.tuoi_)
print('Lop:',kim_chi.lop_)
print(kim_chi.xinchao())