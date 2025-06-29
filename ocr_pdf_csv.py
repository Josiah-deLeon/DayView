# Optical Character Recoginition Method.
# Author:        Josiah de Leon
# Filename:      ocr_pdf_csv
# Description:   Converts a scanned document into a csv file 

import pandas as pd
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import re
import os
import cv2
import numpy as np

def preproces_image_for_ocr(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.medianBlur(gray, 3)
    _, tresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return Image.fromarray(tresh)

def enchanced_scanned_pdf_to_csv(pdf_path, csv_path):
    try:
        print("Converting PDF to images...")
        pages = convert_from_path(pdf_path, dpi)
    
    except Exception as e:
        print(f"Error: {e}")
        return None