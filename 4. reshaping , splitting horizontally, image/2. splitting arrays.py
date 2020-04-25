import numpy as np

x = np.arange(9)
print(x)

print(np.split(x,3))
#must be equal division

print(np.split(x,[4,7]))

#split horizontally
a = np.array([["dhaka","mirpur","shahbag","Badda"],
			["brahmanbaria","paikpara","medda","pirbari"]])

print(a)

p1,p2 = np.hsplit(a,2)

print(p1)
print(p2)


print(np.hsplit(a,4))