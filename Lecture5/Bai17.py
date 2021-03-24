dic = {'ten': 'kimchi', 'Lop': 'IT17A1.11', 'Nam hoc ': 2017}
print(dic)
print(type(dic))

dic1 = {key: value for key, value in [('name','kimchi'), ('nam hoc',2017)]}
print(dic1)
print(type(dic1 ))

dic2 = dict(ten='kimchi', lop='IT17A1.11', namhoc=2017)
print(dic2)

#phuong thuc su dung fromkeys
itemr = ('ten' , 'name' , True , 89)
dic3 = dict.fromkeys(itemr,'kimchi')
print(dic3)

#lay value trong dict bang key

print(dic3[True])	

#thay doi noi dung trong dict
iterm = ('ten','lop','monhoc')
dics = dict.fromkeys(iterm,'hihi')
print(dics)
dics['namhoc'] = 2017
print(dics)

dic7 = dict(BT='Bui Thi' , KC='KimChi', Age=22)
print(dic7)
dic7['Age'] = dic7['Age'] + 3
print(dic7)