import time
import pytesseract
import pyautogui as pg
import pyscreenshot
import cv2
import imutils
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
def ToHospital(spot):
    pg.click(spot), time.sleep(0.5), pg.click(637, 447), time.sleep(2), pg.click(679, 406)  # To The Hospital
    time.sleep(0.75), pg.click(786, 447), time.sleep(2)  # Gets inside the Hopsital
    pg.click(823, 739)  # Clicks Heal

def Hospital():
    time.sleep(1), pg.click(876, 695), time.sleep(1.5), pg.click(648, 453), time.sleep(2)
    Check1 = 482, 692, 576, 736
    Check2 = 604, 692, 704, 736
    Check3 = 724, 692, 829, 736
    ImageToString(Check1)
    if 'Hospital' in data:
        print('Hospital Detected in Spot 1')
        FirstSpot = 531, 687
        ToHospital(FirstSpot)
    else:
        ImageToString(Check2)
        if 'Hospital' in data:
            print('Hospital Detected In Spot 2')
            SecondSpot = 649, 675
            ToHospital(SecondSpot)
        else:
            ImageToString(Check3)
            if 'Hospital' in data:
                print('Hospital Detected In Spot 3')
                ThirdSpot = 791, 680
                ToHospital(ThirdSpot)
            else:
                print('No Hospital Detected in first 3 spots')
                print('Stopping Hospital Program')
def HeroRecruit():
    time.sleep(1), pg.click(873, 641), time.sleep(4), pg.click(605, 733), time.sleep(2)  # Goes to HeroRecruitment
    for i in range(0, 3):
        pg.click(580, 592), time.sleep(3.5), pg.doubleClick(839, 128), time.sleep(3.5), pg.click(826, 705)
        time.sleep(1.25)
    pg.click(507, 23), time.sleep(1.5), pg.click(507, 23)
    print('Hero Recruitment for Military Completed')

def ToParts(spot):
    pg.click(spot), time.sleep(0.5), pg.click(637, 447), time.sleep(2), pg.click(679, 406)
    time.sleep(2), pg.click(679, 406)  # Goes to Parts Factory
    time.sleep(1.5), pg.click(754, 468), time.sleep(4)  # Gets inside material production
    pg.moveTo(843, 483), pg.dragTo(681, 392, 1), time.sleep(0.5), pg.moveTo(757, 569), pg.dragTo(681, 392, 1)
    time.sleep(0.5)  # Last 2 Materials for Parts
    pg.moveTo(594, 571), pg.dragTo(681, 392, 1), time.sleep(0.5), pg.moveTo(518, 482), pg.dragTo(681, 392, 1)
    time.sleep(0.5)  # First 2 Materials for Parts
    pg.click(498, 21)
    print('Parts Production for Military Completed')
def Parts():
    time.sleep(1), pg.click(869, 693), time.sleep(1.5), pg.click(647, 460)  # Goes to Military Tab
    Check1 = 482, 700, 576, 746
    Check2 = 604, 700, 704, 746
    Check3 = 734, 700, 829, 746
    ImageToString(Check1)
    if 'Parts' in data:
        print('Parts Factory Detected in Spot 1')
        FirstSpot = 531, 687
        ToParts(FirstSpot)
    else:
        ImageToString(Check2)
        if 'Parts' in data:
            print('Parts Factory Detected In Spot 2')
            SecondSpot = 649, 675
            ToParts(SecondSpot)
        else:
            ImageToString(Check3)
            if 'Parts' in data:
                print('Parts Factory Detected In Spot 3')
                ThirdSpot = 791, 680
                ToParts(ThirdSpot)
            else:
                def SpotCheck(count):
                    pg.moveTo(782, 684), pg.dragTo(531, 682, 1.35), pg.dragTo(532, 682), time.sleep(1)
                    ImageToString(Check2)
                    if 'Parts' in data:
                        print('Parts Factory Detected in Spot ' + str(count))
                        SecondSpot = 649, 675
                        ToParts(SecondSpot)
                    else:
                        count += 1
                        ImageToString(Check3)
                        if 'Parts' in data:
                            print('Parts Factory Detected in Spot ' + str(count))
                            ThirdSpot = 791, 680
                            ToParts(ThirdSpot)
                        else:
                            count += 1
                            SpotCheck(count)
                SpotCheck(4)
