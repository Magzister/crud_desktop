import cv2
import requests
import time
import threading
import json


CHECK_ACCESS_URL = 'http://localhost:8000/accesses/get-access-with-key/{id}/'


class DeviceProcess:
    def __init__(self, object_id, object_name, cap):
        self.object_id = object_id
        self.cap = cap
        self.object_name = object_name
        self.event = False
        self.is_access = False

    def run(self):
        try:
            while True:
                ret, frame = self.cap.read()

                if ret:

                    cv2.putText(frame, str(self.object_id), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))

                    qrDecoder = cv2.QRCodeDetector()
                    data, bbox, rectifiedImage = qrDecoder.detectAndDecode(frame)
                    if len(data) > 0:

                        print("Decoded Data : {}".format(data))

                        if not self.event:
                            t = threading.Thread(target=self.make_request, args=(data, self.object_id))
                            t.start()
                        else:
                            if self.is_access:
                                frame = self.access(frame)
                            else:
                                frame = self.reject(frame)

                        cv2.imshow(self.object_name + str(self.object_id), frame)

                    else:
                        cv2.imshow(self.object_name + str(self.object_id), frame)

                key = cv2.waitKey(10)
                if key == 27:
                    break
        finally:
            cv2.destroyAllWindows()

    def make_request(self, code, object_id):
        url = CHECK_ACCESS_URL.format(
            id=object_id
        )
        data = {
            "code": code
        }
        response = requests.get(url=url, data=json.dumps(data))
        if response.status_code == 200:
            self.event = True
            self.is_access = True
            time.sleep(2)
            self.event = False
        else:
            self.event = True
            self.is_access = False
            time.sleep(2)
            self.event = False

    @staticmethod
    def access(frame):
        cv2.putText(frame, 'ACCESS', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0))
        return frame

    @staticmethod
    def reject(frame):
        cv2.putText(frame, 'REJECT', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255))
        return frame