import numpy as np

a = np.arange(11)**2

#printing the square root
for i in a:
	print(i**(1/2))
	

#iterating 2d arrays
students = np.array([["Juboraj", "Naofel", "Utsha"],
					 [30,40,50],
					 [21,22,23]])
print(students)

#iterating the first dimension
for i in students:
	print("i = ",i)
	
#Row major - flattening elements
for element in students.flatten():
	print(element)
	
#Column major - flattening elements
for element in students.flatten(order = "F"):
	print(element)


#nditer function to iterate
array_ = np.arange(12).reshape(3,4)
print(array_)
#row major
for i in np.nditer(array_):
	print(i)
#column major
for i in np.nditer(array_, order = 'F'):
	print(i)
	
	
#there is much difference between nditer and flatten and has advance config