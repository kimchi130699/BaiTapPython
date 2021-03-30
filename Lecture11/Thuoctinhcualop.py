class kimchi:
	stt = 1;
	so_thu_tu = 1
	sub = 'hihi'
	def __init__(chibui,name,age,phone):
		chibui.name_ = name
		chibui.age_ = age
		chibui.phone_ = phone
		chibui.stt = kimchi.so_thu_tu
		kimchi.so_thu_tu +=1

kim_chi = kimchi('chi',22,'0327991485')
kim_chi1 = kimchi('chi',22,'0327991485')
print('Ten toi la:' , kim_chi.name_)
print('Toi : ' ,kim_chi.age_)
print('So dien thoai :' , kim_chi.phone_)
print(kimchi.sub)
print(kim_chi.stt)
print(kim_chi1.stt)
print(kim_chi.so_thu_tu)

kim_chi.sub ='haha'

print(kimchi.sub)
print(kim_chi.sub)

###
class sieunhan:
	suc_manh = 30
	def __init__(seft , ten_ , vukhi_, mausac_):
		seft.ten = ten_
		seft.vukhi = vukhi_
		seft.mausac = mausac_
	def xinchao(seft):
		print('ta la sieu nhan :' , seft.ten)
		print('suc manh cua ta la :' , seft.suc_manh)
sieu_nhan = sieunhan('do','kiem','do')
sieu_nhan.xinchao()

