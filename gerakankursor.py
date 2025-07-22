import cv2
import mediapipe as mp
import pyautogui
import math
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
last_click_time = 0
last_distance = 1
last_double_click_time = 0

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            x1 = hand_landmarks.landmark[8].x
            y1 = hand_landmarks.landmark[8].y
            x2 = hand_landmarks.landmark[4].x
            y2 = hand_landmarks.landmark[4].y

            h, w, _ = img.shape
            cx, cy = int(x1 * w), int(y1 * h)
            cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

            cursor_x = int(screen_width * x1)
            cursor_y = int(screen_height * y1)
            pyautogui.moveTo(cursor_x, cursor_y)

            distance = math.hypot(x2 - x1, y2 - y1)
            cv2.putText(img, f"Jarak: {round(distance, 4)}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            current_time = time.time()
            if distance < 0.05:
                if current_time - last_click_time > 1:
                    pyautogui.click()
                    print("Klik kiri")
                    last_click_time = current_time

                if last_distance > 0.1 and current_time - last_double_click_time < 0.5:
                    pyautogui.doubleClick()
                    print("Double Klik")
                    last_double_click_time = 0
                else:
                    last_double_click_time = current_time

            last_distance = distance

    cv2.imshow("Debug Webcam", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()