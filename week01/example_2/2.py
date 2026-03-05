import cv2 as cv
import numpy as np

WINDOW_NAME = "Painting App"
IMAGE_PATH = "../dataset/soccer.jpg"  

# Brush settings
brush_size = 5
MIN_BRUSH = 1
MAX_BRUSH = 15

# Load image
img = cv.imread(IMAGE_PATH)

# Fallback: create a blank white canvas if image loading fails
if img is None:
    print(f"[Warning] Cannot load '{IMAGE_PATH}'. Using a blank canvas instead.")
    img = np.full((600, 900, 3), 255, dtype=np.uint8)


def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))


def mouse_callback(event, x, y, flags, param):
    global img, brush_size

    # Left click / drag -> blue brush
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), brush_size, (255, 0, 0), -1, lineType=cv.LINE_AA)

    elif event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_LBUTTON):
        cv.circle(img, (x, y), brush_size, (255, 0, 0), -1, lineType=cv.LINE_AA)

    # Right click / drag -> red brush
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), brush_size, (0, 0, 255), -1, lineType=cv.LINE_AA)

    elif event == cv.EVENT_MOUSEMOVE and (flags & cv.EVENT_FLAG_RBUTTON):
        cv.circle(img, (x, y), brush_size, (0, 0, 255), -1, lineType=cv.LINE_AA)


cv.namedWindow(WINDOW_NAME)
cv.setMouseCallback(WINDOW_NAME, mouse_callback)

while True:
    # Display copy so UI text does not permanently remain on the image
    display = img.copy()

    cv.putText(
        display,
        f"Brush Size: {brush_size}   (+ / - to change, q to quit)",
        (10, 30),
        cv.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 0),
        2,
        cv.LINE_AA
    )

    cv.putText(
        display,
        "Left Drag: Blue   Right Drag: Red",
        (10, 65),
        cv.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 0),
        2,
        cv.LINE_AA
    )

    cv.imshow(WINDOW_NAME, display)

    key = cv.waitKey(1) & 0xFF

    # '+' can sometimes be detected as '=' depending on keyboard layout
    if key in (ord('+'), ord('=')):
        brush_size = clamp(brush_size + 1, MIN_BRUSH, MAX_BRUSH)

    elif key in (ord('-'), ord('_')):
        brush_size = clamp(brush_size - 1, MIN_BRUSH, MAX_BRUSH)

    elif key == ord('q'):
        break

cv.destroyAllWindows()