import numpy as np

#creating an array

a = np.array([["dhaka","mirpur","shahbag","Badda"],
			["brahmanbaria","paikpara","medda","pirbari"]])
print(a)
print(a.shape)

#flatten an array using ravel in row major
print(a.ravel())

#transpose an array: row becomes columns and vice versa
print(a.T)

#ravel the transpose
print(a.T.ravel())


#reshape
print(a.reshape(4,2))
