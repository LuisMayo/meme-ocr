from flask import Flask
from flask import request
from memeocr import MemeOCR
import wget
app = Flask(__name__)

@app.route('/')
def hello_world():
    url = request.args.get('imageurl', '')
    name = wget.download(url)
    ocr = MemeOCR()
    txt = ocr.recognize(name)
    return ''.join(txt)
if __name__ == "__main__":
    app.run()