import cv2 as cv
# from scipy.spatial.distance import euclidean
# import math
import numpy as np
import matplotlib.pyplot as plt
import requests

def show_img(window_name, img, adjust=False):
    """3 arguments: window name, source images, boolean to adjust to screen size"""
    if adjust:
        cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    else:
        cv.namedWindow(window_name)

    cv.imshow(window_name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def plt_img(img, title=None):
    """2 Args:
    img: source image
    title: optional string"""
    if len(img.shape)==3:
        plt.imshow(img)
    elif len(img.shape)==2:
        plt.imshow(img, cmap=plt.cm.gray)
    else:
        raise Exception('Incorrect image dimension')
        
    if title is not None:
        plt.title(title)
        
    plt.xticks([]), plt.yticks([])

def download_img_url(fn, url):
    """2 args:
    fn: filename
    url: image address"""
    with open(fn, 'wb') as f:
        f.write(requests.get(url).content)
