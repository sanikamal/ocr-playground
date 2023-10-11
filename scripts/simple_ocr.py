import pytesseract
import cv2
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
args = vars(ap.parse_args())


# Load the input image
img = cv2.imread(args["image"])
img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(img)
print(text)