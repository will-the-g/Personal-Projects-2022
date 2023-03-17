import pyscreenshot
import pytesseract
import pyautogui as pg
import time
import sys
import cv2
import re
import imutils
import Transports
import Alliance
import Misc
import Military
import mysql.connector
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
import cgitb

cgitb.enable(format='text')

width, height = pg.size()
coord1 = int(height - (height / 6))
height2 = height - 40


# Self Explanatory
def CtrlW():
    pg.keyDown('Ctrl')
    pg.keyDown('w')
    pg.keyUp('ctrl')
    pg.keyUp('w')
# Converts Image to String
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
    # cv2.imshow('image', image)    # <-- For Testing Purposes Only
    # cv2.imshow('gray', gray)      # <-- For Testing Purposes Only
    # cv2.imshow('thresh', thresh)  # <-- For Testing Purposes Only

# Loads the Bluestacks Application
def Bluestacks():
    pg.press('Win')
    time.sleep(0.5)
    pg.typewrite('BlueStacks 5', 0.2)
    time.sleep(0.5)
    coords = 790, 284, 907, 314
    ImageToString(coords)
    if 'BlueStacks' in data:
        pg.keyDown('enter')
        pg.keyUp('enter')
    else:
        pg.press('escape')
        Bluestacks()
    time.sleep(5)
    screenshot = pyscreenshot.grab(bbox=(0, coord1, width, height2))
    time.sleep(1)
    count = 0
    count2 = 0
    color = (26, 144, 255)
    black = (0, 0, 0)
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            if screenshot.getpixel((x, y)) == color:
                count += 1
            elif screenshot.getpixel((x, y)) == black:
                count2 += 1
    if count > 0:
        print('Bluestacks is Loading')
        pg.press('F11')
    if count2 > 1000:
        print('BlueStacks Is Ready')
        CtrlW()
    if count2 < 100:
        if count == 0:
            print('Bluestacks is Not Loading')
            Bluestacks()


# Checks if Bluestacks has finished loading
def BlueStacksReady():
    screenshot = pyscreenshot.grab(bbox=(0, coord1, width, height2))
    time.sleep(1)
    count = 0
    color = (26, 144, 255)
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            if screenshot.getpixel((x, y)) == color:
                count += 1
    if count > 0:
        print('BlueStacks is Not Ready Yet')
        time.sleep(15)
        BlueStacksReady()
    if count == 0:
        print('BlueStacks is Ready')


# Loads the Last Shelter Application
def LastShelter():
    pg.press('Win')
    time.sleep(1.5)
    pg.typewrite('apps: LastShelterSurvival', 0.25)
    time.sleep(1)
    pg.press('enter')
    time.sleep(10)
    pg.press('F11')
    print('Last Shelter is now Loading')
    pyscreenshot.grab(bbox=())


# Checks if Last Shelter is loading
def LastShelterLoading():
    screenshot = pyscreenshot.grab(bbox=(470, 620, 881, 747))
    color = (187, 64, 64)
    color2 = (219, 198, 169)
    black = (0, 0, 0)
    count = 0
    count2 = 0
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            if screenshot.getpixel((x, y)) == color:
                count += 1
            if screenshot.getpixel((x, y)) == black:
                count2 += 1
            if screenshot.getpixel((x, y)) == color2:
                count += 1

    if count > 0 or count2 > 100:
        print('Last Shelter is Still Loading')
        time.sleep(20)
        LastShelterLoading()

    if count == 0:
        print('Last Shelter is Ready')


# Checks if the Wasteland News is on the screen
def WastelandNews():
    screenshot = pyscreenshot.grab(bbox=(794, 141, 845, 204))
    redX = (191, 95, 77)
    count = 0
    count2 = 0
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            if screenshot.getpixel((x, y)) == redX:
                count += 1
    if count > 0:
        print('Wasteland News is Present')
        time.sleep(1)
        pg.moveTo(822, 177, 0.1)
        pg.click()
        count2 += 1
        WastelandNews()
    if count == 0:
        print('There is no Wasteland News Loaded')
        if count2 > 0:
            print('Wasteland News is Exited')


# Checks if the custom avatar page is on the screen
def CustomAvatar():
    screenshot = pyscreenshot.grab(bbox=(853, 6, 895, 39))
    count = 0
    Color1 = (174, 148, 121)
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            if screenshot.getpixel((x, y)) == Color1:
                count += 1
    if count > 0:
        print('Custom Avatar Screen is Present')
        pg.moveTo(878, 25)
        pg.click()
        print('Custom Avatar Screen has been Exited')

    if count == 0:
        print('Custom Avatar Screen is not Present')


# Goes to the Gathering Screen
def Gathering():
    pg.moveTo(808, 68)
    pg.click()
    pg.moveTo(871, 733, 0.1)
    pg.click()
    time.sleep(10)
    pg.moveTo(687, 612, 0.1)
    pg.click()
    time.sleep(10)
    pg.moveTo(682, 646, 0.1)
    pg.click()


# Checks the Amount of Resources
def RssCheck():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    screenshot = pyscreenshot.grab(bbox=(735, 212, 810, 233))
    screenshot.save('screenshot.png')

    image = cv2.imread('screenshot.png')
    image2 = imutils.resize(image, width=200)
    gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

    data = str(pytesseract.image_to_string(thresh, lang='eng', config='--psm 6'))
    global rss
    rss = int(re.sub('[^0-9]', '', data))


