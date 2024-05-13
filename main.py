from camera import Camera
from flask import Flask, request
import base64
import requests
import io

app = Flask(__name__)

cam = Camera()

@app.route("/capture", methods=['GET'])
def capture():
    img = cam.capture()

    files=[('image',('photo.png',img.getvalue(),'image/png'))]

    data = img.getvalue()         # get data from file (BytesIO)
    data = base64.b64encode(data) # convert to base64 as bytes
    data = data.decode()          # convert bytes to string

    payload={}
    headers = {}

    response = requests.request("POST", "http://localhost:5001/display", headers=headers, data=payload, files=files)
    return(f'<img src="data:image/png;base64,{format(data)}"> Response : {response.content}')

if __name__ == "__main__":
    app.run(host='0.0.0.0')