import numpy as np

#add two array elements together
a = np.array([[1,2],[4,5]])
b = np.array([[1,0],[5,6]])
print(a)
print(b)


#elementwise result
c =a*b 
print(c)


#matrics multiplication
print((a.dot(b)))
#-----or------
print((np.dot(a,b)))


#more
r = a.sum(axis=0)
print(r)

r = a.sum(axis=1)
print(r)

r = a.min(axis=0)
print(r)

r = a.max(axis=1)
print(r) 
