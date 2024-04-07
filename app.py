from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from src.cnnClassifier.utils.common import decodeImage
from src.cnnClassifier.pipeline.prediction import PredictionPipeline
import base64

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image_data = request.json['image']
    decodeImage(image_data, clApp.filename)
    result = clApp.classifier.predict()

    # Encode image data to base64
    with open(clApp.filename, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    # Return the result and encoded image data as a list
    return jsonify([result, {"image": encoded_image}])

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080) # for AWS