# [2025-1] Computer Vision

동아대학교 소프트웨어대학 **컴퓨터비전** 과목의 실습, 과제, 프로젝트 결과물을 정리한 저장소입니다.

## 1. Course Information

- **Course**: Computer Vision
- **Semester**: [2025-1]
- **Instructor**: [서정일 교수님]
- **Department**: [AI학과]
- **Student Name**: [김정식]
- **Student ID**: [2343783]
- **GitHub**: [github.com/jsk4074]

---

## Repository Goal

이 저장소는 다음 목적을 위해 운영합니다.

- 주차별 실습 코드 정리
- 과제 결과물 업로드
- 실행 결과 이미지 및 분석 내용 기록
- Term Project 진행 내용 아카이브
- 과목 제출용 GitHub 링크 관리

---

## Development Environment

- **Language**: Python 3.x
- **Main Libraries**: OpenCV, NumPy, Matplotlib, scikit-image, PyTorch 
- **IDE / Tools**: VS Code / Jupyter Notebook / PyCharm
- **OS**: Ubuntu / macOS

### Example Environment

```bash
python --version
pip install opencv-python numpy matplotlib
```

---

## Repository Structure

<!-- ```bash
computer-vision/
├─ README.md
├─ week01_opencv_basics/
│  ├─ src/
│  ├─ images/
│  ├─ results/
│  └─ README.md
├─ week02_image_transformation/
│  ├─ src/
│  ├─ images/
│  ├─ results/
│  └─ README.md
├─ week03_edge_and_region/
├─ week04_local_feature/
├─ week05_image_recognition/
├─ week06_dynamic_vision/
├─ week07_vision_transformer/
└─ term_project/
   ├─ src/
   ├─ data/
   ├─ results/
   └─ README.md
``` -->

---

## Weekly Labs and Assignments

| Week | Topic | Folder | Status | Notes |
|---|---|---|---|---|
| W01 | OpenCV Basics / Orientation | `week01_opencv_basics` | [ ] | 이미지 로드, grayscale 변환 |
| W02 | Image Transformation | `week02_image_transformation` | [ ] | resize, rotate, affine/perspective |
| W03 | Edge and Region | `week03_edge_and_region` | [ ] | edge detection, segmentation |
| W04 | Local Feature | `week04_local_feature` | [ ] | corner, keypoint, descriptor |
| W05 | Image Recognition | `week05_image_recognition` | [ ] | classification / recognition |
| W06 | Dynamic Vision | `week06_dynamic_vision` | [ ] | motion, optical flow, tracking |
| W07 | Vision Transformer | `week07_vision_transformer` | [ ] | transformer-based vision model |
| Project | Term Project / Kaggle | `term_project` | [ ] | 개인 프로젝트 |

> `Status` 예시: `Done`, `In Progress`, `Not Started`

---

## What to Include for Each Assignment

각 주차 폴더에는 아래 내용을 포함합니다.

### Required
- `src/` : 실행 가능한 코드
- `images/` : 입력 이미지 또는 예제 데이터
- `results/` : 실행 결과 이미지, 그래프, 캡처 화면
- `README.md` : 실습/과제 설명

### Recommended README Format for Each Week
- **Objective**: 실습 목표
- **Main Functions / Algorithms**: 사용한 함수나 알고리즘
- **How to Run**: 실행 방법
- **Results**: 결과 이미지 및 해석
- **Issues / Fixes**: 에러와 해결 방법
- **What I Learned**: 배운 점

---

## Example: Weekly README Template

````md
# Week 01 - OpenCV Basics

## Objective
- OpenCV를 사용해 이미지를 불러오고 grayscale 이미지로 변환한다.

## Main Code
- cv.imread()
- cv.cvtColor()
- np.hstack()
- cv.imshow()
- cv.waitKey()

## How to Run
```bash
python main.py
```

## Results
- Original image와 grayscale image를 나란히 출력하였다.

## Issues / Fixes
- grayscale 이미지는 channel 수가 달라서 `np.hstack()` 전에 `cv.COLOR_GRAY2BGR` 변환이 필요했다.

## What I Learned
- OpenCV의 기본 이미지 입출력 흐름을 이해했다.
````

---

## Execution Guide

예시 실행 방법:

```bash
cd week01_opencv_basics/src
python main.py
```

또는 Jupyter Notebook 사용 시:

```bash
jupyter notebook
```

---

## Results Preview

각 실습 결과는 아래처럼 정리합니다.

- **Input**: 원본 이미지
- **Processing**: grayscale / edge / transform / feature extraction
- **Output**: 처리 결과 이미지
- **Analysis**: 결과가 왜 그렇게 나왔는지 간단한 설명

예시:

````md
### Example Result
| Original | Grayscale |
|---|---|
| ![](./results/original.png) | ![](./results/grayscale.png) |
````

---

## Term Project

````md

# Term Project

## Title
[프로젝트 제목]

## Task
[예: Image Classification / Object Detection / Segmentation]

## Dataset
[사용한 데이터셋 이름 및 링크]

## Model
[사용한 모델 구조]

## Evaluation
[Accuracy / F1-score / mAP 등]

## Results
[정량 결과 + 정성 결과]

## Report
[프로젝트 요약]

---

## References

- OpenCV Documentation
- Course Slides
- Textbook / Papers / Online Tutorials used in this repository

---

## Memo

- [수업 중 메모할 내용 작성]

