from picamera2 import Picamera2, Preview
import time
import io

class Camera():
    def __init__(self):
        try:
            self.picam2 = Picamera2()
            self.camera_config = self.picam2.create_preview_configuration()
            self.picam2.configure(self.camera_config)
            self.picam2.start_preview(Preview.NULL)
            self.picam2.start()
        except Exception as e:
            raise e

    def capture(self):
        try:
            data = io.BytesIO()
            self.picam2.capture_file(data, format='png')
            return data
        except Exception as e:
            raise e