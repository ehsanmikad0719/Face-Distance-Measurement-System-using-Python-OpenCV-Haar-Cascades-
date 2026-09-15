# Face-Distance-Measurement-System-using-Python-OpenCV-Haar-Cascades-

# Face Distance Measurement System

A real-time computer vision application built with Python and OpenCV that estimates the distance between a person's face and the webcam. The project utilizes **Haar Cascade Classifiers** for face detection and applies a **triangle similarity framework** to calculate depth.

## 🚀 Features
* **Real-time Detection:** Rapid face tracking using OpenCV's built-in Haar Cascade algorithm.
* **Distance Estimation:** Computes the live distance of an adult human face from the camera in centimeters.
* **On-Screen Display (OSD):** Draws a bounding box around the detected face and overlays the live distance metric.

## 📐 How it Works
The system uses the mathematical principle of triangle similarity to estimate depth:
Distance = (Real Face Width × Focal Length) ÷ Face Width in Pixels

* **Average Human Face Width:** Set to a standard 14.0 cm
* **Focal Length:** Pre-calibrated to 750.0pixels. *Note: For maximum accuracy, you can calibrate this value specifically for your webcam.*

## 📋 Prerequisites
Ensure you have Python installed on your system along with the `opencv-python` library.

### Installation
Install the required dependency using pip:
```bash
pip install opencv-python
```

## 🛠️ Usage
1. Clone this repository or copy the script to your local machine.
2. Run the script:
   ```bash
   python main.py
   ```
3. A window will open showing your webcam feed.
4. Press **`q`** on your keyboard to exit the application.

## ⚙️ Configuration
You can fine-tune the parameters inside the script to match your setup:
* `REAL_FACE_WIDTH`: Adjust this if measuring children or specific objects.
* `Focal Length`: Recalibrate if the distance metrics feel too high or low for your specific camera sensor.
* `minNeighbors` / `scaleFactor`: Tweak these in `detectMultiScale` to change face detection sensitivity and reduce false positives.

## 📄 License
This project is open-source.
