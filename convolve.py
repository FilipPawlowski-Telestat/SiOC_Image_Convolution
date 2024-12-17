import numpy as np

def convolution2d(image, kernel, bias):
    m, n = kernel.shape
    if (m == n):
        shape = image.shape
        y, x = shape[0], shape[1]
        y = y - m + 1
        x = x - m + 1
        new_image = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel) + bias
    return new_image