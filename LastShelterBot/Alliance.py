import time
import pyautogui as pg
import pyscreenshot
import pytesseract


def Tech():
    time.sleep(1)
    pg.moveTo(872, 594)  # Moves to Menu Button
    pg.click()
    time.sleep(0.5)
    pg.moveTo(870, 549)  # Moves to Alliance Button
    pg.click()
    time.sleep(3)
    pg.moveTo(631, 524)  # Moves to Alliance Tech Button
    pg.click()
    time.sleep(1.5)
    pg.scroll(-250)
    time.sleep(2)
    pg.click(856, 278)  # Clicks The Iron Research Button (Automated Guidance)
    time.sleep(0.5)
    pg.moveTo(679, 557)
    pg.click(None, None, 25, 0.5)  # Clicks the RSS Donation
    time.sleep(0.5)
    pg.click(792, 558, 11, 0.5)  # Clicks the Diamond Donation
    time.sleep(0.5)
    pg.click(827, 185)  # Clicks the X Button
    time.sleep(0.25)
    def Switch(x, y):
        pg.click(x, y)
        time.sleep(0.5)
        pg.click(792, 558, 13, 0.5)  # Clicks the Diamond Donation
        pg.click(827, 185)  # Clicks the X Button
        time.sleep(0.25)
    Switch(734, 268)  # Multi-Armed Logger
    Switch(635, 266)  # Bio refinery
    Switch(514, 260)  # Genetic Selection
    pg.click(871, 23)
    time.sleep(1)
    pg.click(874, 590)
    print('Alliance Tech Complete')

def Help():
    time.sleep(1)
    pg.click(872, 596), time.sleep(0.25), pg.click(870, 551), time.sleep(1.5), pg.click(828, 435), time.sleep(1)
    pg.click(677, 737), time.sleep(1), pg.click(873, 26), time.sleep(1), pg.click(875, 597)
    print('Alliance Help Complete')

def Salary():
    def idk():
        time.sleep(0.25), pg.click(711, 129), time.sleep(0.25)
    time.sleep(1), pg.click(872, 596), time.sleep(0.25), pg.click(870, 551), time.sleep(1.5), pg.click(534, 528)
    time.sleep(1), pg.click(541, 364), idk(), pg.click(590, 288), idk(), pg.click(638, 356), idk(), pg.click(678, 288)
    idk(), pg.click(730, 356), idk()  # Claiming Active
    pg.click(689, 210), time.sleep(0.25), pg.click(512, 305), idk(), pg.click(722, 305), idk()
    pg.click(873, 318), idk()  # Claiming Attendance
    pg.click(847, 210), pg.click(597, 307), idk(), pg.click(818, 309), idk()  # Claiming Contribution
    pg.click(867, 24), time.sleep(1), pg.click(872, 596)
    print('Alliance Salary Complete')
def Gifts():
    time.sleep(1), pg.click(867, 592), time.sleep(0.5), pg.click(876, 550), time.sleep(1), pg.click(735, 524)
    time.sleep(0.5), pg.click(670, 729), time.sleep(1), pg.click(870, 26), time.sleep(1), pg.click(867, 592)
    print('Alliance Gifts Complete')