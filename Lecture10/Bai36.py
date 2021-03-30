##de quy
def sum(lst):
	if not lst:
		return 0
	else:
		return lst[0] + sum(lst[1:])
print(sum([1,2,3,4,5]))

###
def sum_(lst_):
	return 0 if not lst_ else lst_[0]+sum_(lst_[1:])
print(sum_([1,2,3]))

## 
def cal_sum(lst):
	id0 , *r = lst
	return id0 if not r else id0 + cal_sum(r)
print(cal_sum(['a' , 'b']))

##de quy goi lai no
def cal1(lst):
	if not lst: return 0
	return cal(lst)
def cal(lst):
	return lst[0] + cal1(lst[1:])
print(cal1([1,2,3,4,5]))