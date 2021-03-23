#list bij gioi han trong dau ngoac vuong []
#list cach nhau boi dau phay
#chua moi gia tri doi tuong trong python va bao gom chinh no
a = [1,2,3,"kimchi"]
#tao 1 list chua 30 phan tu ,bat dau tu 0
b = [i for i in range(30)]
c = [[n*2] for n in range(1,4)]
d = list('kimchibui')
#toan tu cong 
e = [1,2,3]
e += ['one','two','three']
#toan tu nhan , luu y : khong th nhan list vs list
f = [1,2,3]
f *= 3
# toan tu in , ktra g co nam trong f khong
g = 2 in f
#cach lay phan tu trong list
t = f[1]
v = f[0:2]
#lay phan tu trong list va dao nguoc lai
x = [1,2,3,4,5,6,7]
h = x[::-1]
#thay doi phan tu trong list
x[2] = 'kimchi'
#ma tran
w = [[3,4,5],[9,8,7],[6,5,4]]

# thay doi 1 so trong ma tran , ko thay doi list ban dau
k = list(w)
k[0] = 'kimchi'
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(t)
print(v)
print(h)
print(x)
print(w[0])
print(w[1])
print(w[2])
#cach truy xuat trong ma tran
print(w[0][1])
print(w[1][0])
print(w[2][0])
print(k)