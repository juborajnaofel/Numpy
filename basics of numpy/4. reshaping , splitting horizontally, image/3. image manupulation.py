import numpy as np

#any image is just n dimentional array
#greyscale = single channel, single value between 0.0 - 0.1
#rgb = multichannel  3 channels,  3 values= (R,G,B)


#3D dimensional matrix images, for greyscale the shape of the image matrix for example  (6,6,1)  
#3D dimension, for color-image the the shape of the image matrix for example  (6,6,3)  
# first 2d for height and width and the 3rd one is for channel


#pip install scipy
#pip install matplotlib

from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

f = misc.face()
print(f.shape)
print(type(f))
print(f)

plt.imshow(f)
plt.show()

a = f[384:,512:,:]
plt.imshow(a)
plt.show()

#vertical split
a1, a2 = np.split(f,2)
plt.imshow(a1)
plt.show()
plt.imshow(a2)
plt.show()


#Horizontal split
b1, b2 = np.split(f,2,axis = 1)
plt.imshow(b1)
plt.show()
plt.imshow(b2)
plt.show()

#concatenate
plt.imshow(np.concatenate((a1,a2)))
plt.show()

#concatenate
plt.imshow(np.concatenate((b1,b2),axis=1))
plt.show()
