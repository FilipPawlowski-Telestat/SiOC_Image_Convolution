import kernels
from scipy import ndimage
import matplotlib.pyplot as plt
import skimage as ski
from skimage import io

# #wczytanie obrazu z dysku w skali szarości
image=ski.io.imread('./Own/woman.jpg', True)

# #konwolucja 2D oryginalnego obrazu z jądrem
modified_image = ndimage.convolve(image,kernels.avrage_kernel)

io.imshow(modified_image)
plt.show()

