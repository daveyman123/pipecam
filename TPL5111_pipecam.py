#!/usr/bin/env

# This is the main pipecam software for the TPL5111 PipcCam
import os
from time import gmtime, strftime
import RPi.GPIO as GPIO

# Set up the GPIO
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD
GPIO.setup(17, GPIO.OUT)           # set GPIO24 as an output
# Set up a 'done' flag
done = 0

################################################################################################################################
def takePhoto(path):
	# Here we handle taking a photo
	timestamp =  strftime("%d-%m-%YH%H%M%S", gmtime())
	extention = ".jpg"
	# Set the output file path
	file_name = path + timestamp + extention

	#Try take the actual photo
	try:
		cmd = "raspistill -hf -vf -ex beach -o %s" % file_name
		os.system(cmd)
		global done = 1
	except:
		global done = 0
		print "\033[31m Error! could not take video\033[0m"

################################################################################################################################

def takeVideo(path):
	# # Here we handle taking a photo
	# timestamp =  strftime("%d-%m-%YH%H%M%S", gmtime())
	# extention = ".h264"
	# file_name = path + timestamp + extention
	# # Settings https://www.npmjs.com/package/raspivid
	# w = '-w 1920'		  			# -w, --width     			: Set image width <size>. Default 1920
	# h = '-h 1080' 					# -h, --height    			: Set image height <size>. Default 1080
	# ex = ''							# -ex, --exposure 			: Set exposure mode options: auto,night,nightpreview,backlight,spotlight,sports,snow,beach,verylong,fixedfps,antishake,fireworks
	# t = '-t 900000' 				# -t, --timeout  		 	: Time (in ms) to capture for. If not specified, set to 5s. Zero to disable
	# fps = '' 						# -fps, --framerate       	: Specify the frames per second to record
	#
	# try:
	# 	cmd = "raspivid %s -vf %s %s %s -o %s.h264 " %(t,ex,w,h,file_name)
	# 	os.system(cmd)
	#   global done = 1
	# except:
	# 	global done = 0
	# 	print "\033[31m Error! could not take video\033[0m"
	print "\033[31m Error! Video code not enabled. No action taken. \033[0m"

################################################################################################################################

def powerOff():
	# What to do when powering down
	# This is an ugly, ugly way of doing it and may cause SD card errors in the long run.
	print "\033[34mDone\033[0m"
	GPIO.output(24, 1)

################################################################################################################################


if __name__ == "__main__":
    # Some UI and output
    # Nice little headertjie
	print '\033[37m                                                  \033[0m'
	print '\033[37m                .:oyhdddddddhyo/-                 \033[0m'
	print '\033[37m            `/ymho/-`       `.:+ymh+.             \033[0m'
	print '\033[37m          -yms:            `-     -odd/           \033[0m'
	print '\033[37m        -hm+`            -sNMmo.     :hm/         \033[0m'
	print '\033[37m       oN+`             :Ms:::dN`      :mh.       \033[0m'
	print '\033[37m     `hm-                yNdddM/        `yN-      \033[0m'
	print '\033[37m     hm.                 sN. :M:          sN-     \033[0m'
	print '\033[37m    oN-                 `mh  `Ny          `dd`    \033[0m'
	print '\033[37m   `Ns                  :M/   sN`          :M/    \033[0m'
	print '\033[37m   /M:                  yN    -M/           Nh    \033[0m'
	print '\033[37m   +M`                 `Ns     mh           dd    \033[0m'
	print '\033[37m   /M-   `ddmNmdddNNdddNMMNMMMMMM.          mh    \033[0m'
	print '\033[37m   .Mo      .Ny  /M:   hMMMMMMMMMo         .M+    \033[0m'
	print '\033[37m    yN`      /M/.Ns   .MMMMMMMMMMm         yN`    \033[0m'
	print '\033[37m    `mh       yNdm`   oMMMMMMMMMMM-       /M/     \033[0m'
	print '\033[37m     -my`     `mM-    mMMMMMMMMMMMs      +N+      \033[0m'
	print '\033[37m      .dNNNNNNNMMNNNNNMMMMMMMMMMMMMNNNNNNN/       \033[0m'
	print '\033[37m        +NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy`        \033[0m'
	print '\033[37m         `+mMMMMMMMMMMMMMMMMMMMMMMMMMNy-          \033[0m'
	print '\033[37m            :smMMMMMMMMMMMMMMMMMMMNh/`            \033[0m'
	print '\033[37m               ./shmMMMMMMMMMNdy+-`               \033[0m'
	print '\033[37m                     `..-..`                      \033[0m'
	print '\033[37m                                                  \033[0m'
	print "\033[34m__________________________________________________\033[0m"
	print ""
	print "\033[34m TPL5111 Pipecam base script\033[0m"
	print ""
    #End of nice little headertjie

	# Start here
	# Set the mode of the pipecam. 0 for photos, 1 for videos
	mode = 0

	# Set the home path where files are stored onboard
	path = "/home/pi"

	# Get the time for some feedback
	timestamp =  strftime("%d-%m-%YH%H%M%S", gmtime())

	# Now lets take some video/photos
	if mode == 0:
		print "\033[34m%s: taking photo on %s\033[0m" % (timestamp,path)
		takePhoto(path)
	else:
		print "\033[34m%s: taking video %s\033[0m" % (timestamp,path)
		takeVideo(path)

	# Power down if successfull
	if done == 1:
		powerOff()

################################################################################################################################
