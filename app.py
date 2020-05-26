from flask import Flask
from flask import request
from memeocr import MemeOCR
import base64
import wget
app = Flask(__name__)

@app.route('/')
def hello_world():
    url = request.args.get('imageurl', None)
    if url != None:
        name = wget.download(url)
    else:
        # image_64_encode = request.args.get('image64', '')
        # image_64_decode = base64.b64decode(image_64_encode)
        # image_result = open('decode', 'wb')
        # image_result.write(image_64_decode)
        # nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
        # name = 'decode'
    ocr = MemeOCR()
    txt = ocr.recognize(name)
    return ''.join(txt)
if __name__ == "__main__":
    app.run()