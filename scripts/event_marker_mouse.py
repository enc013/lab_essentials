#Importing packages
from pynput.mouse import Listener
import logging
from pylsl import StreamInfo, StreamOutlet

#Establishing Event Marker Stream:

stream_name = 'mouse_clicks'
info = StreamInfo(stream_name, 'Markers',
                  1, 0, 'string',
                  'evt_mark_id1')

#Creating an LSL Outlet:
outlet = StreamOutlet(info)

#Letting you know that an stream is established:
#You should open up lab recorder to make sure that
#it is established!
print('Now Sending Markers!')
print('Check Lab Recorder to see your stream named {}'
      .format(stream_name))
input('Press Enter to Continue...')

print('Now we can record events with your mouse')

#We define a variable to keep track of your events
i = 1

#Defining a function to record clicks
# and pushing an event marker. 
def on_click(x, y, button, pressed):
    if pressed:
        global i
        outlet.push_sample(['event_{0}'.format(i)])
        print('event_{0} has been logged.'.format(i))
        i += 1
        
# recording clicks:
with Listener(on_click = on_click) as listener:
    listener.join()
