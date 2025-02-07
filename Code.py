!pip install mediapipe opencv-python

import mediapipe as mp
import cv2

mp_drawing=mp.solutions.drawing_utils
mp_holistic=mp.solutions.holistic

cap=cv2.VideoCapture(0)
while cap.isOpened():
  ret,frame=cap.read()
  cv2.imshow("Raw Webcam Feed",frame)

  if cv2.waitKey(10) & 0xFF==ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()




cap=cv2.VideoCapture(0)
#Initiate Holistic model
with mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:

    while cap.isOpened():
        ret,frame=cap.read()
        
        #Recolor Feed
        image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        #Make detections
        results=holistic.process(image)
        print(results.pose_landmarks)
        
        #face_landmarks, pose_landmarks, left_hand_landmarks, right_hand_landmarks
        
        #Recolor image back to BGR for rendering
        image=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        
        #Draw Face landmarks
        mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_holistic.POSE_CONNECTIONS)
        
        cv2.imshow("Raw Webcam Feed",image)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break

cap.release()
cv2.destroyAllWindows()