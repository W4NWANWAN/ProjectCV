# Real-time Object Detection System

A Flask web application that uses the YOLOv8 model to detect objects from a webcam feed in real-time.

## Description

This project is a web application built using Flask (a Python framework) capable of performing real-time object detection through the user's webcam feed. The application leverages the power of the YOLOv8 model from Ultralytics to identify and localize various objects within the video frames. The detection results are displayed directly in the web interface, providing an interactive experience for the user.

## Key Features

*   **Real-time Object Detection:** Capable of detecting objects from a live webcam feed.
*   **YOLOv8 Model:** Utilizes the state-of-the-art YOLOv8 object detection model for high accuracy and speed.
*   **Interactive Web Interface:** Built with Flask and simple HTML/CSS to display the video feed and detection results.
*   **Easy to Use:** Relatively straightforward installation and usage process.

## Technologies Used

*   **Python:** The primary programming language used.
*   **Flask:** A micro web framework for building the application.
*   **OpenCV (cv2):** Library for image and video processing, including webcam feed capture.
*   **Ultralytics YOLOv8:** Library for implementing the YOLOv8 model.
*   **HTML/CSS:** For building the client-side user interface.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/USERNAME/REPOSITORY-NAME.git
    cd REPOSITORY-NAME
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # For Windows
    venv\Scripts\activate
    # For macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Ensure the `requirements.txt` file contains all necessary packages like `flask`, `opencv-python`, `ultralytics`)*

## Usage

1.  **Run the Flask Application:**
    ```bash
    python app.py
    ```
    *(Note: The main file name might differ, adjust if necessary)*

2.  **Open Your Browser:**
    Open your web browser and go to `http://127.0.0.1:5000/` (or the address displayed in your terminal).

3.  **Allow Webcam Access:**
    Your browser will ask for permission to access your webcam. Allow it.

4.  **View Detection:**
    Your webcam feed will be displayed on the web page, and detected objects will be marked with bounding boxes and class labels.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork this repository and create a pull request. You can also open an issue if you find a bug or have a feature suggestion.

## License

This project is licensed under the [LICENSE NAME, e.g., MIT License]. See the `LICENSE` file for more details.
---

**Additional Notes:**

*   Ensure you have a webcam connected and functioning correctly.
*   Detection performance may vary depending on your computer's hardware specifications.
*   You might need to install additional drivers for your webcam depending on your operating system.
*   The `requirements.txt` file must be created and should list all required Python dependencies. Example content for `requirements.txt`:
    ```
    Flask
    opencv-python
    ultralytics
    # Add other libraries if any
    ```
