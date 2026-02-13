import cv2
import mediapipe as mp
import math

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

tipIds = [4, 8, 12, 16, 20]

video = cv2.VideoCapture(0)

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])*2 + (point1[1] - point2[1])*2)

def are_keypoints_visible(lmList, keypoints):
    # Check if the keypoints are visible on the screen
    return all(id < len(lmList) for id in keypoints)

with mp_hand.Hands(min_detection_confidence=0.5,
                   min_tracking_confidence=0.5) as hands:
    while True:
        ret, image = video.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
        
        gesture = "None"
        if len(lmList) != 0:
            # Check for BREATH gesture: All four keypoints (4, 8, 12, 16) are visible
            if are_keypoints_visible(lmList, [4, 8, 12, 16]):
                gesture = "BREATH"

            # Check for CALL gesture: Thumb extended, other fingers downward
            thumb_extended = lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]
            all_fingers_down = all(lmList[tipIds[i]][2] > lmList[tipIds[i] - 2][2] for i in range(1, 5))
            if thumb_extended and all_fingers_down:
                gesture = "CALL"

            # Check for ALLOW gesture: Index finger extended, other fingers downward
            index_finger_extended = lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]
            other_fingers_closed = all(lmList[tipIds[i]][2] > lmList[tipIds[i] - 2][2] for i in range(2, 5))
            if index_finger_extended and other_fingers_closed:
                gesture = "ALLOW"

            # Check for O gesture: Thumb and Index finger touching, other fingers straight
            thumb_tip = (lmList[tipIds[0]][1], lmList[tipIds[0]][2])
            index_tip = (lmList[tipIds[1]][1], lmList[tipIds[1]][2])
            distance_thumb_index = calculate_distance(thumb_tip, index_tip)

            thumb_extended = lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]
            index_finger_extended = lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]
            other_fingers_straight = all(lmList[tipIds[i]][2] < lmList[tipIds[i] - 2][2] for i in range(2, 5))

            if distance_thumb_index < 50 and thumb_extended and index_finger_extended and other_fingers_straight:
                gesture = "O"

            # Display text box with the detected gesture
            cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
            cv2.putText(image, gesture, (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
        
        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
