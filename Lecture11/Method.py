##class method
##staticmethod
class sieunhan:
	sucmanh = 50
	def __init__(kc, ten_,vukhi_,mausac_):
		kc.ten = ten_
		kc.vukhi = vukhi_
		kc.mausac = mausac_
	@classmethod
	def string(cls,s):
		lst = s.split('-')
		new_lst = [st.strip() for st in lst]
		ten, vukhi, mausac = new_lst
		return cls(ten, vukhi, mausac)
	@staticmethod
	def bienhinh():
		print('1,2,3 . Sieu nhan kim chi bien hinh')
str_ = 'do-kiem-do'
sieu_nhan = sieunhan.string(str_)
sieu_nhan.bienhinh()
print(sieu_nhan.__dict__) 
