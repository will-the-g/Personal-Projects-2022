import pyautogui as pg
import time
import Checks
import pyscreenshot
import pytesseract
import cv2
import imutils
import re

def ImageToColor(coords, color):
    screenshot = pyscreenshot.grab(bbox=(coords))
    global count
    count = 0
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            if screenshot.getpixel((x, y)) == color:
              count += 1
            # print(screenshot.getpixel((x, y)))
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

def RSSCheck():
    coords = 642, 379, 733, 413
    color = 255, 155, 24
    ImageToColor(coords, color)
    if count > 0:
        print('Electricity Detected')
        global Electricity
        Electricity = True
    else:
        Electricity = False
    color2 = 50, 148, 200
    ImageToColor(coords, color2)
    if count > 0:
        print('Water Detected')
        global Water
        Water = True
    else:
        Water = False
    color3 = 126, 141, 153
    ImageToColor(coords, color3)
    if count > 0:
        print('Oil Detected')
        global Oil
        Oil = True
    else:
        Oil = False
    color4 = 124, 108, 74
    ImageToColor(coords, color4)
    if count > 0:
        print('Iron Detected')
        global Iron
        Iron = True
    else:
        Iron = False
    color5 = 255, 192, 1
    ImageToColor(coords, color5)
    if count > 0:
        print('Food Detected')
        global Food
        Food = True
    else:
        Food = False
    color6 = 203, 143, 81
    ImageToColor(coords, color6)
    if count > 0:
        print('Lumber Detected')
        global Lumber
        Lumber = True
    else:
        Lumber = False
def IronCheck():
    Coords = 679, 291, 708, 306
    ImageToString(Coords)
    if 'Iron' in data or 'Iran' in data:
        global IronChecks
        IronChecks = True
        print('Iron Detected in Trade')
    else:
        IronChecks = False
def BottomFour(Coord1, Coord2):
    pg.click(Coord1, Coord2)  # Bottom Left Trade
    RSSCheck()
    if Electricity is True or Water is True:
        idk2()
    if Oil is True or Iron is True or Food is True or Lumber is True:
        IronCheck()
        if IronChecks is True:
            idk2()
        if IronChecks is False:
            time.sleep(0.75), pg.click(743, 122), time.sleep(0.25)
def ReplenishCheck():
    Coords = 594, 7, 772, 42
    ImageToString(Coords)
    if 'Replenish Resources' in data:
        print('Replenish Resources is needed')
        time.sleep(0.5), pg.click(500, 24), time.sleep(1.5), pg.click(715, 140)

def idk2():
    time.sleep(0.75), pg.click(691, 394), time.sleep(0.75), ReplenishCheck()  # Clicks the Trade Button
def Helicopter():
    time.sleep(1), pg.click(871, 693), time.sleep(1), pg.click(778, 334), time.sleep(1.5), pg.click(660, 686)
    time.sleep(0.5), pg.click(634, 447)  # Gets Position of Helicopter
    time.sleep(2), pg.click(679, 373), time.sleep(1), pg.click(787, 444)  # Gets inside trading area
    time.sleep(1), pg.click(846, 372), idk2(), pg.click(740, 373), idk2(), pg.click(635, 375), idk2()
    pg.click(528, 369), idk2()  # Top 4 Cash Trades
    BottomFour(836, 541)  # Bottom Right
    BottomFour(743, 538)  # Bottom 2nd on the Right
    BottomFour(627, 540)  # Bottom 2nd on the Left
    BottomFour(534, 536)  # Bottom Left
    time.sleep(1), pg.click(871, 242), time.sleep(1), pg.click(686, 442), time.sleep(1.5)  # Free Refresh
    time.sleep(1), pg.click(846, 372), idk2(), pg.click(740, 373), idk2(), pg.click(635, 375), idk2()
    pg.click(528, 369), idk2()  # Top 4 Cash Trades
    BottomFour(836, 541)  # Bottom Right
    BottomFour(743, 538)  # Bottom 2nd on the Right
    BottomFour(627, 540)  # Bottom 2nd on the Left
    BottomFour(534, 536)  # Bottom Left
    pg.click(506, 48)
    print('Helicopter Complete')


def test():
    coords = 642, 379, 733, 413
    coords2 = 658, 385, 674, 408
    color2 = 255, 192, 1
    ImageToColor(coords2, color2)
    if count > 0:
        print('Food Detected')
def ToClassHall(Spot):
    pg.click(Spot), time.sleep(0.5), pg.click(637, 447), time.sleep(2), pg.click(679, 406)  # Goes to Class Hall
    time.sleep(0.75), pg.click(786, 432), time.sleep(2)
    coords = 472, 454, 752, 481
    Choosing(coords, 1)

def NQ():
    time.sleep(1), pg.click(871, 696), time.sleep(1), pg.click(775, 464), time.sleep(1)
    Check1 = 482, 692, 576, 736
    Check2 = 604, 692, 704, 736
    Check3 = 724, 692, 829, 736
    ImageToString(Check1)
    if 'Class Hall' in data:
        print('Class Hall Detected in Spot 1')
        FirstSpot = 531, 687
        ToClassHall(FirstSpot)
    else:
        ImageToString(Check2)
        if 'Class Hall' in data:
            print('Class Hall Detected In Spot 2')
            SecondSpot = 649, 675
            ToClassHall(SecondSpot)
        else:
            ImageToString(Check3)
            if 'Class Hall' in data:
                print('Class Hall Detected In Spot 3')
                ThirdSpot = 791, 680
                ToClassHall(ThirdSpot)
            else:
                print('No Class Hall Detected in first 3 spots')
                print('Stopping NQ Program')

