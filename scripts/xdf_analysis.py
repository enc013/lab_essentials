#Importing all necessary packages for our script
# We use pyxdf to load in our xdf files:
import numpy as np
import pandas as pd
import pyxdf
import os

#We define the the path to the xdf file, which is
# in a a local folder called "sample xdf":
folder_name = 'sample xdf'
file_name = 's01_set1.xdf'

#We use the function os.path.join to make a path
# for your operating system to read
xdf_path = os.path.join(folder_name, file_name)

#Loading xdf file using load xdf: 
streams, header = pyxdf.load_xdf(xdf_path)

#We see that when we load our xdf files,
# we get a list.
sentence1 = "When we load our xdf file, we get a {}".format(type(streams))
sentence2 = "There are {} items in this list. \n".format(len(streams))
print(sentence1)
print(sentence2)

#Each of these items represent an LSL stream.

#We access these streams (this list) with square 
# brackets. We can store all our streams into 
# variables stream1, stream2, stream3:
stream1 = streams[0]
stream2 = streams[1]
stream3 = streams[2]

#When you access these streams, we will see that 
# these are dictionaries with three keys: info,
# footer, time_series, and time_stamps. 

sentence1 = "Each of our streams are {}".format(type(stream1))
sentence2 = "The following keys are present in each stream:"
i = 1

print(sentence1)
print(sentence2)
for key, value in streams[0].items():
    print("{}. {}".format(i, key))
    i += 1

#Dictionaries are a different type of data
# that organizes data into categories (keys)
# As we have seen we have three keys: 
    
#To access dictionaries, we use brackets and in that
# bracket, we pass the keys as a string variable. 
# For instance, when we want to access the time_series
# key, we can access the first streams time_series with 
# the following command: 
# streams[0]['time_series']
# We can access our info key with the following: 
# streams[0]['info']
# You can probably infer how to access our 
# time_stamps key.
    
# info gives you information about a stream
#like the name, channel descriptions, type of data,
#and number of streams of the stream. 
    
#time_series gives you your actual data
# with each rows representing the channels.
# This is a numpy array.

#time_stamps gives you the timestamps of 
# each of your data points. This is a 
# numpy array.
    
# We can store our data (time_series) into 
#a variable. We can also store our 
#timestamps for our data: 
# first stream
time_series1 = streams[0]['time_series']
#second stream
time_series2 = streams[1]['time_series']
#third stream
time_series3 = streams[2]['time_series']

#time stamps:
time_stamps1 = streams[0]['time_stamps']
time_stamps2 = streams[1]['time_stamps']
time_stamps3 = streams[2]['time_stamps']
    
#Let's take a look at the dimensions of these
# numpy arrays for each stream. We can use the 
# function .shape on the numpy array to find the
# number of rows and columns. The number of rows
# tell us how many data points were taken, and 
# the number of columns tell us how many channels. 
# However, with markers, we have string data types,
# so the time_series for our markers, will be a 
# list: 
i = 1
print('\n')
sentence1 = "Stream {} has {} data points and {} channels." 
sentence2 = "Stream {} has {} data points with 1 channel."
for stream in streams: 
    if isinstance(stream['time_series'], list):
        print(sentence2.format(i, len(stream['time_series'])))
    else:
        num_rows, num_cols = stream['time_series'].shape
        print(sentence1.format(i, num_rows, num_cols))
    
    i += 1
#    num_row, num_col = stream['time_series'].shape
#    print(sentence1.format(i, num_row, num_col))

# What kind of info do we have for our first 
# stream: 
sentence1 = '\nOur info field for our first stream has the following keys present:'
i = 1
print(sentence1)
for key, value in streams[0]['info'].items():
    print("{}. {}".format(i, key))
    i += 1
    
# What is the name of this first stream?
#Let's first look what type of data type it 
#is. Our last variable, streams[0]['info']
#is a dictionary. As shown in the last bit of 
#code, we have several keys. One of them is a 
#key called name. Let's see what type of 
# data this is: 
sentence1 = "\nWhen we access our name key through the command streams[0]['info']['name']"
sentence2 = "We find that it is a {} data type".format(type(streams[0]['info']['name']))

print(sentence1)
print(sentence2)

# We will find that there is one item in this list,
#accessing the name of our stream: 
sentence1 = "\nThe name of the first stream is {}."
stream_name = streams[0]['info']['name'][0]
print(sentence1.format(stream_name))

#We know how to access the name of our stream, so 
# let's display all our stream names: 
sentence1 = "\nOur streams have the following names:"
sentence2 = "Stream {}: {}"
i = 1
print(sentence1)
for stream in streams:
    stream_name = stream['info']['name'][0]
    print(sentence2.format(i, stream_name))
    i += 1
    
#We have seen that we can access our data (time_series)
# and the name of our streams. However, we don't know 
# what the data corresponds to. What do the columns
# (channels) in time_series represent? 

