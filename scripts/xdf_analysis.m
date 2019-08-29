clear; clc
%This script will show you how to load in 
% .xdf files recorded by lab recorder. 
% Additionally, this script will show you 
% how to extract certain data from each 
% .xdf file (e.g. pupil diameter, 
% confidence, EEG, and event markers. 

%% Defining a path to your .xdf files. 

folder_name = 'sample xdf';
xdf_name = 's01_set1.xdf';

%The fullfile function will create a path name of 
% the two character strings above according to the
% way your operating system creates file paths. 
xdf_path = fullfile(folder_name, xdf_name);

%% Loading xdf file

s01_set1 = load_xdf(xdf_path);

%% Exploring Data

%When we load in our data, we see that it 
% loads in as a cell array (1 x 3). We have
% three streams so each cell corresponds to 
% each stream. How do we know which is which?
sentence = ['\nWhen we load in our %s, we see ' ...
'that it loads as a %s with %d row(s) and %d '...
'column(s). \n'];
data_type = class(s01_set1);
xdf_size = size(s01_set1);
fprintf(sentence, xdf_name, data_type, ...
    xdf_size(1), xdf_size(2))
 
%% Accessing a Cell Array
%To access this cell array, we use curly
% brackets {} next to our cell array 
% variable. Let's access our first stream of 
% our xdf file. 
disp(['When we access our first stream we see '...
    'that it is a struct with three parameters'])
s01_set1{1}

%Structs are a different data type that
% organizes data into categories. In this
% case we have three different ones:
% info, time_series, and 'time_stamps'. 

%info gives you information about a stream
% like the name, description, type of data,
% number of channels of the stream.

%time_series gives you your actual data
% with each rows representing the channels
% of your stream. The data will be a 
% regular MATLAB array. 

%time_stamps gives you the time stamps of 
% your data on the LSL time epoch. The data
% will be a regular MATLAB array. 

%To access structs by placing a period and
% the name of the field (category) of our
% first stream. We will store our data
% into the variable called time_series.
% We suppress the output with a semicolon
% because of the large number of data points!
time_series = s01_set1{1}.time_series;

%We can store our time stamp as well in a 
% variable if you like:
time_stamps = s01_set1{1}.time_stamps;

%What do these numbers mean? We can find
% more information about these numbers in
% the info field of our loaded xdf cell
% array. 

%Let's first look at what the stream name
% is. Our info field is also a struct, so 
% let's explore the first stream's info 
% field:
disp('We see the information of our first stream')
s01_set1{1}.info

%We can see a lot of information! Let's
% say we want to get the name of the 
% stream as a variable. We access like
% we do with any struct:
disp('This data is for the eye data (pupil_capture)')
stream_name = s01_set1{1}.info.name

%% Displaying all stream names: 
%We use a for-loop to display all stream names:
sentence = "Stream %d: %s (%d channel(s))\n";
fprintf("Number of Streams: %d \n", length(s01_set1))
for i = 1:length(s01_set1)
    name = s01_set1{i}.info.name;
    NumRows = size(s01_set1{i}.time_series, 1);
    fprintf(sentence, i, name, NumRows)
end
%% Seeing all channels for our data: 
%Stream 1 of this info corresponds to 
% the data from Pupil Capture as seen 
% by the the stream name (above). 

%Next we will see what each row (channels)
% are in your data (time_series). To do this,
% we will need to access the description of 
% this stream in the info field. 
s01_set1{1}.info.desc

%However, we will see that this produces 
% a struct with a field called channels. 
s01_set1{1}.info.desc.channels

%Again, we see that in the last variable is 
% a struct with a field called channel. This 
% field contains a cell with 1 row and 22 
% columns (each corresponding to each 
% channel). Therefore, we can see what 
% the first channel corresponds to: 
s01_set1{1}.info.desc.channels.channel{1}

%The first channel is eye confidence for 
% both eyes. Let's use a for-loop to display
% what each of these channels corresponds to:
sentence = "Channel %d: %s (%s)\n";
fprintf("Stream: %s \n", s01_set1{1}.info.name)
for i = 1:length(s01_set1{1}.info.desc.channels.channel)
    name = s01_set1{1}.info.desc.channels.channel{i}.label;
    unit = s01_set1{1}.info.desc.channels.channel{i}.unit;
    fprintf(sentence, i, name, unit)   
end

%We see what each row in time_series 
% corresponds to. We see our normalized
% x and y positions, as well as the calculated
% 3D diameter of our eye according to this
% software on channel 21 (mm). There is a 
% channel that gives you the diameter of 
% your eye in pixels. 

%Let's display the EEG channels as well: 

sentence = "Channel %d: %s (%s)\n";
fprintf("\nStream: %s \n", s01_set1{2}.info.name)
for i = 1:length(s01_set1{2}.info.desc.channels.channel)
    name = s01_set1{2}.info.desc.channels.channel{i}.label;
    unit = s01_set1{2}.info.desc.channels.channel{i}.unit;
    fprintf(sentence, i, name, unit)   
end

%% Storing data into variables. 
%What data do we want to store in variables
% is up to what you want to analyze. 

%Let's say we want to store our data .mat files
% This could be usefule as some of your data may
% be very large ad ay take a lot of time to load
% into MATLAB. Storing them in smaller variables 
% may be more advantageous for time's sake to analyze
% later to compare subjects. 

%Say we only want our EEG data and some Pupil Data 
% (pupil diameter in mm, pupil diameter in pixels,
% confidence, normalized x, and normalized y),
% markers, and their respective timestamps. 

%We are going to use a for-loop to store them 
% two variables: 

%initializing variables
eye_data = [];
eeg_data = [];
event_data = {};

for i = 1:length(s01_set1)
    
    if s01_set1{i}.info.name == "pupil_capture"
        %first row in time_series is confidence
        %second row in time_series is normalized
        % x coordinate
        %third row in time_series is normalized
        % y coordinate
        %19th row in time_series is 
        % pupil diameter in pixels
        % 20th row in time_series is 
        % pupil diameter in millimeters
        
        %We will make make the first row in this variable 
        % as time stamps and the relevant data (See above).
        % This is an array
        eye_data(1, :) = s01_set1{i}.time_stamps;
        eye_data = [eye_data; s01_set1{i}.time_series([1:3,19, 21],:)];
        
    elseif s01_set1{i}.info.name == "Emotiv-CyKIT"
        %We will make the first row as time stamps
        % and the next 14 rows include all 
        % 14 channel of the EMOTIV EPOC+.
        %This is an array.
        eeg_data = s01_set1{i}.time_stamps;
        eeg_data = [eeg_data; s01_set1{i}.time_series];
            
    elseif s01_set1{i}.info.name == "TestMarkerStream"
        %This data is a cell array because the data 
        % are character arrays (strings). 
        event_data = num2cell(s01_set1{i}.time_stamps);
        event_data = [event_data;...
            s01_set1{i}.time_series];
    end
    
end