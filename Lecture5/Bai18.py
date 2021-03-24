#phuong thuc copy
dic = {'name' : 'kimchi','lop':'IT17A1.11'}
print(dic)
dic1 = dic.copy()
print(dic1)
#phuong thuc clear
dic2= {'name':'kimchi', 'tuoi' : 21}
dic2.clear()
print(dic2)

#get theo key va tra ve value cua no
value = dic1.get('name')
value1 = dic1.get('sdhsdfnjs' , 'a nhon se do') #neu key ko ton tai , se tu dong hien a nhon se do
print(value)
print(value1)

#phuong thuc items
d  = {'name' : 'kimchi', 'chieucao':150}
print(d)
dic3 = list(d.items())
print(dic3[0][0])

#lay ra nhung key trong dict
dic4 = d.keys()
print(dic4)
#lay values trong dict
dic5 = d.values()
print(dic5)

#pop lay hoan toan du lieu o trong dict ra
dic6 = d.pop('name')
print(d)
#neu khong co du lieu trong dict thi them default de ko bi loi
dic7 = d.pop('dddd' , 'hello every body')
print(dic7)

r = {'name':'kimchi','class' :'IT17A1.11'}
dic_1 = r.setdefault('subject','AI')
print(r)

#update du lieu moi
r = {'name':'kimchi','classs' :'IT17A1.11'}
print(r)
e= r.update(name = 'minhtuan')
print(r)