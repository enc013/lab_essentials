"""Example program to demonstrate how to send string-valued markers into LSL."""

import random
import time

from pylsl import StreamInfo, StreamOutlet

# first create a new stream info (here we set the name to MyMarkerStream,
# the content-type to Markers, 1 channel, irregular sampling rate,
# and string-valued data) The last value would be the locally unique
# identifier for the stream as far as available, e.g.
# program-scriptname-subjectnumber (you could also omit it but interrupted
# connections wouldn't auto-recover). The important part is that the
# content-type is set to 'Markers', because then other programs will know how
#  to interpret the content

#Defining variables to define stream information 
stream_name = 'MyMarkerStream'
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

print("now sending markers...")
# Defining the marker strings
markernames = ['Test', 'Blah', 'Marker',
               'XXX', 'Testtest', 'Test-1-2-3']

#Infinte while loop
while True:
    # pick a sample to send an wait for a bit
    # The function random.choice() picks one of the
    # markers at random from the markernames list.
    # Please note that we push an event marker
    # as a list.
    outlet.push_sample([random.choice(markernames)])
    #We then wait for a random time interval from
    # 1 to 3 seconds. The random.random()function
    # randomly picks a number from 0 to 1. This
    # number is then multiplied by 3. We use time.sleep
    # to wait for that specified time.
    time.sleep(random.random()*3)
