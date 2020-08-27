from collections import Counter

import cv2
import numpy as np
from PIL import Image
import pytesseract

kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

dir_path = "./captchas/"


def callTesseract(result, legacy=True):
    cv2.imwrite("result.jpg", result)
    if legacy:
        text = pytesseract.image_to_string(Image.open("result.jpg"),config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz --psm 7 --oem 0 --tessdata-dir ./ -l eng-leg")
    else:
        text = pytesseract.image_to_string(Image.open("result.jpg"),config="-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz --psm 7 --oem 1 --tessdata-dir ./")
    return text.strip().replace(" ", "").replace("0", "o")

def solveCaptcha(image_path):
    img = cv2.imread(dir_path+image_path)
    img = np.pad(img, ((0, 3), (3, 3), (0, 0)), mode='constant', constant_values=255)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return chooseGuess([solveCaptcha0(img),
                        solveCaptcha1(img),
                        solveCaptcha2(img),
                        solveCaptcha3(img),
                        solveCaptcha4(img),
                    ])


def chooseGuess(guess):
    five = [g for g in guess if len(g) == 5]
    if len(five) == 0:
        return ""
    c = Counter(five)
    return c.most_common(1)[0][0]

def solveCaptcha0(img):
    opening = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    opening = cv2.adaptiveThreshold(opening,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,301,133)
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel3, iterations=1)
    result = opening
    return callTesseract(result)

def solveCaptcha1(img):
    opening = solveCaptchaCrop(img)
    opening = cv2.cvtColor(opening, cv2.COLOR_BGR2GRAY)
    opening = cv2.adaptiveThreshold(opening,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,233,119)
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel3, iterations=1)
    result = opening
    return callTesseract(result)

def solveCaptcha2(img):
    opening = solveCaptchaCrop(img)
    opening = cv2.cvtColor(opening, cv2.COLOR_BGR2GRAY)
    opening = cv2.fastNlMeansDenoising(opening, None, 37, 5, 20)
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel3, iterations=1)
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel2, iterations=1)
    result = opening
    return callTesseract(result)

def solveCaptcha3(img):
    opening = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    opening = cv2.fastNlMeansDenoising(opening, None, 37, 5, 20)
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel2, iterations=1)
    edges = cv2.Canny(opening, 255, 255)
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel3, iterations=1)
    opening = opening * (edges < 64)
    result = opening
    return callTesseract(result)

def solveCaptcha4(img):
    opening = img
    opening = solveCaptchaCrop(img)    
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel3, iterations=1)
    opening = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel3, iterations=1)
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel3, iterations=1)
    opening = cv2.cvtColor(opening, cv2.COLOR_BGR2GRAY)
    # ret, opening = cv2.threshold(opening, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    result = opening
    return callTesseract(result)

def solveCaptchaCrop(img):
    opening = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    opening = cv2.adaptiveThreshold(opening,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,301,133)
    opening = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel3, iterations=1)
    
    cnts = cv2.findContours(opening, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    opening[:] = 255
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for i in range(len(cnts)):
        cnt = cnts[i]
        # hull = cv2.convexHull(cnt)
        # cnts[i] = hull
        # epsilon = 0.0005*cv2.arcLength(cnt,True)
        # approx = cv2.approxPolyDP(cnt,epsilon,True)
        # cnts[i] = approx
        area = cv2.contourArea(cnt)
        if area < 3000 and area > 10:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(opening,(x,y),(x+w,y+h),(0,0,0),-1)
    # cv2.drawContours(opening, cnts[1:], -1, (0,0,0), -1)
    opening = opening[..., np.newaxis]
    result = img | opening
    return result

