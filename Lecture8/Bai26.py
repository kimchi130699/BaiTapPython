length = 4
iter_ = (x for x in range(length))
a = 0 
while a < length:
	print(next(iter_))
	a += 1

## Try , except
length1 = 6
iter_1 = (x for x in range(length1))
b = 0 
while b < length1:
	try :
		print(next(iter_1))
	except StopIteration:
		break

#for
iter_2 = (x for x in range(4))
for value in iter_2:
	print('->',value)

#items , for
st = {'name' : 'kim chi' , 'class': 'IT17A1.11'}
for key , value in st.items():
	print(key , '->' , value)


#break ,for
s = 'Dong A University'
for ch in s :
	if ch == ' ':
		break
	else:
		print(ch)

#continue, for
s = 'Bui Thi Kim Chi'
for ch in s :
	if ch == ' ':
		continue
	else:
		print(ch)
#for ,else , break (cos break thi else khong co tac dung) , 
for k in (1,2,3):
	print(k)
	if k % 2 == 0:
		break
else:
	print('Done!')

#for ,else , continue (co continue thi else  co tac dung) , 
for k in (1,2,3):
	print(k)
	if k % 2 == 0:
		continue
else:
	print('Done!')