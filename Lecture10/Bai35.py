##map
a = [1,2,3,4]
print(list(map(lambda x : x+1,a)))

##
b = lambda x:x+1
c = [2,3,4,5]
print([b(x) for x in c])
##
func = lambda x, y : x+y
a_ = [2,4,5,6]
b_ = [1,3,7,4]
ab = map(func, a_ ,b_)
print(list(ab))

##filter
funt = lambda x: x>0
c_ = [1,-3,6,0,-2,10,14]
print(list(filter(funt,c_)))
print(list(filter(None,c_)))

#reduce
from functools import reduce
r = lambda x , y: x+y
r_ = [1,2,3,4,5]
print(reduce(r,r_))

#
from functools import reduce

p_ = [1,2,3,4,5]
add= lambda x , y: x+y
mul = lambda x,y:x*y
print(reduce(add,p_,10))
print(reduce(mul,p_,10))