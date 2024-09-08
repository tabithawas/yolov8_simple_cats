# About  

This contains an object detection model that was trained on a small dataset of cats. The dataset was created using Roboflow. 

# Future 

There will be files added to perform inference on existing videos and real-time object detection. 

# Detailed Process

### Dataset creation 

Some of the images are pictures that I have taken, and some of the pictures were collected from Google (the Google image results were filtered by having a Creative Commons license). 

The images were uploaded to Roboflow. I annotated all of the images with rectangular bounding boxes. 

The dataset split is 70% / 20% / 10% which resulted in 57 training images, 13 validation images, and 10 test images. 

The dataset had the following preprocessing steps applied: 
- Auto-Orient: Applied 
- Resize: Stretch to 640x640 

The data set had the following augmentations applied: 
- Flip: Horizontal, Vertical 
- 90 degree Rotate: Clockwise, Counter-Clockwise
- Grayscale: Apply to 15% of images 
- Saturation: Between -25% and +25% 
- Brightness: Between -15% and +15% 
- Exposure: Between -10% and +10% 
- Noise: Up to 0.89% of pixels 

This resulted in 3 times the number of training images, so the final numbers for the dataset were 138 training images, 13 validation images, and 6 test images. This was a split of 88% / 8% / 4%. 

### Training 

The dataset was trained using yolov8. It trained with for 100 epochs and the imgsz paramater was set to 640. The **yolov8n.pt** model was used as the base pretrained model. This model is automatically downloaded when the training is run. 

The training took just under 1 hour. 

### Model 

The **simple_cats.pt** file is the model created during training. It was originally the **last.pt** file that resulted from the training. 

### Existing Image Inference 

The **img_inference.py** file performs inference on existing images. It takes in a folder of images and saves the resulting images and their bounding boxes to another folder. 

The results are filtered for 70% confidence. 

The **test_imgs** folder contains some testing images that were not included in the dataset. The **output_imgs** folder contains the results from running **img_inference.py** on the **test_imgs** folder. The results are pretty good considering the small dataset. 

