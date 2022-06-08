# ECE 191 Team D SP22
RobotX Maritime Competition: Camera testing


## color_detection.py
This script would perform a very simple red and blue detection algorithm. 
* Modify the name or directory of the image at line 8
* Indicate if the output image is from Zed camera or not at line 9
    * It is because Zed camera would put 2 output images side by side
* Indicate whether you are doing red or blue detection at line 10
    * set to True if you are doing red detection, set to False if you are doing blue detection

Details of the algorithm:
1. blur (smoothen) the input image by 5x5 Gaussian blur kernel
2. Convert input image from RGB to HSV color space
3. Define the range of red/blue in HSV color space
4. Put the range into a mask
5. Apply the mask using 3x3 Gaussian blur kernel
6. Apply threshold to threshold the input image from the mask.
   6. That way we are eliminating all the color other than the ones that we defined for the mask  
7. Find all contours in the thresholded image
8. Set a range of area to find the contour we need
9. Box the contour on the input image
10. Print the thresholded image and input image with tracked image boxed


## glare.py
This script would perform a very simple glare elimination algorithm. 
* Modify the name or directory of the image at line 5
* Indicate if the output image is from Zed camera or not at line 7
    * It is because Zed camera would put 2 output images side by side
    
Details of the algorithm:
1. Convert input image to a grayscale image
    1. colors are irrelevant for analyzing glare, as glare are usually extreme white
2. Apply Adaptive Histogram Equalization
3. Generate grayscale histogram
4. Print out the input image in grayscale, post AHE image, and grayscale histogram
5. Print out the number of pixels that has a grayscale value great than 250 (extreme white) for further analysis


    