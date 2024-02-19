# Detection of E-Waste using OpenCV and YOLOv8

Trained YOLOv8 on a dataset of electronics from Google's Open Image Dataset for detection and segmentation. The model is able to identify various types of electronic waste, including mobile phone, computer mouse, computer keyboard, printer, computer monitor, headphones.
This project is an implementation of the object detection model, YOLOv8 for detecting electronic  waste (E-waste) in images. The code uses OpenCV to read, preprocess and visualize the results from the model with an border around the detected object with an cofidence percentage.
Integrated this into a WebApp using Flask. 
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)


## Installation

Run the following commands to install the required libraries.
```bash
pip install -r requirements.txt
```

[Link to the prepared dataset](#https://drive.google.com/drive/folders/1YBtsNDSrWJjjTbAtVTglOW_B_BOz2-eY?usp=sharing)

## usage
To run the FLask WebApp.
```bash
python app.py
```

To run the CV , simply run the following command.
```bash
python main.py
```

