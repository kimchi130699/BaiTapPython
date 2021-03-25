#xuat ham co khoang trang
print('Bui Thi Kim Chi' , 'Hoc Cong Nghe Thong Tin')
print('Bui Thi Kim Chi' + str('Hoc Cong Nghe Thong Tin'))
print('Kim Chi',69)
print(123, [1,2,3] , 'kim chi')

#xuat ham chia ra, phan ra
print('Bui Thi' , 'Kim Chi', sep=' hihi ') #ko muon co khoang trang o giua thi : sep=''

#xuat ham khong xuong dong
print('Bui Thi Kim Chi' ,end=' ') #co the them moi ki tu hay chuoi trong end=''

from time import sleep 
print('start..')
sleep(3) #doi 3 giay
print('end...')

#se hien thi start va end  cung 1 luc , vi o day co mot dong line .
print('start.....' , end='')
sleep(2)
print('end')

#se hien thi start 1 truoc , roi toi start 2,end , vi start1 co line \n
print('start1\n','start2' , end='')
sleep(2)
print('end')

#tao ra file moi  
with open('Bai21.txt','w') as f:
	print('Hello Kim chi ne !!!' , file=f)

#flush=True la goi tat ca nhung gi co trong bo dem ra
print('start1\n','start2' , end='',flush=True)
sleep(2)
print('end')

from time import sleep
name = 'Bui Thi Kim Chi '
pp = 'Hoc lop IT17A1.11'

for c in name + pp:
	print(c,end='',flush=True)
	sleep(0.1)
print()