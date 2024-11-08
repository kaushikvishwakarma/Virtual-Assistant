import cv2;
import mediapipe as mp
cap=cv2.VideoCapture(0)
hand_det=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
while True:
    _,  frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_height,frame_width,_=frame.shape
    rgbframe=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_det.process(rgbframe)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                print(x,y)
        

    
    cv2.imshow('video',frame)
    cv2.waitKey(1)
