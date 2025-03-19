import cv2
import numpy as np 
from ultralytics import YOLO
class Vision_View:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")
        self.cap = cv2.VideoCapture(0)

    def detect_object(self):
        while True : 
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to read camera! try again")
                continue

            height,width, _ = frame.shape
            focus_x,focus_y = width // 2, height // 2
            results = self.model(frame)
            for result in results:
                for box in result.boxes.xyxy:
                    x1,y1,x2,y2 = map(int,box)
                    obj_center_x = (x1 + x2) // 2
                    obj_center_y = (y1 + y2) // 2
                    distance = np.sqrt((focus_x - obj_center_x)**2 + (focus_y - obj_center_y) ** 2)
                    if distance < 150:
                        label = result.names[result.boxes.cls[0].item()]
                        cv2.putText(frame,label,(x1,y1 - 10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
                        cv2.rectangle(frame,(x1,y1),(x2,y2),(255,255,255),2)
            cv2.imshow("Tracking",frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()
