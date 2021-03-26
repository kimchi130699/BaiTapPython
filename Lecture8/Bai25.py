k = 5
while k > 0:
	print('k =',k)
	k -=1

#vong lap chuoi
chuoi = 'Kim Chi'
value = 0
dodai = len(chuoi)

while value < dodai:
	print(value,'text:',chuoi[value])
	value += 1

#break
tup = []
var = 1

while True:
	if var % 2==0:
		tup.append(var)
		if len(tup) >=5:
			break #neu tup > = 5 thi se dung vong lap tai day
	var +=1
print(tup)
print(var)

#continue
num = 0
while num < 10:
	num += 1
	if num % 2 == 0 :
		continue
	print(num , 'khong chia het cho 2')
print(num)

#
k = 0
while k <5 :
	print('so k la:',k)
	k +=1
else:
	print('k khong nho hon 5')