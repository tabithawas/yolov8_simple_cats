from ultralytics import YOLO
import cv2
import os

# Load a pretrained YOLOv8n model
model = YOLO("./simple_cats.pt")

def heic_to_png(input_folder, output_folder): 
    for filename in os.listdir(input_folder): 

        # Define path to the image file
        img_path = input_folder + "/" + filename

        # Run inference on the source
        results = model(img_path, conf=0.7)  
    
        # Visualize detection 
        results_img = results[0].plot() 

        cv2.imwrite(output_folder + "/" + filename, results_img)

input_folder = "./test_imgs"
output_folder = "./output_imgs"
heic_to_png(input_folder, output_folder)