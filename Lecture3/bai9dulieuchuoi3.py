a = 'My name is %s %s' %('chi','bui')
print(a)
# lam tron so thap phan
f = '%.f' %(3.9999)
print(f) 
#
c = 'kim chi bui'
d = f'{c} - very crazy'
print(d)
#
name = 'kim chi'
address = 'Da Nang city'
phone = '0327991485'
result = f'Student : {name}\nAddress:{address}\nPhone:{phone}'
print(result)
#
r = '1: {hi}, 2:{mi}'.format(hi=111,mi=222)
print(r)
#
c = 'hello {:*^50} it is me '.format('chi chi')
print(c)