import cv2


class DeviceProcess:
    def __init__(self, object_id, object_name, cap):
        self.object_id = object_id
        self.cap = cap
        self.object_name = object_name

    def run(self):
        try:
            while True:
                ret, frame = self.cap.read()

                cv2.putText(frame, str(self.object_id), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))

                cv2.imshow(self.object_name, frame)
                key = cv2.waitKey(10)
                if key == 27:
                    break
        finally:
            self.cap.release()
            cv2.destroyAllWindows()