def Choosing(coords, row):
    ImageToString(coords)
    if 'Farm' in data or 'Expert' in data:
        global FarmExpert
        FarmExpert = True
        print('Farm Expert Quest Detected')
        level = int(re.sub('[^0-9]', '', data))
        if level == 1 or level == 5:
            def Availability(x, y):
                time.sleep(0.5), pg.click(x, y)
                time.sleep(2)
                coords = 574, 191, 791, 210
                ImageToString(coords)
                if 'Please choose a Marching Queue' in data:
                    global Available
                    Available = True
                    pg.click(772, 617)
                    time.sleep(5)
                    pg.click(868, 738)
                    print('National Quest Completed')
                else:
                    Available = False
            if row == 1:
                Availability(843, 552)
            if row == 2:
                Availability(843, 704)
            if row == 3:
                Availability(843, 513)
            if Available is False:
                print('No Availability detected in the first row')
                FarmExpert = False

    else:
        FarmExpert = False
        print('Farm Expert Quest Not Found')
def MainQuest(test):
    if test is False:
        coords = 472, 454, 752, 481
        Choosing(coords, 1)
    else:
        NQ()
    if FarmExpert is False:
        coords = 471, 613, 662, 637
        Choosing(coords, 2)
    if FarmExpert is False:
        time.sleep(1)
        pg.scroll(-150)
        time.sleep(1)
        coords = 478, 410, 642, 434
        Choosing(coords, 3)
    if FarmExpert is False:
        time.sleep(1), pg.click(875, 70)
        MainQuest(False)
def ToShield():
    time.sleep(1), pg.click(871, 735), time.sleep(5), pg.click(679, 347), time.sleep(2), pg.click(679, 347)
    time.sleep(2), pg.click(585, 422), time.sleep(1.5), pg.click(845, 96), time.sleep(1.5)
def EightHourShield():
    ToShield()
    pg.click(840, 171), time.sleep(0.75), pg.click(683, 448), time.sleep(1), pg.click(500, 21)
    time.sleep(0.5), pg.click(500, 21), time.sleep(0.75), pg.click(875, 740), time.sleep(1.75)
    print('Eight Hour Shield Completed')
def OneDayShield():
    ToShield()
    pg.click(842, 256), time.sleep(0.75), pg.click(683, 448), time.sleep(1), pg.click(500, 21)
    time.sleep(0.5), pg.click(500, 21), time.sleep(0.75), pg.click(875, 740), time.sleep(1.75)
    print('One Day Shield Completed')
def ThreeDayShield():
    ToShield()
    pg.click(842, 342), time.sleep(0.75), pg.click(683, 448), time.sleep(1), pg.click(500, 21)
    time.sleep(0.5), pg.click(500, 21), time.sleep(0.75), pg.click(875, 740), time.sleep(1.75)
    print('Three Day Shield Completed')
def ToProductionCenter(spot):
    pg.click(spot), time.sleep(0.5), pg.click(637, 447), time.sleep(2), pg.click(679, 406), time.sleep(0.5)
    pg.click(754, 458), time.sleep(0.75), pg.click(686, 529)
    print('Production Center Completed')


def ProductionCenter():
    time.sleep(1), pg.click(869, 694), time.sleep(1), pg.click(777, 463), time.sleep(2)
    Check1 = 482, 700, 576, 746
    Check2 = 604, 700, 704, 746
    Check3 = 734, 700, 829, 746
    ImageToString(Check1)
    if 'Production' in data or 'Center' in data:
        print('Production Center Detected in Spot 1')
        FirstSpot = 531, 687
        ToProductionCenter(FirstSpot)
    else:
        ImageToString(Check2)
        if 'Production' in data or 'Center' in data:
            print('Production Center Detected In Spot 2')
            SecondSpot = 649, 675
            ToProductionCenter(SecondSpot)
        else:
            ImageToString(Check3)
            if 'Production' in data or 'Center' in data:
                print('Production Center Detected In Spot 3')
                ThirdSpot = 791, 680
                ToProductionCenter(ThirdSpot)
            else:
                pg.moveTo(782, 684), pg.dragTo(505, 682, 0.5), time.sleep(1)
                ImageToString(Check2)
                if 'Production' in data or 'Center' in data:
                    print('Production Center Detected in Spot 4')
                    SecondSpot = 649, 675
                    ToProductionCenter(SecondSpot)
                else:
                    ImageToString(Check3)
                    if 'Production' in data or 'Center' in data:
                        print('Production Center Detected in Spot 5')
                        ThirdSpot = 791, 680
                        ToProductionCenter(ThirdSpot)
def Mail():
    def SectionClear(x, y):
        pg.click(x, y), time.sleep(1.25), pg.click(689, 713), time.sleep(0.75)  # Clears Out Section
        pg.click(44, 34), time.sleep(1.5)
    time.sleep(1), pg.click(874, 593), time.sleep(0.5), pg.click(870, 477), time.sleep(3)  # Gets To Mail
    SectionClear(711, 169)
    SectionClear(711, 367)
    SectionClear(711, 555)
    pg.scroll(-350)
    time.sleep(1)
    SectionClear(711, 206)
    SectionClear(711, 396)
    SectionClear(711, 583)
    pg.click(1329, 33), time.sleep(3), pg.click(872, 597)
    print('Mail Complete')
