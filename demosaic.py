import numpy as np
from scipy import ndimage
from skimage import io
import matplotlib.pyplot as plt
import kernels

image = np.load("Bayer\circle.npy")


demosaic_image = np.dstack([
    ndimage.convolve(image[:, :, channel], kernels.bayer_mask[:, :, channel], mode="wrap")
    for channel in range(3)
])

io.imshow(demosaic_image)
plt.show()

