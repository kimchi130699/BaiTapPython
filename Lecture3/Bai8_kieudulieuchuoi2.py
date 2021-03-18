#noi chuoi du lieu
StrA = "KIMCHI"
StrB = "BUITHI"
StrC = StrA + '\n'+ StrB
print(StrC)
#doi du lieu chuoi thanh so va nguoc lai
StrD = int("99") + 88
StrE = str(678) + "99"
print(StrD)
print(StrE)
#tim vi tri chu co trong chuoi hay khong 
strA = "KIMCHI"
strB = "M"
strC = strB in strA
print(strC)
#tim chu do theo vi tri
strD = "KimChi"
strE = strD[3]
print(strE)
#tim chu co vi tri cuoi cung trong chuoi
stra = "kimchi"
strb = stra[len(stra) -1]
print(strb)
#tim chu den vi tri nao do
strb = stra[None : 4]
print(strb)
#nhay buoc trong chuoi
strc = stra[None:2:-1]
print(strc)
#thay chu trong chuoi
strh = "kimchi102"
strg = strh[None:6] + "2" + strh[-2:None]
print(strg)