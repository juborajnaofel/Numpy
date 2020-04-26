import numpy as np

#add two array elements together
a = np.array([1,2,3,4,5,6,7])
b = np.array([12,22,43,564,565,66,77])
c = a + b 
print(c)

c = b - a
print(c)

#elementwise multiplication if same dimension
c = a*b 
print(c)

c = b / a 
print(c)


#also if we use scalar
c = a%3
print(c)

#if we use conditionals 
print((a<25))
print((a<5))
print((a>25))


#more.....
r = a.sum()
print(r)

r = a.min()
print(r)

r = a.max()
print(r)

a *= 3
print(a)