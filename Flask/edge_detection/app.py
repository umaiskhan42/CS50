import cv2
import gradio as gr
import numpy as np

def edge_detection(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply edge detection
    edges = cv2.Canny(gray_image, 100, 200)
    return edges

# Gradio interface
iface = gr.Interface(
    fn=edge_detection,
    inputs=gr.Image(type="numpy"),
    outputs="image",
    title="Edge Detection with OpenCV",
    description="Upload an image and get the edges detected using OpenCV's Canny edge detector."
)

iface.launch(share=True)
