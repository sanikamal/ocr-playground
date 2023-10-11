import pytesseract
import cv2
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
ap.add_argument("-d","--digits",type=int,default=1,
                help="whether or not digits only OCR should be performed")
args = vars(ap.parse_args())


# Load the input image
img = cv2.imread(args["image"])
img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

options=""

if args["digits"] > 0:
    options="outputbase digits"

text = pytesseract.image_to_string(img,config=options)
print(text)