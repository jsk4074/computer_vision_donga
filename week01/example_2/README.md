
---

## `example_2/README.md`

```markdown
# Example 2 — Painting + Brush Size Control

**File:** `2.py`  
**Goal:** Paint on an image using mouse input, and control brush size using keyboard input.

## Controls
- Left drag: Blue brush
- Right drag: Red brush
- `+`: brush size +1
- `-`: brush size -1
- `q`: quit

## What you learn
- `cv.setMouseCallback()` for mouse events
- `cv.circle()` to draw strokes
- `cv.waitKey(1)` for real-time key input
- Managing state (brush size, pressed mouse button)

## Run
From the repository root:
![Result](./Result%202%20inpaint.png)

```bash
python example_2/2.py