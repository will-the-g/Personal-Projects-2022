import pyautogui as pg
import time
import pyscreenshot
import pytesseract
import cv2
import Checks
import re
import imutils
time.sleep(2)

def ImageToString(Coords):

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    screenshot = pyscreenshot.grab(bbox=(Coords))
    screenshot.save('screenshot.png')
    image = cv2.imread('screenshot.png')
    image2 = imutils.resize(image, width=200)
    gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    global data
    data = str(pytesseract.image_to_string(thresh, lang='eng', config='--psm 6'))
    # cv2.imshow('image', image)    # <-- For Testing Purposes Only
    # cv2.imshow('gray', gray)      # <-- For Testing Purposes Only
    # cv2.imshow('thresh', thresh)  # <-- For Testing Purposes Only

def LoadPowerPlants(n):
    time.sleep(1)
    x = 800
    if n <= 2:
        y = 420 - (20 * (n - 1))
    if n > 2:
        y = 360 + (20 * (n - 2))
    pg.click(x, y)
    pg.moveTo(678, 426), pg.dragTo(831, 423, 0.75), time.sleep(0.5)  # Slider for Loading the Plant
    pg.click(686, 466)
    time.sleep(3)
    Checks.Exploration()


def ToPowerPlant(Spot):
    pg.click(Spot), time.sleep(0.5), pg.click(637, 447)  # Goes to First Power Plant
    time.sleep(2)
    pg.click(679, 405)  # Clicks on The Power Plant
    LoadPowerPlants(1)

def PowerPlantSwitch(n):
    x = 685
    if n <= 2:
        y = 405 - (20 * (n - 1))
        X = x + 45
    if n > 2:
        y = 355 + (20 * (n - 2))
        X = x - 45
    pg.click(X, y - 20)
    time.sleep(1)
    LoadPowerPlants(n)

def MainPowerPlant():
    pg.click(873, 693), time.sleep(1.5), pg.click(783, 280), time.sleep(2)  # Goes to Electricity Buildings
    Check1 = 482, 692, 576, 736
    Check2 = 604, 692, 704, 736
    Check3 = 724, 692, 829, 736
    ImageToString(Check1)
    if 'Power Plant' in data:
        print('Power Plant Detected in Spot 1')
        FirstSpot = 531, 687
        ToPowerPlant(FirstSpot)
    else:
        ImageToString(Check2)
        if 'Power Plant' in data:
            print('Power Plant Detected In Spot 2')
            SecondSpot = 649, 675
            ToPowerPlant(SecondSpot)
        else:
            ImageToString(Check3)
            if 'Power Plant' in data:
                print('Power Plant Detected In Spot 3')
                ThirdSpot = 791, 680
                ToPowerPlant(ThirdSpot)
            else:
                print('No Power Plant Detected in first 3 spots')
    PowerPlantSwitch(1)
    PowerPlantSwitch(2)
    PowerPlantSwitch(3)
    PowerPlantSwitch(4)
    PowerPlantSwitch(5)
    print('Finished PowerPlants for Transports')

def first_plant():
    pg.click(874, 698), time.sleep(0.75), pg.click(586, 382), time.sleep(1), pg.click(533, 681), time.sleep(1)
    pg.click(635, 447), time.sleep(1), pg.click(682, 411)  # Gets Position of first Chip Plant


def plant_load(n):
    y = 420 - (20 * (n - 1))
    if n > 1:
        x = 800
    if n == 1:
        x = 820
    time.sleep(1), pg.click(x, y), time.sleep(0.75), pg.moveTo(672, 424), pg.dragTo(817, 424, 1), pg.click(687, 471)
    time.sleep(3), Checks.Exploration()

def plant_switch(n):
    y = 405 - (20 * n)
    if n == 1:
        x = 685
    if n == 2:
        x = 725
    if n == 3:
        x = 690
    pg.click(x + 45, y)
    time.sleep(1)
    plant_load(n)

def main_chips():
    first_plant()
    plant_load(1)
    plant_switch(1)
    plant_switch(2)
    plant_switch(3)
    print('Finished Chips for Transports')

