# Hand Capture Volume Controller

![Status](https://img.shields.io/badge/status-work--in--progress-orange)
![Language](https://img.shields.io/badge/language-Python-green)
![Library](https://img.shields.io/badge/library-OpenCV-red)

A Python application that uses OpenCV to detect a hand through the webcam and adjusts the **system volume** based on the distance between two specific landmarks: the thumb and the index finger.  
The farther the fingers move from each other, the higher the volume — the closer they are, the lower the volume.

A simple but effective demonstration of gesture-based interaction and computer vision.

---

## 🔍 Features

- Real-time hand tracking using OpenCV  
- Landmark detection to identify thumb and index finger positions  
- Distance calculation used to control system volume  
- Smooth and intuitive gesture-based interaction  
- Works with any standard webcam  
- No buttons or GUI — fully gesture-controlled

---

## 🛠️ Technologies Used

- **Python**  
- **OpenCV** – camera capture + hand detection  
- **Mediapipe Hands** 
- **Numpy** – mathematical calculations  
- **System volume control library**  
  (e.g., `pycaw` on Windows or equivalent for your OS)

---

## 🧠 How It Works

1. The webcam feed is read frame-by-frame using OpenCV.  
2. A hand-tracking model detects **21 hand landmarks** in real time.  
3. Two specific landmarks are extracted:
   - Thumb tip  
   - Index finger tip  
4. The Euclidean distance between these two landmarks is calculated.  
5. That distance is mapped to a volume range, typically:
   - **Small distance → low volume**  
   - **Large distance → high volume**  
6. The program sends volume-change commands to the operating system.  
7. Visual feedback (a line or circle) may be drawn on the video feed to show detection.

This project demonstrates concepts from:

- Real-time computer vision  
- Gesture recognition  
- Hand landmark processing  
- Mapping physical movement to system actions  
- Interactive and intuitive user experience design  

---

## 🔮 Future Improvements

- Add additional gestures (mute, pause, skip)  
- Integrate with media apps (Spotify API, VLC, YouTube)  
- Add smoothing filters to make volume transitions even more natural  
- Display a UI bar with the current volume level  
- Multi-hand controls (left hand = volume, right hand = playback)

---

## 👤 Author

**Diogo Regadas**  
[GitHub Profile](https://github.com/DiogoRegadas)
