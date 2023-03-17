import time
import pyautogui as pg
import pytesseract
import pyscreenshot
import cv2
import imutils

def ImageToString(Coords):

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    screenshot = pyscreenshot.grab(bbox=(Coords))
    screenshot.save('screenshot.png')
    image = cv2.imread('screenshot.png')
    image2 = imutils.resize(image, width=500)
    gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    global data
    data = str(pytesseract.image_to_string(thresh, lang='eng', config='--psm 6'))
    cv2.imshow('image', image)    # <-- For Testing Purposes Only
    cv2.imshow('gray', gray)      # <-- For Testing Purposes Only
    cv2.imshow('thresh', thresh)  # <-- For Testing Purposes Only

def Exploration():
    ClaimAll = 622, 609, 726, 633
    ImageToString(ClaimAll)
    if "Claim All" in data:
        pg.click(685, 623), time.sleep(3)  # Clicks Claim All
        print('Claimed All Explorations')
        pg.click(750, 114), time.sleep(1)
        FirstCheck = 760, 217, 831, 256
        SecondCheck = 760, 291, 831, 317
        ThirdCheck = 760, 361, 831, 387
        FourthCheck = 760, 433, 831, 455
        ImageToString(FirstCheck)
        if 'Dispatch' in data:
            pg.click(803, 232)
        else:
            ImageToString(SecondCheck)
            if 'Dispatch' in data:
                pg.click(801, 301)
            else:
                ImageToString(ThirdCheck)
                if 'Dispatch' in data:
                    pg.click(801, 373)
                else:
                    ImageToString(FourthCheck)
                    if 'Dispatch' in data:
                        pg.click(797, 444)
                    else:
                        'No Construction Vehicle is Available'

    else:
        print('No Exploration Detected')