def ToVehicleFactory(spot, tier):
    pg.click(spot), time.sleep(0.5), pg.click(637, 447), time.sleep(2), pg.click(679, 406)
    time.sleep(2), pg.click(679, 406)  # Goes to Vehicle Factory
    time.sleep(1.5), pg.click(787, 448), time.sleep(1.5)
    for i in range(0, 3):
        pg.moveTo(534, 533), pg.dragTo(842, 533, 0.5)
    tier += 1
    for l in range(2, tier):
        pg.click(754, 540)
        time.sleep(0.5)
    time.sleep(1.5), pg.click(778, 731)
    tier -= 1
    time.sleep(0.75), pg.click(480, 45)
    print('Finished Training Tier ' + str(tier) + ' Vehicles')
def VehicleFactory(tier):
    time.sleep(1), pg.click(869, 693), time.sleep(1.5), pg.click(647, 460)  # Goes to Military Tab
    Check1 = 472, 700, 586, 746
    Check2 = 594, 700, 714, 746
    Check3 = 724, 700, 839, 746
    ImageToString(Check1)
    if 'Vehicle' in data or 'Factory' in data:
        print('Vehicle Factory Detected in Spot 1')
        FirstSpot = 531, 687
        ToVehicleFactory(FirstSpot, tier)
    else:
        ImageToString(Check2)
        if 'Vehicle' in data or 'Factory' in data:
            print('Vehicle Factory Detected In Spot 2')
            SecondSpot = 649, 675
            ToVehicleFactory(SecondSpot, tier)
        else:
            ImageToString(Check3)
            if 'Vehicle' in data or 'Factory' in data:
                print('Vehicle Factory Detected In Spot 3')
                ThirdSpot = 791, 680
                ToVehicleFactory(ThirdSpot, tier)
            else:
                def SpotCheck(count):
                    count2 = 0
                    pg.moveTo(782, 684), pg.dragTo(560, 682, 1.35), pg.click(None, None, 1, 1)
                    time.sleep(1)
                    ImageToString(Check2)
                    if 'Vehicle' in data or 'Factory' in data:
                        print('Vehicle Factory Detected in Spot ' + str(count))
                        SecondSpot = 649, 675
                        ToVehicleFactory(SecondSpot, tier)
                    else:
                        count += 1
                        ImageToString(Check3)
                        if 'Vehicle' in data or 'Factory' in data:
                            print('Vehicle Factory Detected in Spot ' + str(count))
                            ThirdSpot = 791, 680
                            ToVehicleFactory(ThirdSpot, tier)
                        else:
                            count += 1
                            if count > 16:
                                for i in range(0, 6):
                                    pg.moveTo(560, 682), pg.dragTo(782, 682, 0.5)
                                count -= count
                                SpotCheck(4)
                                count2 += 1
                            else:
                                if count2 < 1:
                                    SpotCheck(count)


                SpotCheck(4)
def ToShootingRange(spot, tier):
    pg.click(spot), time.sleep(0.5), pg.click(637, 447), time.sleep(2), pg.click(679, 406)
    time.sleep(2), pg.click(679, 406)  # Goes to Shooting Range
    time.sleep(1.5), pg.click(787, 448), time.sleep(1.5)
    for i in range(0, 3):
        pg.moveTo(534, 533), pg.dragTo(842, 533, 0.5)
    tier += 1
    for l in range(2, tier):
        pg.click(754, 540)
        time.sleep(0.5)
    time.sleep(1.5), pg.click(778, 731)
    tier -= 1
    time.sleep(0.75), pg.click(480, 45)
    print('Finished Training Tier ' + str(tier) + ' Shooters')
