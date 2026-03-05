import cv2 as cv
import numpy as np

# 1. Load image
image_path = "../dataset/soccer.jpg"   # Change this to your image file name
img = cv.imread(image_path)

# Check if image was loaded successfully
if img is None:
    raise FileNotFoundError(f"Cannot load image: {image_path}")

# 2. Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 3. Convert grayscale back to BGR for side-by-side display
#    이유: 원본은 (H, W, 3), 그레이스케일은 (H, W)라서
#    np.hstack()를 바로 하면 shape mismatch가 발생할 수 있음
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

# 4. Concatenate images horizontally
result = np.hstack((img, gray_bgr))

# 5. Display result
cv.imshow("Original Image | Grayscale Image", result)

# Wait until any key is pressed
cv.waitKey(0)

# Close all windows
cv.destroyAllWindows()