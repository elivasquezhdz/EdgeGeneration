import sys
import os
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join


def auto_canny(image, sigma=0.33):
	image = cv2.GaussianBlur(image, (3, 3), 0)
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged

def main():
	iter = 0
	sav = sys.argv[2] #Destination folder
	imgpath = sys.argv[1] #Source folder
	imgs = [f for f in listdir(imgpath) if isfile(join(imgpath, f))]

	for i in range(0,len(imgs)):
		ix = imgpath + imgs[i]
		img = cv2.imread(ix,1)
		edged = auto_canny(img)
		cv2.imwrite(sav + "e_" + str(i) + ".jpg",edged )
		iter+=1
	
	print("done with " + str(iter) + " images")

main()
