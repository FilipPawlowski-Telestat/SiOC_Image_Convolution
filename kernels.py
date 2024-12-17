import numpy as np
from skimage.filters import prewitt

sobel_x_kernel=np.array([[1,0,-1],
                         [2,0,-2],
                         [1,0,-1]])

sobel_y_kernel=np.array([[1,2,1],
                         [0,0,0],
                         [-1,-2,-1]])

laplace_kernel=np.array([[0,1,0],
                         [1,-4,1],
                         [0,1,0]])


gauss_kernel=np.array([[1/16,1/8,1/16],
                       [1/16,1/4,1/16],
                       [1/16,1/8,1/16]])


gauss_kernel5=np.array([[1, 4, 6, 4, 1],
                        [4, 16, 24, 16, 4],
                        [6, 24, 36, 24, 6],
                        [4, 16, 24, 16, 4],
                        [1, 4, 6, 4, 1]])/256

avrage_kernel=np.ones((3,3))/9

w_kernel=np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])


scharr_kernel0=np.array([[-3,0,3],
                        [-10,0,10],
                        [-3,0,3]])

scharr_kernel90=np.array([[3,10,3],
                          [0,0,0],
                          [-3,10,-3]])

prewitt_kernel0=np.array([[-1,0,1],
                          [-1,0,1],
                          [-1,0,1]])

prewitt_kernel90=np.array([[1,1,1],
                          [0,0,0],
                          [-1,-1,-1]])


bayer_mask = np.dstack([
    np.ones([2, 2]),
    np.ones([2, 2])/2,
    np.ones([2, 2]),])

