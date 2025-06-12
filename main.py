import cv2
import mediapipe as mp
import time
from directkeys import PressKey, ReleaseKey

# Define key mappings
right_pressed = 'd'
left_pressed = 'a'

# Delay to allow user to prepare
time.sleep(2.0)
current_key_pressed = set()

# Initialize MediaPipe
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

# Fingertip landmark IDs
tipIds = [4, 8, 12, 16, 20]

# Start webcam
video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        keyPressed = False
        key_count = 0
        key_pressed = 0

        ret, image = video.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmark.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)

        fingers = []
        if len(lmList) != 0:
            # Thumb (tipIds[0])
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other four fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total = fingers.count(1)

            # Fist detected (0 fingers) -> BRAKE
            if total == 0:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
                PressKey(left_pressed)
                current_key_pressed.add(left_pressed)
                key_pressed = left_pressed
                keyPressed = True
                key_count += 1

            # Open palm (5 fingers) -> ACCELERATE
            elif total == 5:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, " GAS", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
                PressKey(right_pressed)
                current_key_pressed.add(right_pressed)
                key_pressed = right_pressed
                keyPressed = True
                key_count += 1

        # Release keys if no gesture is detected
        if not keyPressed and len(current_key_pressed) != 0:
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()

        # If one key should remain pressed
        elif key_count == 1 and len(current_key_pressed) == 2:
            for key in current_key_pressed:
                if key_pressed != key:
                    ReleaseKey(key)
            current_key_pressed = set()
            current_key_pressed.add(key_pressed)

        cv2.imshow("Frame", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
