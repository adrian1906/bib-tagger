# -*- coding: utf-8 -*-
"""
Created on Fri May  4 10:38:44 2018

@author: adrian.a.hood
"""

from skimage import io
import dlib
import os
import cv2
from scipy.io import loadmat


def train_detector(FolderName_Class, Annotation_Path,DetectorOutputFolder):
    # Set Default Options
    options=dlib.simple_object_detector_training_options()
    images=[]
    imagename=[]
    boxes=[]
    annotations=[]
    exts = ['.bmp', '.pbm', '.pgm', '.ppm', '.sr', '.ras', '.jpeg', '.jpg',
            '.jpe', '.jp2', '.tiff', '.tif', '.png']
    # Loop over all images inside the specified folder (single class)
    myImageList = os.listdir(FolderName_Class)
    for imagefilename in myImageList:
        name,ext = os.path.splitext(imagefilename)
        if ext in exts:
            images.append(cv2.imread(imagefilename))
            imagename.append(name)
            annotations = loadmat(os.path.join(Annotation_Path,name +".xml"))
            bb=[dlib.rectangle(left=x,top=y,right=w,bottom=h)  
                for (y,h,x,w) in annotations]
            boxes.append(bb)
    
    # Train the object detector
    print("[INFO] Training the Support Vector Machine Deector")
    mySVM_Detector=dlib.train_simple_object_detector(images,boxes,options)
    
    # Save the detector
    print("[INFO] Saving SVM Detector")
    mySVM_Detector.save(DetectorOutputFolder)
    
    