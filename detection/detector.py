# detector.py
import mediapipe as mp
import cv2
import math
from HandCapture.src.audio.controller import volume

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


def create_hand_detector():
    return mp_hands.Hands(max_num_hands=2)


def detect_hand(frame, hands):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    middle_left_x = None
    middle_left_y = None
    middle_right_x = None
    middle_right_y = None
    dist_hand = 0

    frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_drawing.draw_landmarks(frame_bgr, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            label = handedness.classification[0].label

            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]

            h, w, _ = frame.shape
            x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
            x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

            cv2.line(frame_bgr, (x1, y1), (x2, y2), (255, 0, 0), thickness=2)

            if label == 'Left':

                middle_left_x = int((x1 + x2) / 2)
                middle_left_y = int((y1 + y2) / 2)

                cv2.circle(frame_bgr, (middle_left_x, middle_left_y), radius=5, color=(0, 255, 0), thickness=1)

            elif label == 'Right':

                middle_right_x = int((x1 + x2) / 2)
                middle_right_y = int((y1 + y2) / 2)

                cv2.circle(frame_bgr, (middle_right_x, middle_right_y), radius=5, color=(0, 255, 0), thickness=1)

            if (
                    middle_left_x is not None and middle_right_x is not None and
                    middle_left_y is not None and middle_right_y is not None
            ):
                cv2.line(frame_bgr, (middle_left_x, middle_left_y), (middle_right_x, middle_right_y),
                         (0, 255, 255), 2)

                dist_hand = math.sqrt((middle_left_x - middle_right_x) ** 2 + (middle_left_y - middle_right_y) ** 2)

            dist_fingers = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            volume(dist_fingers)

            print(f"{label} : Finger Distance: {dist_fingers:.2f} {dist_hand:.2f}")


    return frame_bgr
