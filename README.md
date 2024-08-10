# Neural Style Transfer Web App

A web application that allows users to apply neural style transfer to their images. This app utilizes TensorFlow and Flask to provide a simple and interactive way to stylize images using a pre-trained model.

## Features

- Upload images for content and style.
- Apply neural style transfer to the uploaded images.
- Download the stylized image.


## Installation

1. **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the Flask Server:**

    ```bash
    python app.py
    ```

2. **Open Your Web Browser:**

    Navigate to URL to access the web app.

## Usage

1. **Upload Images:**

   - Click on the "Choose File" button to upload your content and style images.
   - Make sure both images are in the correct formats (e.g., .jpg, .png).

2. **Apply Style Transfer:**

   - Click the "Upload" button to start the neural style transfer process.
   - Wait for the processing to complete.

3. **Download the Stylized Image:**

   - Once the process is complete, click the "Download Stylized Image" button to save the result to your device.