# Checks if the error "No target has been found within 100km of base" pops up
def NoneFound():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    screenshot = pyscreenshot.grab(bbox=(554, 178, 821, 220))
    screenshot.save('screenshot.png')
    image = cv2.imread('screenshot.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    data = str(pytesseract.image_to_string(thresh, lang='eng', config='--psm 6'))
    if "No target found" in data:
        print('No target found 100km within base')
        global target
        target = False
    else:
        print('Target Acquired')
        target = True


# Checks Which APC is Selected when gathering
def SpecificAPC():
    ClassAPC = 814, 243, 861, 265
    APC1 = 814, 239, 855, 259
    APC2 = 814, 389, 861, 407
    APC3 = 814, 534, 861, 560
    pg.moveTo(685, 301)
    pg.dragTo(685, 470, 0.25)
    count = 0
    color = (255, 217, 141)
    global APC
    screenshot = pyscreenshot.grab(bbox=(887, 240, 905, 338))
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            if screenshot.getpixel((x, y)) == color:
                count += 1
    if count > 0:
        APC = ClassAPC
    if count == 0:
        time.sleep(1)
        pg.moveTo(703, 282)
        pg.dragTo(703, 57, 0.25)
        time.sleep(1)
        screenshot = pyscreenshot.grab(bbox=(887, 240, 905, 338))
        for x in range(screenshot.width):
            for y in range(screenshot.height):
                if screenshot.getpixel((x, y)) == color:
                    count += 1
        if count > 0:
            APC = APC1
        if count == 0:
            screenshot = pyscreenshot.grab(bbox=(887, 396, 905, 460))
            for x in range(screenshot.width):
                for y in range(screenshot.height):
                    if screenshot.getpixel((x, y)) == color:
                        count += 1
            if count > 0:
                APC = APC2
            if count == 0:
                screenshot = pyscreenshot.grab(bbox=(887, 549, 905, 620))
                for x in range(screenshot.width):
                    for y in range(screenshot.height):
                        if screenshot.getpixel((x, y)) == color:
                            count += 1
                if count > 0:
                    APC = APC3
                if count == 0:
                    print('No APC is selected, so that should be impossible? must be an error ig.')


def ImageString(Para):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    screenshot = pyscreenshot.grab(bbox=(Para))
    screenshot.save('screenshot.png')

    image = cv2.imread('screenshot.png')
    image2 = imutils.resize(image, width=200)
    gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    global data
    data = str(pytesseract.image_to_string(thresh, lang='eng', config='--psm 6'))
    # cv2.imshow('image', image)    <-- For Testing Purposes Only
    # cv2.imshow('gray', gray)      <-- For Testing Purposes Only
    # cv2.imshow('thresh', thresh)  <-- For Testing Purposes Only


# Gets the Load of the APC
def APCload():
    global load
    if '.' in data:
        if "M" in data:
            if data.find('.') < data.find('M'):
                load = float(re.sub('[^0-9.]', '', data))  # Removes all characters except #s and .
                load *= 1000000
            if data.find('.') > data.find('M'):
                load = float(re.sub('[^0-9.]', '', data))
                load *= 100000
        if "K" in data:
            if data.find('.') < data.find('K'):
                load = float(re.sub('[^0-9.]', '', data))
                load *= 1000
            if data.find('.') > data.find('K'):
                load = float(re.sub('[^0-9.]', '', data))
                load *= 100
    else:
        if "M" in data:
            load = float(re.sub('[^0-9.]', '', data))
            load *= 100000
        if "K" in data:
            load = float(re.sub('[^0-9.]', '', data))
            load *= 100
    load = int(load)


# Sends APC to gather Oil
def GatherOil(lvl, LowOilCount):
    time.sleep(2)
    global Lvl9Oil
    Lvl9Oil = True
    GatherCount = 0
    for i in range(0, 4):
        pg.moveTo(667, 481)
        pg.dragTo(766, 493, 0.4)  # Drags to the very left
        time.sleep(0.5)
    pg.moveTo(732, 576)  # Plus Button for Lvl
    for i in range(0, 10):
        pg.click()
        time.sleep(0.25)
    pg.moveTo(538, 577)  # Minus Button for Lvl
    for i in range(0, lvl):
        pg.click()
    time.sleep(0.3)
    pg.moveTo(786, 576)  # Go Button
    pg.click()
    time.sleep(1)
    NoneFound()
    if target is False:
        Lvl9Oil = False
        pg.moveTo(793, 351)  # Clicks Out of Gather Screen
        pg.click()
        pg.moveTo(687, 611)  # Coordinate Button
        pg.click()
        time.sleep(0.5)
        pg.moveTo(682, 648)  # Resource Button
        pg.click()
        time.sleep(1)
        GatherOil(2, 0)
        GatherCount += 1
    time.sleep(2)
    pg.moveTo(689, 384)  # Clicks on the Oil Well
    pg.click()
    time.sleep(5)
    RssCheck()
    print('Oil: ' + str(rss))
    if rss >= 2000000:
        pg.moveTo(721, 468, 0.2)  # Gather Button
        pg.click()
        time.sleep(2)
        pg.moveTo(566, 742)  # Auto Deploy
        pg.click()
        time.sleep(0.5)
        SpecificAPC()
        ImageString(APC)
        APCload()
        print('Load: ' + str(load))
        if load >= rss:
            pg.moveTo(791, 733)  # March Button
            pg.click()
            coords = 554, 337, 806, 377
            ImageToString(coords)
            if 'Another' in data or 'formation' in data:
                print('Another formation is marching to resource, restarting process')
                pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                GatherOil(lvl, 0)
        if load < rss:
            time.sleep(1)
            pg.moveTo(507, 25)  # Back Button
            pg.click()
            time.sleep(1)
            pg.moveTo(687, 611)  # Coordinate Button
            pg.click()
            time.sleep(0.5)
            pg.moveTo(682, 648)  # Resource Button
            pg.click()
            time.sleep(1)
            GatherOil(2, 0)
            GatherCount += 1
    if 1500000 <= rss < 2000000:
        LowOilCount = 0
        if GatherCount == 0:
            pg.moveTo(721, 468, 0.2)  # Gather Button
            pg.click()
            time.sleep(2)
            pg.moveTo(566, 742)  # Auto Deploy
            pg.click()
            time.sleep(0.5)
            SpecificAPC()
            ImageString(APC)
            APCload()
            print('Load: ' + str(load))
            if load >= 1500000:
                pg.moveTo(791, 733)  # March Button
                pg.click()
                coords = 554, 337, 806, 377
                ImageToString(coords)
                if 'Another' in data or 'formation' in data:
                    print('Another formation is marching to resource, restarting process')
                    pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                    time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                    GatherOil(lvl, 0)
            if load < 1500000:
                time.sleep(1)
                pg.moveTo(507, 25)  # Back Button
                pg.click()
                time.sleep(1)
                pg.moveTo(687, 611)  # Coordinate Button
                pg.click()
                time.sleep(0.5)
                pg.moveTo(682, 648)  # Resource Button
                pg.click()
                time.sleep(1)
                GatherOil(3, 0)
                GatherCount += 1
    if rss < 1500000:
        if GatherCount == 0:
            if lvl == 3:
                pg.moveTo(721, 468, 0.2)  # Gather Button
                pg.click()
                time.sleep(2)
                pg.moveTo(566, 742)  # Auto Deploy
                pg.click()
                time.sleep(0.5)
                pg.moveTo(791, 733)  # March Button
                pg.click()
                coords = 554, 337, 806, 377
                ImageToString(coords)
                if 'Another' in data or 'formation' in data:
                    print('Another formation is marching to resource, restarting process')
                    pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                    time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                    GatherOil(lvl, 0)
            else:
                if lvl == 2:
                    LowOilCount += 1
                    print('Low Oil Count: ' + str(LowOilCount))
                    if LowOilCount > 4:
                        if rss < 1200000:
                            pg.moveTo(687, 611)  # Coordinate Button
                            pg.click()
                            time.sleep(0.5)
                            pg.moveTo(682, 648)  # Resource Button
                            pg.click()
                            time.sleep(1)
                            GatherOil(3, 0)
                            GatherCount += 1
                        if rss >= 1200000:
                            pg.moveTo(721, 468, 0.2)  # Gather Button
                            pg.click()
                            time.sleep(2)
                            pg.moveTo(566, 742)  # Auto Deploy
                            pg.click()
                            time.sleep(0.5)
                            pg.moveTo(791, 733)  # March Button
                            pg.click()
                            coords = 554, 337, 806, 377
                            ImageToString(coords)
                            if 'Another' in data or 'formation' in data:
                                print('Another formation is marching to resource, restarting process')
                                pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                                time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                                GatherOil(lvl, 0)
                    else:
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherOil(2, LowOilCount)
                        GatherCount += 1
                if lvl == 1:
                    LowOilCount += 1
                    print('Low Oil Count: ' + str(LowOilCount))
                    if LowOilCount <= 4:
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherOil(1, LowOilCount)
                        GatherCount += 1
                    if LowOilCount > 4:
                        print('Switching to Level 8 Oil Wells')
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherOil(2, 0)
                        GatherCount += 1
    if GatherCount <= 1:
        pg.moveTo(687, 611)  # Coordinate Button
        pg.click()
        time.sleep(0.5)
        pg.moveTo(682, 648)  # Resource Button
        pg.click()
        time.sleep(1)


# Sends APC out to gather Iron
def GatherIron(lvl, LowIronCount):
    time.sleep(2)
    global Lvl9Iron
    Lvl9Iron = True
    GatherCount = 0
    for i in range(0, 4):
        pg.moveTo(667, 481)
        pg.dragTo(766, 493, 0.4)  # Drags to the very left
        time.sleep(0.5)
    pg.moveTo(766, 493)
    pg.dragTo(667, 481)  # Drags to Iron
    pg.moveTo(732, 576)  # Plus Button for Lvl
    for i in range(0, 10):
        pg.click()
        time.sleep(0.25)
    pg.moveTo(538, 577)  # Minus Button for Lvl
    for i in range(0, lvl):
        pg.click()
    time.sleep(0.3)
    pg.moveTo(786, 576)  # Go Button
    pg.click()
    time.sleep(1)
    NoneFound()
    if target is False:
        Lvl9Iron = False
        pg.moveTo(793, 351)  # Clicks Out of Gather Screen
        pg.click()
        pg.moveTo(687, 611)  # Coordinate Button
        pg.click()
        time.sleep(0.5)
        pg.moveTo(682, 648)  # Resource Button
        pg.click()
        time.sleep(1)
        GatherIron(2, 0)
        GatherCount += 1
    time.sleep(2)
    pg.moveTo(689, 384)  # Clicks on the Iron Refinery
    pg.click()
    time.sleep(5)
    RssCheck()
    print('Iron: ' + str(rss))
    if rss >= 1000000:
        pg.moveTo(721, 468, 0.2)  # Gather Button
        pg.click()
        time.sleep(2)
        pg.moveTo(566, 742)  # Auto Deploy
        pg.click()
        time.sleep(0.5)
        SpecificAPC()
        ImageString(APC)
        APCload()
        print('Load: ' + str(load))
        if load >= rss:
            pg.moveTo(791, 733)  # March Button
            pg.click()
            coords = 554, 337, 806, 377
            ImageToString(coords)
            if 'Another' in data or 'formation' in data:
                print('Another formation is marching to resource, restarting process')
                pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                GatherIron(lvl, 0)
        if load < rss:
            time.sleep(1)
            pg.moveTo(507, 25)  # Back Button
            pg.click()
            time.sleep(1)
            pg.moveTo(687, 611)  # Coordinate Button
            pg.click()
            time.sleep(0.5)
            pg.moveTo(682, 648)  # Resource Button
            pg.click()
            time.sleep(1)
            GatherIron(2, 0)
            GatherCount += 1
    if 750000 <= rss < 1000000:
        LowIronCount = 0
        if GatherCount == 0:
            pg.moveTo(721, 468, 0.2)  # Gather Button
            pg.click()
            time.sleep(2)
            pg.moveTo(566, 742)  # Auto Deploy
            pg.click()
            time.sleep(0.5)
            SpecificAPC()
            ImageString(APC)
            APCload()
            print('Load: ' + str(load))
            if load >= 750000:
                pg.moveTo(791, 733)  # March Button
                pg.click()
                coords = 554, 337, 806, 377
                ImageToString(coords)
                if 'Another' in data or 'formation' in data:
                    print('Another formation is marching to resource, restarting process')
                    pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                    time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                    GatherIron(lvl, 0)
            if load < 750000:
                time.sleep(1)
                pg.moveTo(507, 25)  # Back Button
                pg.click()
                time.sleep(1)
                pg.moveTo(687, 611)  # Coordinate Button
                pg.click()
                time.sleep(0.5)
                pg.moveTo(682, 648)  # Resource Button
                pg.click()
                time.sleep(1)
                GatherIron(3, 0)
                GatherCount += 1
    if rss < 750000:
        if GatherCount == 0:
            if lvl == 3:
                pg.moveTo(721, 468, 0.2)  # Gather Button
                pg.click()
                time.sleep(2)
                pg.moveTo(566, 742)  # Auto Deploy
                pg.click()
                time.sleep(0.5)
                pg.moveTo(791, 733)  # March Button
                pg.click()
                coords = 554, 337, 806, 377
                ImageToString(coords)
                if 'Another' in data or 'formation' in data:
                    print('Another formation is marching to resource, restarting process')
                    pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                    time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                    GatherIron(lvl, 0)
            else:
                if lvl == 2:
                    LowIronCount += 1
                    print('Low Iron Count ' + str(LowIronCount))
                    if LowIronCount > 4:
                        if rss < 600000:
                            pg.moveTo(687, 611)  # Coordinate Button
                            pg.click()
                            time.sleep(0.5)
                            pg.moveTo(682, 648)  # Resource Button
                            pg.click()
                            time.sleep(1)
                            GatherIron(3, 0)
                            GatherCount += 1
                        if rss >= 600000:
                            pg.moveTo(721, 468, 0.2)  # Gather Button
                            pg.click()
                            time.sleep(2)
                            pg.moveTo(566, 742)  # Auto Deploy
                            pg.click()
                            time.sleep(0.5)
                            pg.moveTo(791, 733)  # March Button
                            pg.click()
                            coords = 554, 337, 806, 377
                            ImageToString(coords)
                            if 'Another' in data or 'formation' in data:
                                print('Another formation is marching to resource, restarting process')
                                pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                                time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                                GatherIron(lvl, 0)
                    else:
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherIron(2, LowIronCount)
                        GatherCount += 1
                if lvl == 1:
                    LowIronCount += 1
                    print('Low Iron Count ' + str(LowIronCount))
                    if LowIronCount <= 4:
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherOil(1, LowIronCount)
                        GatherCount += 1
                    if LowIronCount > 4:
                        print('Switching to Level 8 Refinery')
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherOil(2, 0)
                        GatherCount += 1
    if GatherCount <= 1:
        pg.moveTo(687, 611)  # Coordinate Button
        pg.click()
        time.sleep(0.5)
        pg.moveTo(682, 648)  # Resource Button
        pg.click()
        time.sleep(1)

def GatherFood(lvl, LowFoodCount):
    time.sleep(2)
    global Lvl9Food
    Lvl9Food = True
    GatherCount = 0
    for i in range(0, 4):
        pg.moveTo(667, 481)
        pg.dragTo(766, 493, 0.4)  # Drags to the very left
        time.sleep(0.5)
    for i in range(0, 3):
        pg.moveTo(766, 493)
        pg.dragTo(667, 481)  # Drags to Food
    pg.moveTo(732, 576)  # Plus Button for Lvl
    for i in range(0, 10):
        pg.click()
        time.sleep(0.25)
    pg.moveTo(538, 577)  # Minus Button for Lvl
    for i in range(0, lvl):
        pg.click()
    time.sleep(0.3)
    pg.moveTo(786, 576)  # Go Button
    pg.click()
    time.sleep(1)
    NoneFound()
    if target is False:
        Lvl9Food = False
        pg.moveTo(793, 351)  # Clicks Out of Gather Screen
        pg.click()
        pg.moveTo(687, 611)  # Coordinate Button
        pg.click()
        time.sleep(0.5)
        pg.moveTo(682, 648)  # Resource Button
        pg.click()
        time.sleep(1)
        GatherFood(2, 0)
        GatherCount += 1
    time.sleep(2)
    pg.moveTo(689, 384)  # Clicks on the Farm
    pg.click()
    time.sleep(5)
    RssCheck()
    print(rss)
    if rss >= 2000000:
        pg.moveTo(721, 468, 0.2)  # Gather Button
        pg.click()
        time.sleep(2)
        pg.moveTo(566, 742)  # Auto Deploy
        pg.click()
        time.sleep(0.5)
        SpecificAPC()
        ImageString(APC)
        APCload()
        print(load)
        if load >= rss:
            pg.moveTo(791, 733)  # March Button
            pg.click()
            coords = 554, 337, 806, 377
            ImageToString(coords)
            if 'Another' in data or 'formation' in data:
                print('Another formation is marching to resource, restarting process')
                pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                GatherFood(lvl, 0)
        if load < rss:
            time.sleep(1)
            pg.moveTo(507, 25)  # Back Button
            pg.click()
            time.sleep(1)
            pg.moveTo(687, 611)  # Coordinate Button
            pg.click()
            time.sleep(0.5)
            pg.moveTo(682, 648)  # Resource Button
            pg.click()
            time.sleep(1)
            GatherFood(2, 0)
            GatherCount += 1
    if 1500000 <= rss < 2000000:
        LowFoodCount = 0
        if GatherCount == 0:
            pg.moveTo(721, 468, 0.2)  # Gather Button
            pg.click()
            time.sleep(2)
            pg.moveTo(566, 742)  # Auto Deploy
            pg.click()
            time.sleep(0.5)
            SpecificAPC()
            ImageString(APC)
            APCload()
            print(load)
            if load >= 1500000:
                pg.moveTo(791, 733)  # March Button
                pg.click()
                coords = 554, 337, 806, 377
                ImageToString(coords)
                if 'Another' in data or 'formation' in data:
                    print('Another formation is marching to resource, restarting process')
                    pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                    time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                    GatherFood(lvl, 0)
            if load < 1500000:
                time.sleep(1)
                pg.moveTo(507, 25)  # Back Button
                pg.click()
                time.sleep(1)
                pg.moveTo(687, 611)  # Coordinate Button
                pg.click()
                time.sleep(0.5)
                pg.moveTo(682, 648)  # Resource Button
                pg.click()
                time.sleep(1)
                GatherFood(3, 0)
                GatherCount += 1
    if rss < 1500000:
        if GatherCount == 0:
            if lvl == 3:
                pg.moveTo(721, 468, 0.2)  # Gather Button
                pg.click()
                time.sleep(2)
                pg.moveTo(566, 742)  # Auto Deploy
                pg.click()
                time.sleep(0.5)
                pg.moveTo(791, 733)  # March Button
                pg.click()
                coords = 554, 337, 806, 377
                ImageToString(coords)
                if 'Another' in data or 'formation' in data:
                    print('Another formation is marching to resource, restarting process')
                    pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                    time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                    GatherFood(lvl, 0)
            else:
                if lvl == 2:
                    LowFoodCount += 1
                    print('Low Food Count: ' + str(LowFoodCount))
                    if LowFoodCount > 4:
                        if rss < 1200000:
                            pg.moveTo(687, 611)  # Coordinate Button
                            pg.click()
                            time.sleep(0.5)
                            pg.moveTo(682, 648)  # Resource Button
                            pg.click()
                            time.sleep(1)
                            print('Switching to Lvl 7 Farm')
                            GatherFood(3, 0)
                            GatherCount += 1
                        if rss >= 1200000:
                            pg.moveTo(721, 468, 0.2)  # Gather Button
                            pg.click()
                            time.sleep(2)
                            pg.moveTo(566, 742)  # Auto Deploy
                            pg.click()
                            time.sleep(0.5)
                            pg.moveTo(791, 733)  # March Button
                            pg.click()
                            coords = 554, 337, 806, 377
                            ImageToString(coords)
                            if 'Another' in data or 'formation' in data:
                                print('Another formation is marching to resource, restarting process')
                                pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                                time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                                GatherFood(lvl, 0)
                    else:
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherFood(2, LowFoodCount)
                        GatherCount += 1
                if lvl == 1:
                    LowFoodCount += 1
                    print('Low Oil Count: ' + str(LowFoodCount))
                    if LowFoodCount <= 4:
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherFood(1, LowFoodCount)
                        GatherCount += 1
                    if LowFoodCount > 4:
                        print('Switching to Level 8 Farm')
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherFood(2, 0)
                        GatherCount += 1
    if GatherCount <= 1:
        pg.moveTo(687, 611)  # Coordinate Button
        pg.click()
        time.sleep(0.5)
        pg.moveTo(682, 648)  # Resource Button
        pg.click()
        time.sleep(1)

def GatherLumber(lvl, LowLumberCount):
    time.sleep(2)
    global Lvl9Lumber
    Lvl9Lumber = True
    GatherCount = 0
    for i in range(0, 4):
        pg.moveTo(667, 481)
        pg.dragTo(766, 493, 0.4)  # Drags to the very left
        time.sleep(0.5)
    for i in range(0, 2):
        pg.moveTo(766, 493)
        pg.dragTo(667, 481)  # Drags to Lumber
    pg.moveTo(732, 576)  # Plus Button for Lvl
    for i in range(0, 10):
        pg.click()
        time.sleep(0.25)
    pg.moveTo(538, 577)  # Minus Button for Lvl
    for i in range(0, lvl):
        pg.click()
    time.sleep(0.3)
    pg.moveTo(786, 576)  # Go Button
    pg.click()
    time.sleep(1)
    NoneFound()
    if target is False:
        Lvl9Lumber = False
        pg.moveTo(793, 351)  # Clicks Out of Gather Screen
        pg.click()
        pg.moveTo(687, 611)  # Coordinate Button
        pg.click()
        time.sleep(0.5)
        pg.moveTo(682, 648)  # Resource Button
        pg.click()
        time.sleep(1)
        GatherLumber(2, 0)
        GatherCount += 1
    time.sleep(2)
    pg.moveTo(689, 384)  # Clicks on the Lumber Mill
    pg.click()
    time.sleep(5)
    RssCheck()
    print('Lumber: ' + str(rss))
    if rss >= 1400000:
        pg.moveTo(721, 468, 0.2)  # Gather Button
        pg.click()
        time.sleep(2)
        pg.moveTo(566, 742)  # Auto Deploy
        pg.click()
        time.sleep(0.5)
        SpecificAPC()
        ImageString(APC)
        APCload()
        print('Load: ' + str(load))
        if load >= rss:
            pg.moveTo(791, 733)  # March Button
            pg.click()
            coords = 554, 337, 806, 377
            ImageToString(coords)
            if 'Another' in data or 'formation' in data:
                print('Another formation is marching to resource, restarting process')
                pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                GatherLumber(lvl, 0)
        if load < rss:
            time.sleep(1)
            pg.moveTo(507, 25)  # Back Button
            pg.click()
            time.sleep(1)
            pg.moveTo(687, 611)  # Coordinate Button
            pg.click()
            time.sleep(0.5)
            pg.moveTo(682, 648)  # Resource Button
            pg.click()
            time.sleep(1)
            GatherLumber(2, 0)
            GatherCount += 1
    if 1100000 <= rss < 1400000:
        if GatherCount == 0:
            pg.moveTo(721, 468, 0.2)  # Gather Button
            pg.click()
            time.sleep(2)
            pg.moveTo(566, 742)  # Auto Deploy
            pg.click()
            time.sleep(0.5)
            SpecificAPC()
            ImageString(APC)
            APCload()
            print('Load: ' + str(load))
            if load >= 1100000:
                pg.moveTo(791, 733)  # March Button
                pg.click()
                coords = 554, 337, 806, 377
                ImageToString(coords)
                if 'Another' in data or 'formation' in data:
                    print('Another formation is marching to resource, restarting process')
                    pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                    time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                    GatherLumber(lvl, 0)
            if load < 1100000:
                time.sleep(1)
                pg.moveTo(507, 25)  # Back Button
                pg.click()
                time.sleep(1)
                pg.moveTo(687, 611)  # Coordinate Button
                pg.click()
                time.sleep(0.5)
                pg.moveTo(682, 648)  # Resource Button
                pg.click()
                time.sleep(1)
                print('Now Gathering Lvl 7 Lumber Mill')
                GatherLumber(3, 0)
                GatherCount += 1
    if rss < 1100000:
        if GatherCount == 0:
            if lvl == 3:
                pg.moveTo(721, 468, 0.2)  # Gather Button
                pg.click()
                time.sleep(2)
                pg.moveTo(566, 742)  # Auto Deploy
                pg.click()
                time.sleep(0.5)
                pg.moveTo(791, 733)  # March Button
                pg.click()
                coords = 554, 337, 806, 377
                ImageToString(coords)
                if 'Another' in data or 'formation' in data:
                    print('Another formation is marching to resource, restarting process')
                    pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                    time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                    GatherLumber(lvl, 0)
            else:
                if lvl == 2:
                    LowLumberCount += 1
                    if LowLumberCount > 4:
                        if rss < 800000:
                            pg.moveTo(687, 611)  # Coordinate Button
                            pg.click()
                            time.sleep(0.5)
                            pg.moveTo(682, 648)  # Resource Button
                            pg.click()
                            time.sleep(1)
                            GatherLumber(3, 0)
                            GatherCount += 1
                        if rss >= 800000:
                            pg.moveTo(721, 468, 0.2)  # Gather Button
                            pg.click()
                            time.sleep(2)
                            pg.moveTo(566, 742)  # Auto Deploy
                            pg.click()
                            time.sleep(0.5)
                            pg.moveTo(791, 733)  # March Button
                            pg.click()
                            coords = 554, 337, 806, 377
                            ImageToString(coords)
                            if 'Another' in data or 'formation' in data:
                                print('Another formation is marching to resource, restarting process')
                                pg.click(713, 115), time.sleep(1), pg.click(492, 23), pg.click(687, 611)
                                time.sleep(0.5), pg.click(682, 648), time.sleep(1)
                                GatherLumber(lvl, 0)
                    else:
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherLumber(2, LowLumberCount)
                        GatherCount += 1
                if lvl == 1:
                    LowLumberCount += 1
                    print('Low Oil Count: ' + str(LowLumberCount))
                    if LowLumberCount <= 4:
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherFood(1, LowLumberCount)
                        GatherCount += 1
                    if LowLumberCount > 4:
                        print('Switching to Level 8 Farm')
                        pg.moveTo(687, 611)  # Coordinate Button
                        pg.click()
                        time.sleep(0.5)
                        pg.moveTo(682, 648)  # Resource Button
                        pg.click()
                        time.sleep(1)
                        GatherFood(2, 0)
                        GatherCount += 1
    if GatherCount <= 1:
        pg.moveTo(687, 611)  # Coordinate Button
        pg.click()
        time.sleep(0.5)
        pg.moveTo(682, 648)  # Resource Button
        pg.click()
        time.sleep(1)


# Adjusts application to certain parameters no matter the size of the screen
width, height = pg.size()
Parameter1 = int(width / 6)
Parameter2 = int(height / 6)
Parameter3 = int(width - 2 * (width / 6))
Parameter4 = int(height - 2 * (height / 6))
class SubWindow(QWidget):
    def __init__(self):
        super(SubWindow, self).__init__()
        self.resize(400, 600)
        self.setWindowTitle('Building Upgrades')
        self.subinitUI()

    def ChipsUBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Chips for Upgrade')
        else:
            print('Unchecked Chips for Upgrade')

    def subinitUI(self):
        self.background = QtWidgets.QLabel(self)
        pixmap = QPixmap('pfp218.jpg')
        pixmap2 = pixmap.scaled(400, 600)
        self.background.setPixmap(pixmap2)
        self.chips = QCheckBox('Chips', self)
        self.chips.move(50, 50)
        self.chips.stateChanged.connect(self.ChipsUBox)
        self.EnergyRefining = QCheckBox('Energy Cores', self)
        self.EnergyRefining.move(50, 80)
        self.EnergyRefining.stateChanged.connect(self.ECUBox)
        self.Barracks = QCheckBox('Barracks', self)
        self.Barracks.move(50, 110)
        self.Barracks.stateChanged.connect(self.BarracksUBox)

    def ECUBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Energy Cores has been Checked for Building Upgrades')
            global ECUpgrade
            ECUpgrade = True
        else:
            print('Energy Cores has been Unchecked for Building Upgrades')
            ECUpgrade = False

    def BarracksUBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Barracks has been Checked for Building Upgrades')
            global BarracksUpgrade
            BarracksUpgrade = True
        else:
            print('Barracks has been Unchecked for Building Upgrades')
            BarracksUpgrade = False
class SubWindow2(QWidget):
    def __init__(self):
        super(SubWindow2,self).__init__()
        self.resize(140, 160)
        self.setWindowTitle('Shield')
        self.setStyleSheet('background-color: rgb(38,38,38)')
        self.subinitUI2()

    def subinitUI2(self):
        self.SaveButton = QtWidgets.QPushButton('Save', self)
        self.SaveButton.move(20, 130)
        self.SaveButton.resize(100, 20)
        self.SaveButton.setStyleSheet('QPushButton { border: 1px solid black; background: #00b9fb } '
                                      'QPushButton::hover { background-color: lightgreen; }')
        self.SaveButton.clicked.connect(self.clicked)
        self.EightHours = QtWidgets.QCheckBox('8 Hours', self)
        self.EightHours.move(30, 30)
        self.EightHours.stateChanged.connect(self.EightHourBox)
        self.OneDay = QtWidgets.QCheckBox('1 Day', self)
        self.OneDay.move(30, 60)
        self.OneDay.stateChanged.connect(self.OneDayBox)
        self.ThreeDays = QtWidgets.QCheckBox('3 Days', self)
        self.ThreeDays.move(30, 90)
        self.ThreeDays.stateChanged.connect(self.ThreeDaysBox)

    def clicked(self):
        self.close()
        print('Shield Time Saved')

    def EightHourBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked 8 Hours for Shield')
        else:
            print('Unchecked 8 Hours for Shield')
    def OneDayBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked 1 Day for Shield')
        else:
            print('Unchecked 1 day for Shield')
    def ThreeDaysBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked 3 Days for Shield')
        else:
            print('Uncheck 3 Days for Shield')

class SubWindow3(QWidget):
    def __init__(self):
        super(SubWindow3, self).__init__()
        self.resize(200, 600)
        self.setWindowTitle('Resource Building Upgrades')
        self.setStyleSheet('background-color: rgb(38,38,38)')
        self.subinitUI3()
    def subinitUI3(self):
        self.SaveButton = QtWidgets.QPushButton('Save', self)
        self.SaveButton.move(20, 560)
        self.SaveButton.resize(100, 20)
        self.SaveButton.setStyleSheet('QPushButton { border: 1px solid black; background: #00b9fb } '
                                      'QPushButton::hover { background-color: lightgreen; }')
        self.SaveButton.clicked.connect(self.clicked)
        self.WaterFilter = QtWidgets.QCheckBox('Water Filter', self)
        self.WaterFilter.move(20, 30)
        self.WaterFilter.setFont(QtGui.QFont('Courier', 15))
        self.WaterFilter.setStyleSheet('color: #2184de')
        self.WaterFilter.stateChanged.connect(self.WaterFilterBox)
        self.Farm = QtWidgets.QCheckBox('Farm', self)
        self.Farm.move(20, 100)
        self.Farm.setFont(QtGui.QFont('Courier', 15))
        self.Farm.setStyleSheet('color: #f2e27d')
        self.Farm.stateChanged.connect(self.FarmBox)
        self.LumberMill = QtWidgets.QCheckBox('Lumber Mill', self)
        self.LumberMill.move(20, 170)
        self.LumberMill.setFont(QtGui.QFont('Courier', 15))
        self.LumberMill.setStyleSheet('color: #b5651d')
        self.LumberMill.stateChanged.connect(self.LumberMillBox)
        self.OilWell = QtWidgets.QCheckBox('Oil Well', self)
        self.OilWell.move(20, 240)
        self.OilWell.setFont(QtGui.QFont('Courier', 15))
        self.OilWell.setStyleSheet('color: #808080')
        self.OilWell.stateChanged.connect(self.OilWellBox)
        self.Refinery = QtWidgets.QCheckBox('Refinery', self)
        self.Refinery.move(20, 310)
        self.Refinery.setFont(QtGui.QFont('Courier', 15))
        self.Refinery.setStyleSheet('color: #d3d3d3')
        self.Refinery.stateChanged.connect(self.RefineryBox)
        self.WindTurbine = QtWidgets.QCheckBox('Wind Turbine', self)
        self.WindTurbine.move(20, 380)
        self.WindTurbine.setFont(QtGui.QFont('Courier', 15))
        self.WindTurbine.setStyleSheet('color: #ADD8E6')
        self.WindTurbine.stateChanged.connect(self.WindTurbineBox)
        self.PowerPlants = QtWidgets.QCheckBox('Power Plants', self)
        self.PowerPlants.move(20, 450)
        self.PowerPlants.setFont(QtGui.QFont('Courier', 15))
        self.PowerPlants.setStyleSheet('color: #ec2400')
        self.PowerPlants.stateChanged.connect(self.PowerPlantBox)
        self.Banks = QtWidgets.QCheckBox('Banks', self)
        self.Banks.move(20, 520)
        self.Banks.setFont(QtGui.QFont('Courier', 15))
        self.Banks.setStyleSheet('color: #118C4F')
        self.Banks.stateChanged.connect(self.BankBox)
    def clicked(self):
        self.close()
        print('Resource Upgrades Saved')

    def WaterFilterBox(self, state):
        if state == QtCore.Qt.Checked:
            print('WaterFilter Checked for Upgrade')
        else:
            print('WaterFilter Unchecked for Upgrade')
    def FarmBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Farm Checked for Upgrade')
        else:
            print('Farm Unchecked for Upgrade')
    def LumberMillBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Lumber Mill Checked for Upgrade')
        else:
            print('Lumber Mill Unchecked for Upgrade')
    def OilWellBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Oil Well Checked for Upgrade')
        else:
            print('Oil Well Unchecked for Upgrade')
    def RefineryBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Refinery Checked for Upgrade')
        else:
            print('Refinery Unchecked for Upgrade')
    def WindTurbineBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Wind Turbine Checked for Upgrade')
        else:
            print('Wind Turbine Unchecked for Upgrade')
    def PowerPlantBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Power Plants Checked for Upgrade')
        else:
            print('Power Plants Unchecked for Upgrade')
    def BankBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Banks Checked for Upgrade')
        else:
            print('Banks Unchecked for Upgrade')

class SubWindow4(QWidget):
    def __init__(self):
        super(SubWindow4, self).__init__()
        self.resize(200, 400)
        self.setStyleSheet('SubWindow4{background-color: rgb(38,38,38)}'
                           'QInputDialog{background-color: gray; }')
        self.setWindowTitle('Troops Training')
        self.subinitUI4()
    def Inputs(self):
        if self.VehicleCustom.isChecked() is True:
            self.VehicleInput = QtWidgets.QInputDialog.getInt(self, 'Vehicle Tier', 'Input Vehicle Tier 2-8', 6, 2, 8)
        if self.ShooterCustom.isChecked() is True:
            self.ShooterInput = QtWidgets.QInputDialog.getInt(self, 'Shooter Tier', 'Input Shooter Tier 2-8', 4, 2, 8)
        if self.FighterCustom.isChecked() is True:
            self.FighterInput = QtWidgets.QInputDialog.getInt(self, 'Fighter Tier', 'Input Fighter Tier 2-8', 1, 2, 8)
    def subinitUI4(self):
        self.SaveButton = QtWidgets.QPushButton('Save', self)
        self.SaveButton.move(20, 360)
        self.SaveButton.resize(100, 20)
        self.SaveButton.setStyleSheet('QPushButton { border: 1px solid black; background: #00b9fb } '
                                      'QPushButton::hover { background-color: lightgreen; }')
        self.SaveButton.clicked.connect(self.clicked)
        self.VehicleT1 = QtWidgets.QCheckBox('T1 Vehicle', self)
        self.VehicleT1.move(20, 30)
        self.VehicleT1.stateChanged.connect(self.VehicleT1Box)
        self.VehicleT1.setStyleSheet('color: yellow')
        self.VehicleT1.setFont(QtGui.QFont('Courier', 12))
        self.VehicleCustom = QtWidgets.QCheckBox('Custom Tier', self)
        self.VehicleCustom.move(20, 80)
        self.VehicleCustom.stateChanged.connect(self.Inputs)
        self.VehicleCustom.setStyleSheet('color: #B58B00')
        self.VehicleCustom.setFont(QtGui.QFont('Courier', 12))
        self.ShooterT1 = QtWidgets.QCheckBox('T1 Shooter', self)
        self.ShooterT1.move(20, 130)
        self.ShooterT1.stateChanged.connect(self.ShooterT1Box)
        self.ShooterT1.setStyleSheet('color: #666699')
        self.ShooterT1.setFont(QtGui.QFont('Courier', 12))
        self.ShooterCustom = QtWidgets.QCheckBox('Custom Shooter', self)
        self.ShooterCustom.move(20, 180)
        self.ShooterCustom.stateChanged.connect(self.Inputs)
        self.ShooterCustom.setStyleSheet('color: #9F2B00')
        self.ShooterCustom.setFont(QtGui.QFont('Courier', 12))
        self.FighterT1 = QtWidgets.QCheckBox('T1 Fighter', self)
        self.FighterT1 .move(20, 230)
        self.FighterT1.stateChanged.connect(self.FighterT1Box)
        self.FighterT1 .setStyleSheet('color: #FF8300')
        self.FighterT1 .setFont(QtGui.QFont('Courier', 12))
        self.FighterCustom = QtWidgets.QCheckBox('Custom Fighter', self)
        self.FighterCustom.move(20, 280)
        self.FighterCustom.stateChanged.connect(self.Inputs)
        self.FighterCustom.setStyleSheet('color: #FF5C4D')
        self.FighterCustom.setFont(QtGui.QFont('Courier', 12))
    def clicked(self):
        self.close()
        print('Troop Training Saved')
        if self.VehicleCustom.isChecked() is True:
            VehicleTier = re.sub('[^0-9]', '', str(self.VehicleInput))
            print('Tier ' + VehicleTier + ' for Vehicles')
        if self.ShooterCustom.isChecked() is True:
            ShooterTier = re.sub('^[0-9]', '', str(self.ShooterInput))
            print('Tier' + ShooterTier + ' for Shooters')
        if self.FighterCustom.isChecked() is True:
            FighterTier = re.sub('[^0-9]', '', str(self.FighterInput))
            print('Tier' + FighterTier + ' for Fighters')
        if self.VehicleCustom.isChecked() is True and self.VehicleT1.isChecked() is True:
            print('More than one tier for Vehicles is Selected, Unchecking Custom Tier')
            self.VehicleCustom.setChecked(False)
        if self.ShooterCustom.isChecked() is True and self.ShooterT1.isChecked() is True:
            print('More than one tier for Shooters is Selected. Unchecking Custom Tier')
            self.ShooterCustom.setChecked(False)
        if self.FighterCustom.isChecked() is True and self.FighterT1.isChecked() is True:
            print('More than one tier for Fighters is Selected, Unchecking Custom Tier')
            self.FighterCustom.setChecked(False)
    def VehicleT1Box(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Tier 1 Vehicle for Training')
        else:
            print('Unchecked Tier 1 Vehicle for Training')
    def VehicleCustomBox(self, state):
        if state == QtCore.Qt.Checked:
            print(self.VehicleInput)
        else:
            print('Unchecked Custom Tier Vehicle for Training')
    def ShooterT1Box(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked T1 Shooters for Training')
        else:
            print('Unchecked T1 Shooters for Training')
    def ShooterCustomBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Custom Shooters for Training')
        else:
            print('Unchecked Custom Tier Shooters for Training')
    def FighterT1Box(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked T1 Fighters for Training')
        else:
            print('Unchecked T1 Fighters for Training')
    def FighterCustomBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Highest Tier Fighter for Training')
        else:
            print('Unchecked Custom Tier Fighter for Training')
# Application Window
class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(Parameter1, Parameter2, Parameter3, Parameter4)
        self.setWindowTitle('Last Shelter Survival Bot')
        self.setToolTip('Last Shelter Bot')
        self.setWindowIcon(QIcon('wallpaper116.jpg'))
        self.setStyleSheet('background-color: #808080')
        print('--------------------Application Loaded--------------------')
        self.initUI()
        self.ui1 = SubWindow()
        self.ui2 = SubWindow2()
        self.ui3 = SubWindow3()
        self.ui4 = SubWindow4()
    def window1(self):
        if self.UpgradeCheckbox.isChecked() is True:
            self.ui1.show()
    def window2(self):
        if self.Shield.isChecked() is True:
            self.ui2.show()
    def window3(self):
        if self.RSSBuildings.isChecked() is True:
            self.ui3.show()
    def window4(self):
        if self.Training.isChecked() is True:
            self.ui4.show()
    def initUI(self):
        Parameter5 = int(Parameter4 - (Parameter4 / 2.5))
        # LoadingLastShelterButton
        self.Load = QtWidgets.QPushButton(self)
        color = QColor(177, 156, 217)
        self.Load.setStyleSheet('QPushButton::hover { background-color: lightgreen; }'
                                'QPushButton { border: 2px solid black; background: %s; }' % color.name())
        self.Load.setText('Load Last Shelter')
        self.Load.clicked.connect(self.clicked)
        self.Load.move(50, 50)
        self.Load.resize(100, 50)

        self.button2 = QtWidgets.QPushButton('Run', self)
        self.button2.setStyleSheet('QPushButton::hover { background-color: lightgreen; }'
                                   'QPushButton { border: 2px solid black; background: %s; }' % color.name())
        self.button2.clicked.connect(self.clicked2)
        self.button2.move(500, 50)
        self.button2.resize(100, 50)
        
        self.list = QListWidget(self)
        self.list.setGeometry(125, 125, 650, 170)
        self.item1 = QListWidgetItem()
        self.list.addItems

        # Gathering Section
        self.GatheringLabel = QtWidgets.QLabel('Gathering', self)
        self.GatheringLabel.move(50, Parameter5)
        self.Checkbox1 = QCheckBox('Oil', self)
        self.Checkbox1.move(50, (Parameter5 + 50))
        self.Checkbox1.stateChanged.connect(self.OilBox)
        self.Checkbox2 = QCheckBox('Food', self)
        self.Checkbox2.move(50, (Parameter5 + 80))
        self.Checkbox2.stateChanged.connect(self.FoodBox)
        self.Checkbox3 = QCheckBox('Iron', self)
        self.Checkbox3.move(50, (Parameter5 + 110))
        self.Checkbox3.stateChanged.connect(self.IronBox)
        self.Checkbox4 = QCheckBox('Lumber', self)
        self.Checkbox4.move(50, (Parameter5 + 140))
        self.Checkbox4.stateChanged.connect(self.LumberBox)
        # Alliance Section
        self.AllianceLabel = QtWidgets.QLabel('Alliance', self)
        self.AllianceLabel.move(150, Parameter5)
        self.HelpCheckbox = QCheckBox('Help', self)
        self.HelpCheckbox.move(150, Parameter5 + 50)
        self.HelpCheckbox.stateChanged.connect(self.HelpBox)
        self.TechCheckbox = QCheckBox('Tech', self)
        self.TechCheckbox.move(150, Parameter5 + 80)
        self.TechCheckbox.stateChanged.connect(self.TechBox)
        self.SalaryCheckbox = QCheckBox('Salary', self)
        self.SalaryCheckbox.move(150, Parameter5 + 110)
        self.SalaryCheckbox.stateChanged.connect(self.SalaryBox)
        self.GiftCheckbox = QCheckBox('Gifts', self)
        self.GiftCheckbox.move(150, Parameter5 + 140)
        self.GiftCheckbox.stateChanged.connect(self.GiftBox)
        # Transports Section
        self.TransportsLabel = QtWidgets.QLabel('Transports', self)
        self.TransportsLabel.move(250, Parameter5)
        self.PowerPlantCheckbox = QCheckBox('Power Plants', self)
        self.PowerPlantCheckbox.move(250, Parameter5 + 50)
        self.PowerPlantCheckbox.stateChanged.connect(self.PowerPlantBox)
        self.ChipsCheckbox = QCheckBox('Chips', self)
        self.ChipsCheckbox.move(250, Parameter5 + 80)
        self.ChipsCheckbox.stateChanged.connect(self.ChipsBox)
        self.EnergyCoreCheckbox = QCheckBox('Energy Cores', self)
        self.EnergyCoreCheckbox.move(250, Parameter5 + 110)
        self.EnergyCoreCheckbox.stateChanged.connect(self.ECBox)
        self.RationsCheckbox = QCheckBox('Ration Truck', self)
        self.RationsCheckbox.move(250, Parameter5 + 140)
        self.RationsCheckbox.stateChanged.connect(self.RationsBox)
        self.ExplorationCheckbox = QCheckBox('Exploration', self)
        self.ExplorationCheckbox.move(250, Parameter5 + 170)
        self.ExplorationCheckbox.stateChanged.connect(self.ExplorationBox)
        # Upgrades Section
        self.upgradeLabel = QtWidgets.QLabel('Upgrades', self)
        self.upgradeLabel.move(350, Parameter5)
        self.RSSBuildings = QCheckBox('RSS Buildings', self)
        self.RSSBuildings.move(350, Parameter5 + 50)
        self.RSSBuildings.stateChanged.connect(self.window3)
        self.storages = QCheckBox('Storages', self)
        self.storages.move(350, Parameter5 + 80)
        self.storages.stateChanged.connect(self.StoragesBox)
        self.base = QCheckBox('Base', self)
        self.base.move(350, Parameter5 + 110)
        self.base.stateChanged.connect(self.BaseBox)
        self.UpgradeCheckbox = QtWidgets.QCheckBox('Building Upgrades', self)
        self.UpgradeCheckbox.move(350, Parameter5 + 140)
        self.UpgradeCheckbox.clicked.connect(self.window1)
        # Other Section
        self.otherLabel = QtWidgets.QLabel('Other', self)
        self.otherLabel.move(450, Parameter5)
        self.NQ = QCheckBox('National Quest', self)
        self.NQ.move(450, Parameter5 + 50)
        self.NQ.stateChanged.connect(self.NQBox)
        self.PC = QCheckBox('Production Center', self)
        self.PC.move(450, Parameter5 + 80)
        self.PC.stateChanged.connect(self.PCBox)
        self.Shield = QtWidgets.QCheckBox('Shield', self)
        self.Shield.move(450, Parameter5 + 110)
        self.Shield.clicked.connect(self.window2)
        self.HeliCheckbox = QCheckBox('Helicopter', self)
        self.HeliCheckbox.move(450, Parameter5 + 140)
        self.HeliCheckbox.stateChanged.connect(self.HeliBox)
        self.MailCheckbox = QCheckBox('Mail', self)
        self.MailCheckbox.move(450, Parameter5 + 170)
        self.MailCheckbox.stateChanged.connect(self.MailBox)
        # Military Section
        self.MilitaryLabel = QtWidgets.QLabel('Military', self)
        self.MilitaryLabel.move(550, Parameter5)
        self.Heroes = QtWidgets.QCheckBox('Hero Recruit', self)
        self.Heroes.move(550, Parameter5 + 50)
        self.Heroes.stateChanged.connect(self.HeroesBox)
        self.Missiles = QtWidgets.QCheckBox('Missiles', self)
        self.Missiles.move(550, Parameter5 + 80)
        self.Missiles.stateChanged.connect(self.MissilesBox)
        self.Training = QtWidgets.QCheckBox('Training Troops', self)
        self.Training.move(550, Parameter5 + 110)
        self.Training.stateChanged.connect(self.window4)
        self.Hospital = QCheckBox('Hospital', self)
        self.Hospital.move(550, Parameter5 + 140)
        self.Hospital.stateChanged.connect(self.HospitalBox)
        self.Parts = QtWidgets.QCheckBox('Parts', self)
        self.Parts.move(550, Parameter5 + 170)
        self.Parts.stateChanged.connect(self.PartsBox)

    def test(self, state):
        if state == QtCore.Qt.Checked:
            print('yes')
        else:
            print('no')
    # The Load Last Shelter Button
    def clicked(self):
        Bluestacks()
        BlueStacksReady()
        LastShelter()
        LastShelterLoading()
        time.sleep(5)
        WastelandNews(), time.sleep(5)
        CustomAvatar()

    # All of the resource Check Boxes
    def OilBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Oil for Gathering')
            global Oil
            Oil = True
        else:
            print('Unchecked Oil for Gathering')
            Oil = False

    def FoodBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Food for Gathering')
            global Food
            Food = True
        else:
            print('Unchecked Food for Gathering')
            Food = False

    def IronBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Iron for Gathering')
            global Iron
            Iron = True
        else:
            print('Unchecked Iron for Gathering')
            Iron = False

    def LumberBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Lumber for Gathering')
            global Lumber
            Lumber = True
        else:
            print('Unchecked Lumber for Gathering')
            Lumber = False
    # Section of Alliance Checkbox Functions
    def HelpBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Help for Alliance')
            global Help
            Help = True
        else:
            print('Unchecked Help for Alliance')
            Help = False

    def TechBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Technology for Alliance')
            global Tech
            Tech = True
        else:
            print('Unchecked Technology for Alliance')
            Tech = False

    def SalaryBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Salary for Alliance')
            global Salary
            Salary = True
        else:
            print('Unchecked Salary for Alliance')
            Salary = False
    def GiftBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Gifts for Alliance')
            global Gift
            Gift = True
        else:
            print('Unchecked Gifts for Alliance')
            Gift = False
    # Section of Transport Checkbox Functions
    def PowerPlantBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Power Plants for Vehicles')
            global PowerPlant
            PowerPlant = True
        else:
            print('Unchecked Power Plants for Vehicles')
            PowerPlant = False

    def ChipsBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Chips for Vehicles')
            global Chips
            Chips = True
        else:
            print('Unchecked Chips for Vehicles')
            Chips = False

    def ECBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Energy Cores for Vehicles')
            global EC
            EC = True
        else:
            print('Unchecked Energy Cores for Vehicles')
            EC = False

    def RationsBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Ration Truck for Vehicles')
            global Rations
            Rations = True
        else:
            print('Unchecked Ration Truck for Vehicles')
            Rations = False

    def ExplorationBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Exploration for Vehicles')
            global Exploration
            Exploration = True
        else:
            print('Unchecked Exploration for Vehicles')
            Exploration = False
    # Section of Upgrades Checkbox Functions

    def OtherRSSBuildingsBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Other Resource Buildings for Upgrades')
            global OtherRSSBuildings
            OtherRSSBuildings = True
        else:
            print('Unchecked Other Resource Buildings for Upgrades')
            OtherRSSBuildings = False

    def StoragesBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Resource Storages for Upgrades')
            global Storages
            Storages = True
        else:
            print('Unchecked Resource Storages for Upgrades')
            Storages = False

    def BaseBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Base for Upgrades')
            global Base
            Base = True
        else:
            print('Unchecked Base for Upgrades')
            Base = False


    # Section of Other Checkbox Functions
    def NQBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked National Quests for Other')
            global NQ
            NQ = True
        else:
            print('Unchecked National Quests for Other')
            NQ = False
    def HospitalBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Hospital for Other')
            global Hospital
            Hospital = True
        else:
            print('Unchecked Hospital for Other')
            Hospital = False
    def PCBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Production Center for Other')
            global PC
            PC = True
        else:
            print('Unchecked Production Center for Other')
            PC = False
    def HeliBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Shield for Other')
            global Heli
            Heli = True
        else:
            print('Unchecked Shield for Other')
            Heli = False
    # Section of Other 2 Checkbox Functions
    def MailBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Mail for Other 2')
            global Mail
            Mail = True
        else:
            print('Unchecked Mail for Other 2')
            Mail = False
    # Military Function Section
    def HeroesBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Heroes for Military')
        else:
            print('Unchecked Heroes for Military')
    def MissilesBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Missiles for Military')
        else:
            print('Unchecked Missiles for Military')
    def PartsBox(self, state):
        if state == QtCore.Qt.Checked:
            print('Checked Parts for Military')
            global Parts
            Parts = True
        else:
            print('Unechecked Parts for Military')
            Parts = False
    # The Run Button
    def clicked2(self):
        print('--------------------Process Starting--------------------')
        # Transport Section of Functions
        if self.PowerPlantCheckbox.isChecked() is True:
            Transports.MainPowerPlant()
        if self.ChipsCheckbox.isChecked() is True:
            Transports.main_chips()
        # Upgrades Section of Functions
        WaterFilterU = self.ui3.WaterFilter.isChecked()
        FarmU = self.ui3.Farm.isChecked()
        LumberMillU = self.ui3.LumberMill.isChecked()
        OilWellU = self.ui3.OilWell.isChecked()
        RefineryU = self.ui3.Refinery.isChecked()
        WindTurbineU = self.ui3.WindTurbine.isChecked()
        PowerPlantsU = self.ui3.PowerPlants.isChecked()
        BanksU = self.ui3.Banks.isChecked()
        UList = [WaterFilterU, FarmU, LumberMillU, OilWellU, RefineryU, WindTurbineU, PowerPlantsU, BanksU]
        # If the Main Checkbox is 'Unchecked'/False then it set all checkboxes inside to 'Unchecked'/False
        if self.RSSBuildings.isChecked() is False:
            self.ui3.WaterFilter.setChecked(False)
            self.ui3.Farm.setChecked(False)
            self.ui3.LumberMill.setChecked(False)
            self.ui3.OilWell.setChecked(False)
            self.ui3.Refinery.setChecked(False)
            self.ui3.WindTurbine.setChecked(False)
            self.ui3.PowerPlants.setChecked(False)
            self.ui3.Banks.setChecked(False)
        # If Nothing inside is 'Checked'/True but the main box is 'Checked'/True', it sets it to 'Unchecked'/False
        if not any(UList):
            self.RSSBuildings.setChecked(False)
        # Checks If More Than One Upgrade is Selected.
        if self.RSSBuildings.isChecked() is True:
            if WaterFilterU is True:
                assert not any(UList[1:]), 'More Than One RSS Upgrade is Selected!'
                print('Water Filter Upgrade')
            if FarmU is True:
                assert not any(UList[2:]) and not UList[0], 'More Than One RSS Upgrade is Selected!'
                print('Farm Upgrade')
            if LumberMillU is True:
                assert not any(UList[3:]) and not any(UList[:2]), 'More Than One RSS Upgrade is Selected!'
                print('Lumber Mill Upgrade')
            if OilWellU is True:
                assert not any(UList[4:]) and not any(UList[:3]), 'More Than One RSS Upgrade is Selected!'
                print('Oil Well Upgrade')
            if RefineryU is True:
                assert not any(UList[5:]) and not any(UList[:4]), 'More Than One RSS Upgrade is Selected!'
                print('Refinery Upgrade')
            if WindTurbineU is True:
                assert not any(UList[6:]) and not any(UList[:5]), 'More Than One RSS Upgrade is Selected!'
                print('Wind Turbine Upgrade')
            if PowerPlantsU is True:
                assert not UList[7] and not any(UList[:6]), 'More Than One RSS Upgrade is Selected!'
                print('Power Plants Upgrade')
            if BanksU is True:
                assert not any(UList[:7]), 'More Than One RSS Upgrade is Selected!'
                print('Banks Upgrade')

        if self.ui1.chips.isChecked() is True:
            print('yes')
        # Misc Section of Functions
        if self.NQ.isChecked() is True:
            Misc.MainQuest(True)
        if self.Shield.isChecked() is False:  # If Shield is False then everything inside of it is False
            self.ui2.EightHours.setChecked(False)
            self.ui2.OneDay.setChecked(False)
            self.ui2.ThreeDays.setChecked(False)
        if self.ui2.EightHours.isChecked() is False and self.ui2.OneDay.isChecked() is False:
            if self.ui2.ThreeDays.isChecked() is False:  # If everything inside of Shield is False then Shield is False
                self.Shield.setChecked(False)
        if self.ui2.EightHours.isChecked() is True:
            Misc.EightHourShield()
        if self.ui2.OneDay.isChecked() is True:
            Misc.OneDayShield()
        if self.ui2.ThreeDays.isChecked() is True:
            Misc.ThreeDayShield()
        if self.HeliCheckbox.isChecked() is True:
            Misc.Helicopter()
        if self.PC.isChecked() is True:
            Misc.ProductionCenter()
        if self.MailCheckbox.isChecked() is True:
            Misc.Mail()
        # Military Section of Functions
        if self.Heroes.isChecked() is True:
            Military.HeroRecruit()
        if self.Parts.isChecked() is True:
            Military.Parts()
        if self.Training.isChecked() is False:
            self.ui4.VehicleT1.setChecked(False), self.ui4.VehicleCustom.setChecked(False)
            self.ui4.ShooterT1.setChecked(False), self.ui4.ShooterCustom.setChecked(False)
            self.ui4.FighterT1.setChecked(False), self.ui4.FighterCustom.setChecked(False)
        if self.ui4.VehicleT1.isChecked() is True:
            Military.VehicleFactory(1)
        if self.ui4.VehicleCustom.isChecked() is True:
            tier = re.sub('[^0-9]', '', str(self.ui4.VehicleInput))
            Military.VehicleFactory(tier)
        if self.ui4.ShooterT1.isChecked() is True:
            Military.ShootingRange(1)
        if self.ui4.ShooterCustom.isChecked() is True:
            tier = re.sub('[^0-9]', '', str(self.ui4.ShooterInput))
            Military.ShootingRange(tier)
        if self.ui4.FighterT1.isChecked() is True:
            Military.FighterCamp(1)
        if self.ui4.FighterCustom.isChecked() is True:
            tier = re.sub('[^0-9]', '', str(self.ui4.FighterInput))
            Military.FighterCamp(tier)
        # Alliance Section of Functions
        if self.HelpCheckbox.isChecked() is True:
            Alliance.Help()
        if self.TechCheckbox.isChecked() is True:
            Alliance.Tech()
        if self.SalaryCheckbox.isChecked() is True:
            Alliance.Salary()
        if self.GiftCheckbox.isChecked() is True:
            Alliance.Gifts()
        # Gathering Section of Functions
        Oil = self.Checkbox1.isChecked()
        Food = self.Checkbox2.isChecked()
        Iron = self.Checkbox3.isChecked()
        Lumber = self.Checkbox4.isChecked()
        if Oil is True:
            if Food is False and Iron is False and Lumber is False:
                print('Gathering Oil')
                Gathering()
                GatherOil(1, 0)
                if Lvl9Oil is False:
                    GatherOil(2, 0)
                    GatherOil(2, 0)
                    GatherOil(2, 0)
                else:
                    GatherOil(1, 0)
                    GatherOil(1, 0)
                    GatherOil(1, 0)
            if Food is True:
                if Lumber is False and Iron is False:
                    print('Gathering Oil and Food')
                    Gathering()
                    GatherOil(1, 0)
                    if Lvl9Oil is False:
                        GatherOil(2, 0)
                    else:
                        GatherOil(1, 0)
                    GatherFood(1, 0)
                    if Lvl9Food is False:
                        GatherFood(2, 0)
                    else:
                        GatherFood(1, 0)
                if Iron is True:
                    if Lumber is False:
                        print('Gathering Oil, Food, and Iron')
                        Gathering()
                        GatherOil(1, 0)
                        GatherFood(1, 0)
                        GatherIron(1, 0)
                        if Lvl9Iron is False:
                            GatherIron(2, 0)
                        else:
                            GatherIron(1, 0)
                    if Lumber is True:
                        print('Gathering Oil, Food, Iron, and Lumber')
                        Gathering()
                        GatherOil(1, 0)
                        GatherFood(1, 0)
                        GatherIron(1, 0)
                        GatherLumber(1, 0)
                if Lumber is True:
                    if Iron is False:
                        print('Gathering Oil, Food, and Lumber')
                        Gathering()
                        GatherOil(1, 0)
                        GatherFood(1, 0)
                        GatherLumber(1, 0)
                        if Lvl9Lumber is False:
                            GatherLumber(2, 0)
                        else:
                            GatherLumber(1, 0)
            if Iron is True:
                if Lumber is False and Food is False:
                    print('Gathering Oil and Iron')
                    Gathering()
                    GatherOil(1, 0)
                    if Lvl9Oil is False:
                        GatherOil(2, 0)
                    else:
                        GatherOil(1, 0)
                    GatherIron(1, 0)
                    if Lvl9Iron is False:
                        GatherIron(2, 0)
                    else:
                        GatherIron(1, 0)
                if Lumber is True:
                    if Food is False:
                        print('Gathering Oil, Iron, and Lumber')
                        Gathering()
                        GatherOil(1, 0)
                        GatherIron(1, 0)
                        if Lvl9Iron is False:
                            GatherIron(2, 0)
                        else:
                            GatherIron(1, 0)
                        GatherLumber(1, 0)
            if Lumber is True:
                if Iron is False and Food is False:
                    print('Gathering Oil and Lumber')
                    Gathering()
                    GatherOil(1, 0)
                    if Lvl9Oil is False:
                        GatherOil(2, 0)
                    else:
                        GatherOil(1, 0)
                    GatherLumber(1, 0)
                    if Lvl9Lumber is False:
                        GatherLumber(2, 0)
                    else:
                        GatherLumber(1, 0)
        if Food is True:
            if Oil is False and Lumber is False and Iron is False:
                print('Gathering Food')
                Gathering()
                GatherFood(1, 0)
                if Lvl9Food is False:
                    GatherFood(2, 0)
                    GatherFood(2, 0)
                    GatherFood(2, 0)
                else:
                    GatherFood(1, 0)
                    GatherFood(1, 0)
                    GatherFood(1, 0)
            if Iron is True:
                if Oil is False and Lumber is False:
                    print('Gathering Food and Iron')
                    Gathering()
                    GatherFood(1, 0)
                    if Lvl9Food is False:
                        GatherFood(2, 0)
                    else:
                        GatherFood(1, 0)
                    GatherIron(1, 0)
                    if Lvl9Iron is False:
                        GatherIron(2, 0)
                    else:
                        GatherIron(1, 0)
                if Lumber is True:
                    if Oil is False:
                        print('Gathering Food, Iron, and Lumber')
                        Gathering()
                        GatherFood(1, 0)
                        GatherIron(1, 0)
                        if Lvl9Iron is False:  # If the error 'No Target has been found' comes up, skip straight to lvl8
                            GatherIron(2, 0)
                        else:
                            GatherIron(1, 0)
                        GatherLumber(1, 0)
            if Lumber is True:
                if Oil is False and Iron is False:
                    print('Gathering Food and Lumber')
                    Gathering()
                    GatherFood(1, 0)
                    if Lvl9Food is False:
                        GatherFood(2, 0)
                    else:
                        GatherFood(1, 0)
                    GatherLumber(1, 0)
                    if Lvl9Lumber is False:
                        GatherLumber(2, 0)
                    else:
                        GatherLumber(1, 0)
        if Iron is True:
            if Oil is False and Lumber is False and Food is False:
                print('Gathering Iron')
                Gathering()
                GatherIron(1, 0)
                if Lvl9Iron is False:
                    GatherIron(2, 0)
                    GatherIron(2, 0)
                    GatherIron(2, 0)
                else:
                    GatherIron(1, 0)
                    GatherIron(1, 0)
                    GatherIron(1, 0)

            if Lumber is True:
                if Oil is False and Food is False:
                    print('Gathering Iron and Lumber')
                    Gathering()
                    GatherIron(1, 0)
                    if Lvl9Iron is False:
                        GatherIron(2, 0)
                    else:
                        GatherIron(1, 0)
                    GatherLumber(1, 0)
                    if Lvl9Lumber is False:
                        GatherLumber(2, 0)
                    else:
                        GatherLumber(1, 0)
        if Lumber is True:
            if Oil is False and Iron is False and Food is False:
                print('Gathering Lumber')
                Gathering()
                GatherLumber(1, 0)
                if Lvl9Lumber is False:
                    GatherLumber(2, 0)
                    GatherLumber(2, 0)
                    GatherLumber(2, 0)
                else:
                    GatherLumber(1, 0)
                    GatherLumber(1, 0)
                    GatherLumber(1, 0)
        if Lumber is False and Iron is False and Food is False and Oil is False:
            print('--------------------Process Finished--------------------')
# What runs the application window
def window():
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    sys.exit(app.exec_())


window()
