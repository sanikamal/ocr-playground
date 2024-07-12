import pytesseract
import cv2
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
ap.add_argument("-b", "--blacklist", type=str,  default="",
                help="List of characters to blacklist")
ap.add_argument("-w", "--whitelist", type=str,  default="",
                help="List of characters to whitelist")
args = vars(ap.parse_args())


# Load the input image
img = cv2.imread(args["image"])
img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

options = ""

# check to see if a blacklist or whitelist has been supplied

if len(args["blacklist"]) > 0:
    options += "-c tessedit_char_blacklist={}".format(args["blacklist"])

if len(args["whitelist"]) > 0:
    options += "-c tessedit_char_whitelist={}".format(args["whitelist"])

text = pytesseract.image_to_string(img,config=options)
print(text)