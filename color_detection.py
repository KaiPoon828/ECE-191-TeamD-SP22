import cv2
import numpy as np

# oak-d pixel size: 1.55µm x 1.55µm


# Reading frames
image = cv2.imread("oak-D_color_3m_low.png")
isCameraZed = False
isRed = True

font = cv2.FONT_HERSHEY_PLAIN

if isCameraZed is True:
    colu = int(image.shape[1] / 2)
    image = image[:, 0:colu]

row = image.shape[0]
col = image.shape[1]

reference_frame = image.copy()  # for drawing stuff on it

# draw origin
cv2.line(reference_frame, (0, int(row / 2)), (col, int(row / 2)), (0, 255, 0), 1)
cv2.line(reference_frame, (int(col / 2), 0), (int(col / 2), row), (0, 255, 0), 1)
cv2.circle(reference_frame, (int(col / 2), int(row / 2)), 2, (0, 0, 255), 3)

# smoother the frame
blur_frame = cv2.GaussianBlur(image, (5, 5), 0)

# convert frame from BGR to HSV
frame_hsv = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)

if isRed:
    hsv_color1 = np.asarray([160, 110, 20])  # lower limit of red
    hsv_color2 = np.asarray([180, 255, 255])  # upper limit of red
    mask1 = cv2.inRange(frame_hsv, hsv_color1, hsv_color2)

    hsv_color3 = np.asarray([0, 150, 20])
    hsv_color4 = np.asarray([5, 255, 255])
    mask2 = cv2.inRange(frame_hsv, hsv_color3, hsv_color4)

    mask = cv2.bitwise_or(mask1, mask2)

# tracking blue
else:
    hsv_color1 = np.asarray([100, 120, 20])  # lower limit of blue    110 -> HD, 115 -> mid, 120 -> low
    hsv_color2 = np.asarray([135, 255, 255])  # upper limit of blue
    mask = cv2.inRange(frame_hsv, hsv_color1, hsv_color2)



blur_frame = cv2.GaussianBlur(mask, (3, 3), 0)
edges = cv2.Canny(blur_frame, 200, 200)

_, threshold = cv2.threshold(blur_frame, 30, 255, cv2.THRESH_BINARY_INV)  # 33
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

print(row)
print(col)
for contour in contours:

    (x, y, w, h) = cv2.boundingRect(contour)

    # center (x, y) of the rectangle
    x_center = x + int(w / 2)
    y_center = y + int(h / 2)

    # ignore the contour that has an area that is smaller than 50
    if cv2.contourArea(contour) < 10:
        continue

    elif 10 <= cv2.contourArea(contour) <= 90000:
        r = (np.sqrt((w) ** 2 + (h) ** 2)) / 2  # radius

        cv2.rectangle(reference_frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

        # area_in_cm = (cv2.contourArea(contour) * area_of_pixel_in_mirco_meter) * 1e-4
        # print(f"Area of object detected is {area_in_cm}cm")
        print(f"pixel ratio: {(cv2.contourArea(contour) / (row * col)) * 100}%")

        break

cv2.imshow("mask", mask)
cv2.imshow("image", reference_frame)
cv2.imshow("threshold", threshold)
cv2.waitKey(0)