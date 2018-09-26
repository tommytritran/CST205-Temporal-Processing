'''
Author: Tommy Tran - tran7794
Partner: Will Carrara
Date: 2018-Sept-26
Task: Homework2
Exercise: Can you process a series of images using temporal processing to remove an unwanted element in the series?
Course: CST205
'''
from PIL import Image
import glob
import math

#Opens images directory and saves all files with the .png extension into an string array "images/1.png" etc..
im_string_array = glob.glob("images/*.png")

#Instansiating an empty array to hold all the images objects
im_obj_array = []

#Iterates through all string values from the string array and creates an images object and appends it into the im_obj_array
for im in im_string_array:
	img = Image.open(im)
	im_obj_array.append(img)

#Extract the width and size for the new canvas
width,height = im_obj_array[0].size

#Creates new white canvas with sie of the source images
new_img = Image.new("RGB", (width,height),(255,255,255))

#Arrays to hold all the values for each pixel, used to find median
red_array = []
green_array = []
blue_array = []

#Iterates through the width and height of the image
for x in range(width):
	for y in range(height):
		#iterates through all the images
		for z in range(len(im_obj_array)):
			#get the color tuple at current coordinate x,y
			curr_img = im_obj_array[z].getpixel((x,y))
			#extract the red value at current coordinate
			red = curr_img[0]
			red_array.append(red)
			#extract the geen value at current coordinate
			green = curr_img[1]
			green_array.append(green)
			#extract the blue value at current coordinate
			blue = curr_img[2]
			blue_array.append(blue)
		#Sorts all the arrays
		red_array.sort()
		green_array.sort()
		blue_array.sort()
		#Calculates the median for each array that is now sorted
		red_median = math.floor(len(red_array)/2)
		green_median = math.floor(len(green_array)/2)
		blue_median = math.floor(len(blue_array)/2)
		#Gets the median color value from each array and creates new color tuple with median value and appends to the new canvas
		new_img.putpixel((x,y),(red_array[red_median],green_array[green_median],blue_array[blue_median]))
		#Resets the rgb array
		red_array = []
		green_array = []
		blue_array = []

new_img.show()



			

