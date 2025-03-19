import cv2
import numpy as np 
class Eyes_view:
    def set_camera(self):
        cap = cv2.VideoCapture(0)
        
        while True : 
            ret, frame = cap.read()
            if not ret:
                print("Failed to read camera! try again")
                continue
            height,width, _ = frame.shape
            focus_x,focus_y = width // 2, height // 2
            cv2.circle(frame,(focus_x,focus_y),150,(255,255,255),3)
            cv2.circle(frame,(focus_x,focus_y),100,(255,255,255),2)
            cv2.circle(frame,(focus_x,focus_y),50,(255,255,255),1)
            cv2.imshow("Camera",frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
