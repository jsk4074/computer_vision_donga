import cv2 as cv
import numpy as np

WINDOW_MAIN = "ROI Selector"
WINDOW_ROI = "Selected ROI"
IMAGE_PATH = "../dataset/soccer.jpg"   # Change to your image

img = cv.imread(IMAGE_PATH)
if img is None:
    raise FileNotFoundError(f"Cannot load image: {IMAGE_PATH}")

img_original = img.copy()

# State variables
is_dragging = False
start_pt = (0, 0)
end_pt = (0, 0)

roi = None            # stores last extracted ROI (numpy array)
roi_rect = None       # stores last rect (x1, y1, x2, y2)


def normalize_rect(p1, p2):
    """Return normalized rectangle coordinates: (x1, y1, x2, y2) with x1<=x2, y1<=y2."""
    x1, y1 = p1
    x2, y2 = p2
    return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)


def mouse_callback(event, x, y, flags, param):
    global is_dragging, start_pt, end_pt, img, roi, roi_rect

    if event == cv.EVENT_LBUTTONDOWN:
        is_dragging = True
        start_pt = (x, y)
        end_pt = (x, y)

    elif event == cv.EVENT_MOUSEMOVE and is_dragging:
        end_pt = (x, y)

    elif event == cv.EVENT_LBUTTONUP:
        is_dragging = False
        end_pt = (x, y)

        x1, y1, x2, y2 = normalize_rect(start_pt, end_pt)

        # Avoid empty ROI
        if (x2 - x1) < 2 or (y2 - y1) < 2:
            roi = None
            roi_rect = None
            return

        roi_rect = (x1, y1, x2, y2)

        # ROI extraction via numpy slicing (y first, then x)
        roi = img_original[y1:y2, x1:x2].copy()
        cv.imshow(WINDOW_ROI, roi)


cv.namedWindow(WINDOW_MAIN)
cv.setMouseCallback(WINDOW_MAIN, mouse_callback)

print("Controls:")
print(" - Drag with LEFT mouse button to select ROI")
print(" - Press 'r' to reset selection")
print(" - Press 's' to save ROI as roi.png")
print(" - Press 'q' to quit")

while True:
    # Start from original each frame (so rectangle doesn't permanently draw)
    display = img_original.copy()

    # Draw rectangle while dragging or after selection exists
    if is_dragging:
        x1, y1, x2, y2 = normalize_rect(start_pt, end_pt)
        cv.rectangle(display, (x1, y1), (x2, y2), (0, 255, 0), 2)
    elif roi_rect is not None:
        x1, y1, x2, y2 = roi_rect
        cv.rectangle(display, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv.putText(
        display,
        "Drag ROI | r: reset | s: save | q: quit",
        (10, 30),
        cv.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 0),
        2,
        cv.LINE_AA
    )

    cv.imshow(WINDOW_MAIN, display)

    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    elif key == ord('r'):
        roi = None
        roi_rect = None
        cv.destroyWindow(WINDOW_ROI)  # optional: close ROI window if open

    elif key == ord('s'):
        if roi is None:
            print("[Info] No ROI selected yet. Drag to select an ROI first.")
        else:
            out_name = "roi.png"
            cv.imwrite(out_name, roi)
            print(f"[Saved] {out_name}")

cv.destroyAllWindows()