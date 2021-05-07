import cv2


class DeviceProcess:
    def __init__(self, object_id):
        self.object_id = object_id
        self.cap = cv2.VideoCapture(0)

    def run(self):
        while True:
            ret, frame = self.cap.read()

            cv2.putText(frame, str(self.object_id), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()