import os
from flask import Flask, request, render_template, send_file
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

app = Flask(__name__)

model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content_file = request.files['content']
        style_file = request.files['style']

        content_path = os.path.join('uploads', content_file.filename)
        style_path = os.path.join('uploads', style_file.filename)

        content_file.save(content_path)
        style_file.save(style_path)

        content_image = load_image(content_path)
        style_image = load_image(style_path)

        try:
            stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]

            output_image = tf.image.convert_image_dtype(stylized_image, dtype=tf.uint8)
            output_image = tf.image.encode_jpeg(tf.squeeze(output_image))
            output_path = os.path.join('outputs', 'stylized_image.jpg')
            tf.io.write_file(output_path, output_image)

            return send_file(output_path, mimetype='image/jpeg')

        except tf.errors.InvalidArgumentError as e:
            print(f"Error: {e}")
            print(f"Content Image Shape: {content_image.shape}")
            print(f"Style Image Shape: {style_image.shape}")
            return render_template('index.html', error="An error occurred during style transfer. Please try again.")

    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    app.run(debug=True)
