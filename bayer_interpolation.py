from skimage import io
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt


# Wczytanie obrazu
image = np.load('./Bayer/circle.npy')
r_channel = image[:, :, 0]
g_channel = image[:, :, 1]
b_channel = image[:, :, 2]

def interpolate(r, g, b):
    k = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    r_new = ndimage.convolve(r, k, mode='nearest')
    g_new = ndimage.convolve(g, k, mode='nearest')
    b_new = ndimage.convolve(b, k, mode='nearest')

    rgbArray = np.zeros((len(r), len(r), 3), dtype='uint8')
    rgbArray[..., 0] = r_new * 255
    rgbArray[..., 1] = g_new * 255
    rgbArray[..., 2] = b_new * 255

    return rgbArray

img_interpolated = interpolate(r_channel, g_channel, b_channel)
io.imshow(img_interpolated)
plt.show()