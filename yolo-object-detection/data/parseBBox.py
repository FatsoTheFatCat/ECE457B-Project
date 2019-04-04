from __future__ import division
import numpy as np
import cv2
import csv
import glob, os

# delete all text files for a clean directory
for txts in glob.glob("dayTraining/*.txt"):
        os.remove(txts)

# parse the bounding boxes
with open('frameAnnotationsBOX.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=';')
	line_count = 0
	for row in csv_reader:
		# first line consists of headers
		if (line_count > 0):
			# expects that the csv will have columns in the expected order
			name, ext = os.path.splitext(row[0])
			
                        # get image size
                        # img = cv2.imread(os.path.join(os.getcwd(), row[0]))
                        ab_path = os.path.realpath("{}.jpg".format(name))
                        img = cv2.imread(ab_path)
                        width, height, channels = img.shape

			# write to the filename
			bbox_file = open("{}.txt".format(name), 'a+')

			# upper left x
			# upper left y
			# lower right corner x
			# lower right corner y

			# tags are labels
			tag = row[1]

			# bounding box
			up_left_x = int(row[2])
			up_left_y = int(row[3])
			low_right_x = int(row[4])
			low_right_y = int(row[5])

			# reformat bbox to [object center in X] [object center in Y] [object width in X] [object width in Y]
			center_x = (low_right_x + up_left_x) / (2 * width)
			center_y = (low_right_y + up_left_y) / (2 * height)
			width = (low_right_x - up_left_x) / width
			height = (low_right_y - up_left_y) / height

			# write to the file
			bbox_file.write("0 {} {} {} {}\n".format(center_x, center_y, width, height))
			bbox_file.close()

		line_count += 1

# create any missing text files
for jpg in glob.glob("dayTraining/*.jpg"):
	name, ext = os.path.splitext(jpg)
	if not (glob.glob("{}.txt".format(name))):
		txt = open("{}.txt".format(name), 'w')
		txt.close()
