import numpy as np

#find radians of angles
angles = np.array([0,30,45,60,90])
print(angles)

angle_radians = angles * np.pi / 180
print(angle_radians)

#radians using function
angle_radians_fun = np.radians(angles)
print(angle_radians_fun)

#find sine
sin = np.sin(angle_radians)
print(sin)

#find cosine
c = np.cos(angle_radians)
print(c)

#find tan
c = np.tan(angle_radians)
print(c)

#find sine inverse or arc sine
c = np.arcsin(sin)
print(c)

#find degrees
c = np.degrees(c)
print(c)



#others function to perform in an array, statistical functions

#find mean
test_scores = np.array([10,20,30,40,20,21,22,45])
c = np.mean(test_scores)
print(c)

#find median
test_scores = np.array([10,20,30,40,20,21,22,45])
c = np.median(test_scores)
print(c)


#one more function to learn, genfromtext and shape
