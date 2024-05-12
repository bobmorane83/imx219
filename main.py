from camera import Camera
from flask import Flask, request
import base64

app = Flask(__name__)

cam = Camera()

@app.route("/capture", methods=['GET'])
def capture():
    img = cam.capture()

    data = img.getvalue()         # get data from file (BytesIO)

    data = base64.b64encode(data) # convert to base64 as bytes
    data = data.decode()          # convert bytes to string

    return(f'<img src="data:image/png;base64,{format(data)}">')


    # pylab.savefig(data, format = 'png')
    # str_equivalent_image = base64.b64encode(data.getvalue()).decode()
    # img_tag = "<img src='data:image/png;base64," + str_equivalent_image + "'/>"

    # return f"captured : <img>{data}<\img>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')