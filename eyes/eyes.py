import cv2

class eyes_view:
    def set_camera(self):
        cap = cv2.VideoCapture(0)

        while True : 
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Camera",frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
