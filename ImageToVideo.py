# Encoding - UINT 8
# Copyright from Sharebee.cn Inc, All rights reserved.
# Author: Samuel
# Date: July 4, 2021
# Reference: https://blog.csdn.net/haiziccc/article/details/101675468

import os
import cv2
file_dir='/home/workspace/BatteryAccessories/JPGImages/'
list=[]
for root, dirs, files in os.walk(file_dir):
	for file in files:
		list.append(file)  # get the image in the path

# define save path and name of video
video=cv2.VideoWriter('/home/workspace/BatteryAccessories/BatteryAccessories.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, (608, 546))
for i in range(1, len(list)):
	img=cv2.imread('/home/workspace/BatteryAccessories/JPGImages/' + list[i-1])
	img=cv2.resize(img, (608, 546))  # resize image to 608*416
	video.write(img)  # make image write into video

video.release()