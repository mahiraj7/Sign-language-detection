import cv2
import time
import mediapipe as mp
from yes_sign import *
from no_sign import *

mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

capture = cv2.VideoCapture(0)
previousTime = 0
currentTime = 0


while capture.isOpened:
    ret, frame = capture.read()
    frame = cv2.resize(frame, (800,600))
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = holistic_model.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.left_hand_landmarks:
        is_no_sign = check_no_sign(results.left_hand_landmarks, 'left')
        is_yes_sign = check_yes_sign(results.left_hand_landmarks, 'left')
        if is_no_sign:
            cv2.putText(image, f"Left: No", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif is_yes_sign:
            cv2.putText(image, f"Left: Yes", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if results.right_hand_landmarks:
        is_no_sign = check_no_sign(results.right_hand_landmarks, 'right')
        is_yes_sign = check_yes_sign(results.right_hand_landmarks, 'right')
        if is_no_sign:
            cv2.putText(image, f"Right: No", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif is_yes_sign:
            cv2.putText(image, f"Right: Yes", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime

    cv2.putText(image, f"FPS: {int(fps)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Recognition", image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
