# 🦺 Real-Time PPE Detection System

A **real-time Personal Protective Equipment (PPE) detection system** using **YOLO (Ultralytics)** and **OpenCV**.  
It detects **persons, helmets, and absence of helmets** from webcam feed and gives instant visual feedback whether PPE is properly worn.

---

## 🛠 Technologies Used
- **Python**  
- **Ultralytics YOLO** – Object detection model  
- **OpenCV** – For video capture and visualization  
- **Computer Vision** – Real-time detection  
- Pre-trained **YOLO model** (`best.pt`) for PPE detection  

---

## ⚡ Features
- Detects **person**, **helmet**, and **no_helmet** in real-time  
- Displays **bounding boxes** and labels on detected objects  
- Shows **PPE compliance status**:
  - 🟢 `PPE OK` – helmet detected on person  
  - 🔴 `PPE NOT OK` – helmet missing  
- Works with default webcam (or any connected camera)  

---

## 🧠 How It Works

The YOLO model (best.pt) is loaded using Ultralytics.

The webcam captures frames in real-time.

Each frame is processed by the model to detect person, helmet, and no_helmet.

Bounding boxes and labels are drawn on the frame.

If a person is detected:

Helmet detected → PPE OK (green)

No helmet detected → PPE NOT OK (red)

The final annotated frame is displayed live.

## 🔗 References

Ultralytics YOLO

OpenCV Documentation


---

## 💻 How to Run
1. Clone the repository:
```bash
git clone https://github.com/yourusername/ppe-detection.git
