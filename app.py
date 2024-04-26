from flask import Flask, render_template, request
import base64
from tensorflow.keras.preprocessing.image import load_img, img_to_array, array_to_img
from tensorflow.keras.models import load_model
import numpy as np
from io import BytesIO
from PIL import UnidentifiedImageError

labels = {
    0: 'dew',
    1: 'fog smog',
    2: 'frost',
    3: 'glaze',
    4: 'hail',
    5: 'lightning',
    6: 'rain',
    7: 'rainbow',
    8: 'rime',
    9: 'sandstorm',
    10: 'snow'
}

app = Flask(__name__)
allowed_extensions = ['.jpg', '.jpeg', '.png']

# Load the model once during application startup
model = load_model('./model/densenet-121.h5')

def preprocess_image(image):
    image = img_to_array(image) / 255.
    return np.expand_dims(image, axis=0)

def close_streams(streams):
    for stream in streams:
        stream.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['image']
        if not any(file.filename.lower().endswith(ext) for ext in allowed_extensions):
            allowed_extensions_str = ', '.join(allowed_extensions)
            return render_template('index.html', prediction=f'Error: Only {allowed_extensions_str} files are allowed')

        image_stream = file.stream
        image = load_img(BytesIO(image_stream.read()), target_size=(224, 224))
        image_stream.seek(0)  # Reset stream position to beginning
        image_data = None  # Initialize image data

        try:
            image = preprocess_image(image)
            predicted_class = np.argmax(model.predict(image))
            buffered = BytesIO()
            array_to_img(image[0]).save(buffered, format="JPEG")
            image_data = base64.b64encode(buffered.getvalue()).decode("utf-8")
            return render_template('index.html', prediction=labels[predicted_class].capitalize(), uploaded_image=image_data)
        except UnidentifiedImageError as e:
            return render_template('index.html', prediction=f'Error: Unable to identify the image file. {e}')
        finally:
            close_streams([image_stream, buffered])  # Close streams to release resources

    except Exception as e:
        return render_template('index.html', prediction=f'Error: {e}')

if __name__ == '__main__':
    app.run(port=8060)
