import cv2

# Load the image
img = cv2.imread('D:\\test\\Ball.jpg')

# Define the lower and upper boundaries of the green color in the HSV color space
green_lower = (35, 50, 50)
green_upper = (80, 255, 255)

# Convert the image to the HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create a mask using the green color range
mask = cv2.inRange(hsv, green_lower, green_upper)

# Apply the mask to the original image
res = cv2.bitwise_and(img, img, mask=mask)

# Save the result to a file
cv2.imwrite('D:\\test\\result.jpg', res)
