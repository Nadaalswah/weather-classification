# Weather Recognition Classifier using EfficientNetB4 ⛈️

## Overview
This project implements a web-app weather recognition classifier using deep learning with EfficientNetB4 architecture. The classifier is trained to classify images into 11 weather classes, including hail, snow, glaze, lightning, fog smog, frost, dew, rain, rainbow, rime, and sandstorm.

## Dataset
The classifier is trained on the [Weather Dataset](https://www.kaggle.com/datasets/jehanbhathena/weather-dataset) available on Kaggle. This dataset contains labeled images representing various weather conditions.

## Model Architecture
The classifier utilizes the EfficientNetB4 architecture, a state-of-the-art convolutional neural network (CNN) known for its efficiency and effectiveness in image classification tasks. 
EfficientNetB4 is a convolutional neural network architecture that belongs to the EfficientNet family, introduced by Mingxing Tan and Quoc V. Le in 2019. It is designed to balance model size and accuracy by scaling the depth, width, and resolution of the network in an optimal manner. EfficientNetB4 is one of the larger variants in the series, offering better performance at the cost of increased computational resources compared to smaller variants like EfficientNetB0 or B1. It has been widely used for various computer vision tasks, including image classification, object detection, and segmentation.

EfficientNetB4 offers a good balance between model size and performance, making it suitable for deployment on resource-constrained devices.



## Deployment
The model is deployed using a Flask web application, allowing users to interact with it by uploading images and receiving predictions on weather conditions in real time. The deployed application achieves 91% accuracy on the test set, demonstrating its effectiveness in recognizing weather patterns.

Project Link: [Weather Classification Website](https://weather-classification-2.onrender.com/)