def ShootingRange(tier):
    time.sleep(1), pg.click(869, 693), time.sleep(1.5), pg.click(647, 460)  # Goes to Military Tab
    Check1 = 472, 700, 586, 746
    Check2 = 594, 700, 714, 746
    Check3 = 724, 700, 839, 746
    ImageToString(Check1)
    if 'Shooting' in data or 'Range' in data:
        print('Shooting Range Detected in Spot 1')
        FirstSpot = 531, 687
        ToShootingRange(FirstSpot, tier)
    else:
        ImageToString(Check2)
        if 'Shooting' in data or 'Range' in data:
            print('Shooting Range Detected In Spot 2')
            SecondSpot = 649, 675
            ToShootingRange(SecondSpot, tier)
        else:
            ImageToString(Check3)
            if 'Shooting' in data or 'Range' in data:
                print('Shooting Range Detected In Spot 3')
                ThirdSpot = 791, 680
                ToShootingRange(ThirdSpot, tier)
            else:
                def SpotCheck(count):
                    count2 = 0
                    pg.moveTo(782, 684), pg.dragTo(560, 682, 1.35), pg.click(None, None, 1, 1)
                    time.sleep(1)
                    ImageToString(Check2)
                    if 'Shooting' in data or 'Range' in data:
                        print('Shooting Range Detected in Spot ' + str(count))
                        SecondSpot = 649, 675
                        ToShootingRange(SecondSpot, tier)
                    else:
                        count += 1
                        ImageToString(Check3)
                        if 'Shooting' in data or 'Range' in data:
                            print('Shooting Range Detected in Spot ' + str(count))
                            ThirdSpot = 791, 680
                            ToShootingRange(ThirdSpot, tier)
                        else:
                            count += 1
                            if count > 16:
                                for i in range(0, 6):
                                    pg.moveTo(560, 682), pg.dragTo(782, 682, 0.5)
                                count -= count
                                SpotCheck(4)
                                count2 += 1
                            else:
                                if count2 < 1:
                                    SpotCheck(count)

                SpotCheck(4)
def ToFighterCamp(spot, tier):
    pg.click(spot), time.sleep(0.5), pg.click(637, 447), time.sleep(2), pg.click(679, 406)
    time.sleep(2), pg.click(679, 406)  # Goes to Fighter Camp
    time.sleep(1.5), pg.click(787, 448), time.sleep(1.5)
    for i in range(0, 3):
        pg.moveTo(534, 533), pg.dragTo(842, 533, 0.5)
    tier += 1
    for l in range(2, tier):
        pg.click(754, 540)
        time.sleep(0.5)
    time.sleep(1.5), pg.click(778, 731)
    tier -= 1
    time.sleep(0.75), pg.click(480, 45)
    print('Finished Training Tier ' + str(tier) + ' Fighters')
def FighterCamp(tier):
    time.sleep(1), pg.click(869, 693), time.sleep(1.5), pg.click(647, 460)  # Goes to Military Tab
    Check1 = 472, 700, 586, 746
    Check2 = 594, 700, 714, 746
    Check3 = 724, 700, 839, 746
    ImageToString(Check1)
    if 'Fighter' in data or 'Camp' in data:
        print('Fighter Camp Detected in Spot 1')
        FirstSpot = 531, 687
        ToFighterCamp(FirstSpot, tier)
    else:
        ImageToString(Check2)
        if 'Fighter' in data or 'Camp' in data:
            print('Fighter Camp Detected In Spot 2')
            SecondSpot = 649, 675
            ToFighterCamp(SecondSpot, tier)
        else:
            ImageToString(Check3)
            if 'Fighter' in data or 'Camp' in data:
                print('Fighter Camp Detected In Spot 3')
                ThirdSpot = 791, 680
                ToFighterCamp(ThirdSpot, tier)
            else:
                def SpotCheck(count):
                    count2 = 0
                    pg.moveTo(782, 684), pg.dragTo(560, 682, 1.35), pg.click(None, None, 1, 1)
                    time.sleep(1)
                    ImageToString(Check2)
                    if 'Fighter' in data or 'Camp' in data:
                        print('Fighter Camp Detected in Spot ' + str(count))
                        SecondSpot = 649, 675
                        ToFighterCamp(SecondSpot, tier)
                    else:
                        count += 1
                        ImageToString(Check3)
                        if 'Fighter' in data or 'Camp' in data:
                            print('Fighter Camp Detected in Spot ' + str(count))
                            ThirdSpot = 791, 680
                            ToFighterCamp(ThirdSpot, tier)
                        else:
                            count += 1
                            if count > 16:
                                for i in range(0, 6):
                                    pg.moveTo(560, 682), pg.dragTo(782, 682, 0.5)
                                count -= count
                                SpotCheck(4)
                                count2 += 1
                            else:
                                if count2 < 1:
                                    SpotCheck(count)

                SpotCheck(4)