# Accessing our channel information is complex, with
# nested lists and dictionaries. Refer to python 
# documentation on lists and dictionaries

#To do this we have to access the 'desc' key of our 'info'
# dictionary. Inside the 'desc' key, we have a list with one 
# item. In that list, we have a dictionary with one key called
# 'channels'. Accessing the 'channels' key, we see a list with 
# one item. When we access this list, we see a dictionary with
# one key called 'channel'. In this key (channel), we see 
# a list full of the information of our channels. When we 
# access the list, we see a dictionary with many keys such as
# our channel label, type of data, and unit of our data channel
# In these dictionary keys, we see lists with one item. 
# Therefore, we can access channel information: 
sentence1 = "\nStream 1 has the following channel information: "
sentence2 = "{}. {}"
i = 1
print(sentence1)
for key, value in streams[0]['info']['desc'][0]['channels'][0]['channel'][0].items():
    print(sentence2.format(i, key))
    i += 1
    
#Let's look through each stream and find their channel 
# and the units the channels are in. However, for our 
# event markers, we see that we only have one channel
# that has a list of strings, so it does not have
# have channel information. You will get an error
# if you try to access the event marker stream channel information. 
# We don't know which stream is our event markeres, so we have to 
# find this stream with information that is common for markers
# (e.g. the type of stream it is is 'Marker') to 
# differentiate it from other streams (you can use
# the stream name to differentiate).
    
#Let's write code that will show you what each 
# channel represents: 
sentence1 = "Stream {}: {}"
sentence2 = "Channel {}: {} ({})"
print('\n')
for stream, i in zip(streams, range(1,len(streams))):
    stream_name = stream['info']['name']
    if stream['info']['type'][0] != 'Markers':
        print(sentence1.format(i, stream_name))
        for channel, j in zip(stream['info']['desc'][0]['channels'][0]['channel'],
                              range(1, len(stream['info']['desc'][0]['channels'][0]['channel']) + 1)):
            channel_name = channel['label'][0]
            channel_unit = channel['unit'][0]
            print(sentence2.format(j, channel_name, channel_unit))
            
        print('\n')

#We have now seen what these channels represent. Please refer 
# to Pupil Labs documentations (data format) on what this 
# data refers to. The channels for the EMOTIV EPOC+ 
# should look familiar as they are the 14 eeg node names. 

#Let's say we want to extract data into separate variables 
# that can be stored later as csv files. This may be 
# advantageous if our xdf file is very large, making 
# loading time very large. Let's store EEG and 
# certain channels of our pupil_capture stream 
# into variables. Let's use a for loop: 
for stream in streams:
    if stream['info']['name'][0] == 'pupil_capture':
        #first column represents confidence
        #second column represents normalized x
        #third column represents normalized y
        #19th column represents pupil diameter in pixels
        #21st column represents pupil diameter in mm
        
        #extracting the number of rows in time_stamps
        num_rows = stream['time_stamps'].shape[0]
        #we reshape it to have 1 column
        eye_time_stamps = stream['time_stamps'].reshape(num_rows,1)
        #extacting certain gaze data (look above)
        gaze_data = stream['time_series'][:, [0,1,2,18,20]]
        #appending numpy arrays with the first column as time_stamps
        eye_data = np.append(eye_time_stamps, gaze_data, 1)
        
    if stream['info']['name'][0] == 'Emotiv-CyKIT':
        num_rows = stream['time_stamps'].shape[0]
        eeg_time_stamps = stream['time_stamps'].reshape(num_rows,1)
        channel_data = stream['time_series']
        eeg_data = np.append(eeg_time_stamps, channel_data, 1)

# In this data, we will have the first column be our time
# stamps for our data points, while the rest of the columns
# is the extracted data: 
sentence1 = "\nOur eye data numpy array has {} rows and {} columns"
sentence2 = "Our EEG data numpy array has {} rows and {} columns \n"
num_rows_eye, num_cols_eye = eye_data.shape
num_rows_eeg, num_cols_eeg = eeg_data.shape
print(sentence1.format(num_rows_eye, num_cols_eye))
print(sentence2.format(num_rows_eeg, num_cols_eeg))
#Let's say we want to get the first 100 points of 
# the first stream. However, what if I want the 
# confidence (channel 1), normalized x (channel 2),
# normalized y (channel 3), right pupil diameter in pixels
# (channel 19), and right pupil diameter in mm (channel 21)
stream1_100_datapoints = streams[0]['time_series'][:100, [0,1,2,18,20]]

#Let's verify that the dimensions of our new extracted numpy
# array. We should have an numpy array with 100 rows (data points)
# and 5 columns (our extracted channels))

sentence1 = "Our extracted numpy array has {} data points and {} channel(s)"
num_rows, num_cols = stream1_100_datapoints.shape
print(sentence1.format(num_rows, num_cols))