#Importing all necessary packages:
import os
import cv2
import pyautogui
import numpy as np
from pylsl import StreamInfo, StreamOutlet

#Defining variables to define stream information 
stream_name = 'picture_display_stream'
stream_type = 'Markers'
number_of_channels = 1

#A value of 0 is made for the sampling rate
# to signify an irregular sampling rate
sampling_rate = 0
data_type = 'string'
unique_id = 'myuidw43536'

#Defining the stream
info = StreamInfo(stream_name, stream_type,
                  number_of_channels,
                  sampling_rate,
                  data_type, unique_id)

# next make an outlet
outlet = StreamOutlet(info)

#A prompt to start Lab Recorder
print("Your stream is now on the network!")
print("Start Lab Recorder and hit record.")
input("Press Enter to Continue")

#Defining the folder name that contains
# all our images we want to display.
folder_name = "images"

#Getting the complete path to our
# image folder.
folder_path = os.path.join(os.getcwd(),
                   folder_name)

#We get all the names of our images:
image_names = os.listdir(folder_path)

#We only want to import image files
# with valid extension (like .jpg,
# .jpeg, .png), so we create a
# list with the file extensions
# we only want.
valid_image_ext = ['.jpg', '.jpeg',
                   '.gif', '.png']

#Next we get the path to all our
# images in the folder by
# using a for loop that only extracts
# the full path with the extensions
# defined by valid_image_ext.
image_paths = [os.path.join(folder_path, image)
               for image in image_names
               if os.path.splitext(image)[1].lower()
               in valid_image_ext]

#Finding the screen resolution of monitor:
width, height = pyautogui.size()

#Defining a black screen, white screen, and initializing
# gray pre-image.
black_image = np.zeros((height,width))
white_image = np.zeros((height,width)) + 255

#A counter to help us
i = 1

for path in image_paths:

    #Loading an image in
    img = cv2.imread(path, 1)

    #Setting window name:
    cv2.namedWindow('Picture', cv2.WINDOW_NORMAL)

    #Setting Window to fullscreen:
    cv2.setWindowProperty('Picture', cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)

    #Before the First Picture is displayed, a black image and a
    # white image will displayed for 5 seconds:
    if i == 1:
        #LSL outlet to push an event marker when a
        # black image is shown
        outlet.push_sample(['black_image'])
        cv2.imshow('Picture', black_image)
        key = cv2.waitKey(5000)

        #LSL outlet to push an event marker when a
        # white image is shown
        outlet.push_sample(['white_image'])
        cv2.imshow('Picture', white_image)
        key = cv2.waitKey(5000)

    #Displaying our image for 5 seconds:
    # Here we are pushing the name of the image as a
    # string event marker!
    outlet.push_sample([image_names[i-1]])
    cv2.imshow('Picture', img)
    key = cv2.waitKey(5000)

    #At the end of the experiment, all windows will close
    if key == 27 or i == len(image_paths):
        #Display the black image for 5 seconds
        outlet.push_sample(['black_image'])
        cv2.imshow('Picture', black_image)
        key = cv2.waitKey(5000)

        #Display white image for 5 seconds
        outlet.push_sample(['white_image'])
        cv2.imshow('Picture', white_image)
        key = cv2.waitKey(5000)

        #Close all windows
        cv2.destroyAllWindows()

    #Incrementing our counter
    i += 1

#A prompt to stop Lab Recorder
print('\n Your experiment has stopped!')
print('Please stop Lab Recorder.')
input('Press Enter to Continue...')
