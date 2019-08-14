# Read Me

This program is based on my prior project that is linked [here](https://github.com/Russel-Mendes/Medical_Vision_Classifier). In that project, I sought to create a Convolution Neural Network that could identify medical images on the basic wound types. For my AP CSP exam, I created a terminal application of that project which is showcased in this repository. This program can do a variety of features, such as automatically classifying an entire directory, identifying a specific image, and keeping track of program history. Most features of the program is self explanatory, and the code itself is organized and readable.

## Getting Started

This projects has two components: MVCS.h5 and Terminal_Identification.py. In order to use this program, both files has to be in the same directory to function. Additionally, the path or directory of the image in question must be known before this program can function.

## Prerequisites
These are the libraries used during development. 
-Python 3.6+ 
-Tensorflow 1.12.0
-Keras 2.1.6 -- this version of Keras is stable in loading weights 
-Pillow 5.3.0 -- used for image handling

## Components
This section will explain the part of the program. 
-MVC2.h5 -- This file is the model weights that was trained in the Medical Image Classifier Project. This file is necessary for image recognition.
-Terminal_Identification.py -- This file is the program that executes the project

## Build With
Spyder -- a python code editor

## Author
Russel Mendes