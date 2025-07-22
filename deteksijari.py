import cv2
import mediapipe as mp

# inisialisasi modul mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# fungsi cek jari terbuka atau tidak
def jari_terbuka(lm_list):
    jari = []
    # ibu jari (arah x karena posisinya horizontal)
    jari.append(lm_list[4].x < lm_list[3].x)
    # jari telunjuk sampai kelingking (arah y karena vertikal)
    jari.append(lm_list[8].y < lm_list[6].y)
    jari.append(lm_list[12].y < lm_list[10].y)
    jari.append(lm_list[16].y < lm_list[14].y)
    jari.append(lm_list[20].y < lm_list[18].y)
    return jari

# buka kamera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        print("kamera tidak bisa diakses 😭")
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = hand_landmarks.landmark
            status_jari = jari_terbuka(lm_list)

            # cek gesture: I LOVE YOU 🤟
            if status_jari[0] and status_jari[1] and not status_jari[2] and not status_jari[3] and status_jari[4]:
                cv2.putText(img, 'I LOVE YOU 🤟', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 3)

            # gambar landmark tangan
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gesture I LOVE YOU", img)

    # pencet tombol 'q' buat keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# bersihkan
cap.release()
cv2.destroyAllWindows()