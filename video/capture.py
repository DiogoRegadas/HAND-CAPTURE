# capture.py
import cv2

from HandCapture.src.detection.detector import detect_hand, create_hand_detector

def capture_vd():
    cam = cv2.VideoCapture(0)
    #cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    #cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

    hand_detector = create_hand_detector()

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_beta = detect_hand(frame, hand_detector)

        cv2.imshow('Camera', frame_beta)
        if cv2.waitKey(1) == ord('q'):
            break

    hand_detector.close()  # Liberta recursos
    cam.release()
    cv2.destroyAllWindows()
