import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread("oak-D_glare.png")
# image = cv2.imread("zed_glare1.jpg")
isCameraZed = False

if isCameraZed is True:
    colu = int(image.shape[1] / 2)
    image = image[:, colu::]
    # image = image[:, 0:colu]

# image = image[300:1200, 0:1100]
# image = image[300:1200, 0:1100]

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

clahe = cv2.createCLAHE(clipLimit=5.0,
                        tileGridSize=(10, 10))
equalized = clahe.apply(gray)
equalized_HE = cv2.equalizeHist(gray)
cv2.imshow("original", gray)
cv2.imshow("ada_HE", equalized)
# cv2.imshow("original image", image)


dst = cv2.calcHist(equalized, [0], None, [252], [0, 252])

plt.figure(1)
plt.hist(gray.ravel(), 252, [0, 252])
plt.title('Histogram for original grayscale image')
plt.ylim(0, 30000)
plt.xlabel("grayscale value (0 == black, 255 == white)")
plt.ylabel("Number of pixels")

plt.figure(2)
plt.hist(equalized.ravel(), 252, [0, 252])
plt.title('Histogram for adaptive histogram equalization')
plt.ylim(0, 30000)
plt.xlabel("grayscale value (0 == black, 255 == white)")
plt.ylabel("Number of pixels")
plt.show()

rgb_after_hist = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
cv2.imshow("rgb", rgb_after_hist)
cv2.waitKey(0)

white_pixel_count = 0

for i in range(np.shape(image)[0]):
    for j in range(np.shape(image)[1]):
        if gray[i][j] >= 250:
            white_pixel_count += 1

print(white_pixel_count)