# 🖐️ Hand Gesture Based Game Automation 🎮

This project lets you **control a game using your hand gestures** detected through a webcam, powered by **MediaPipe** and **OpenCV**.

### 🚀 What It Does
- Detects hand gestures using a webcam
- Recognizes:
  - ✊ Fist → **Brake** (`A` key)
  - 🖐️ Open Palm → **Accelerate** (`D` key)
- Presses or releases keys accordingly using Python

> No need for a controller or keyboard — just your hand!

---

## 📸 Demo

![Demo](hand_landmarks.png)

---

## 🛠️ Tech Stack & Libraries Used

| Library       | Purpose                                    |
|---------------|---------------------------------------------|
| `opencv-python` | Webcam access, frame capture, and display |
| `mediapipe`   | Hand landmark detection                    |
| `pynput`      | Simulate keyboard presses                  |
| `time` (builtin) | For sleep/delay timing                 |

---

## 🧠 How It Works

### 👋 Gesture Detection Logic
- **Thumb** is checked differently due to its lateral movement
- **Other fingers** are checked by comparing tip and base joint y-coordinates
- Count of "up" fingers is used to decide the action:
  - **0 fingers up** → Fist → Press `'A'` key (Brake)
  - **5 fingers up** → Open Palm → Press `'D'` key (Accelerate)

### 🎮 Key Simulation
- The `directkeys.py` file uses `pynput`'s `Controller` to simulate keypresses:
  ```python
  keyboard.press('d')  # Accelerate
  keyboard.release('a')  # Stop Brake

## 🧑‍💻 How to Run This Project

### 🐍 1. Clone the Repository
```
git clone https://github.com/Sohail22515/Game_Automation.git
cd Game_Automation
```

### 📦 2. Set Up a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 📜 3. Install Dependencies
```
pip install -r requirements.txt
```
### 🏁 4. Run the App
```
python main.py
```

