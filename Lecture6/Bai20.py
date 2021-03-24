itera = [x for x in range(3)] #tao ra mot tuple
print(itera)

itera1 = (x for x in range(3))#tao ra mot iterator
print(itera1)
#truy xuat tung phan tu trong iterator
print(next(itera1))
print(next(itera1))
print(next(itera1))
#ko the truy xuat index , ma chi truy xuat tung phan tu

#tinh tong 
itera2 = (x for x in range(3))

print(sum(itera2))
print(sum(itera2, 1)) #cong them 1
print(sum(itera2, -2)) #cong them -2


#khi da sum thi ko next duoc

#tim gia tri lon nhat
itera3 = (x for x in range(6))
print(max(itera3)) #tim max
itera4 = (x for x in range(6))
print(max([],default='kimchi')) #ko co max thi se tra ve default
print(max(2,4,3,65,6,76))

#tim min
itera5 = (x for x in range(8))
print(min(itera5)) #tim min
itera6 = (x for x in range(5))
print(min([],default='kimchi')) #ko co min thi se tra ve default
print(min(2,4,3,65,6,76))

#dung sort
sort = [2,34,543,2,8,23]
print(sort)
print(sorted(sort))
print(sorted(sort, reverse= True))