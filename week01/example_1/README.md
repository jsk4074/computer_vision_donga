# Example 1 — Load Image + Grayscale

**File:** `1.py`  
**Goal:** Load an image using OpenCV, convert it to grayscale, and display the original and grayscale images side-by-side.

## What you learn
- `cv.imread()` to load an image
- `cv.cvtColor(..., cv.COLOR_BGR2GRAY)` for grayscale conversion
- `np.hstack()` to display images side-by-side
- `cv.imshow()` + `cv.waitKey()` for visualization

## Run
From the repository root:
![Result](./Result%201%20image.png)

```bash
python example_1/1.py