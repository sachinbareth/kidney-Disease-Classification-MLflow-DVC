import numpy as np
import os

try:
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing import image
except ImportError as e:
    error_message = str(e)

class PredictionPipeline:
    class_labels = ['Cyst', 'Normal', 'Stone', 'Tumor']

    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        if 'error_message' in locals():
            return {"error": error_message}
        
        # load model
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        
        # Make prediction
        predictions = model.predict(test_image)
        result_class = self.class_labels[np.argmax(predictions)]
        # print("Predicted class:", result_class)

        return {"image": result_class}