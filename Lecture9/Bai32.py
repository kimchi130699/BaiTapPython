def hcn(cd,cr):
	cv = (cd + cr)*2
	return cv
cd1 = 6
cr1 = 4

cv1 = hcn(cd1,cr1)
print(cv1)
print(hcn(8,4))

##
def return1():
	print('su dung return de ngat ham')
	return
	print('print nay se ko duoc hien')
none = return1()
print(type(none))

## 
def hcn1(chd, chrg):
	chuvi =(chd + chrg) *2
	dientich = chd * chrg
	return chuvi , dientich
chd1 = 7
chrg = 3
chuvi1, dientich1 =hcn1(chd1,chrg)
print(chuvi1,dientich1)

print(hcn1(6,3))