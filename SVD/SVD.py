import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

def svd(gray):
    s, u = np.linalg.eig(np.dot(gray, gray.T))
    s, v = np.linalg.eig(np.dot(gray.T, gray))
    u = np.asarray(u)
    s = np.asarray(s)
    v = np.asarray(v)
    u = u[:, 0: 411]
    print u.shape, v.shape, s.shape
    for i in range(len(s)):
        s[i] = math.sqrt(s[i])
    return u, s, v.T

#Convert color image into gray image
img = mpimg.imread('gal.jpg')
gray = rgb2gray(img)
#plt.imshow(gray, cmap = plt.get_cmap('gray'))
#plt.show()
plt.imsave('gray.jpg', gray, cmap = plt.get_cmap('gray'))

#SVD
U, s, V = np.linalg.svd(gray, full_matrices = False)
print U.shape, V.shape, s.shape
s[50:] = 0
S = np.diag(s)
re_1 = np.dot(U, np.dot(S, V))
plt.imshow(re_1, cmap = plt.get_cmap('gray'))
plt.show()
print U


U, s, V = svd(gray)
s[50:] = 0
S = np.diag(s)
print U
re_2 = np.asarray(np.dot(U, np.dot(S, V)))


plt.imshow(re_2, cmap = plt.get_cmap('gray'))
plt.show()