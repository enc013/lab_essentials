% instantiate the library
disp('Loading library...');
lib = lsl_loadlib();

% make a new stream outlet
% the name (here MyMarkerStream) is visible to the experimenter and should be chosen so that 
% it is clearly recognizable as your MATLAB software's marker stream
% The content-type should be Markers by convention, and the next three arguments indicate the 
% data format (1 channel, irregular rate, string-formatted).
% The so-called source id is an optional string that allows for uniquely identifying your 
% marker stream across re-starts (or crashes) of your script (i.e., after a crash of your script 
% other programs could continue to record from the stream with only a minor interruption).

%Defining LSL info variables:
%This variable will be shown as the stream name
%in Lab Recorder
stream_name = 'MyMarkerStream';
stream_type = 'Markers';
number_of_channels = 1;
sampling_rate = 0;
data_type = 'cf_string';
unique_id = 'myuniquesourceid23443';

disp('Creating a new marker stream info...');

% Defining LSL meta-information
info = lsl_streaminfo(lib,stream_name,stream_type,...
    number_of_channels, sampling_rate,...
    data_type,unique_id);

% Opening the LSL outlet
disp('Opening an outlet...');
outlet = lsl_outlet(info);

%Defining markers
markers = {'Test', 'Blah', 'Marker', 'XXX', 'Testtest', 'Test-1-2-3'};

% send markers into the outlet
disp('Now transmitting data...');

% This is an infinite loop
while true
    % The loop will pause from a time of 0 to 3 seconds. This is 
    % determined by the function rand() that chooses a number
    % between 0 and 1 which is multiplied by 3. 
    pause(rand()*3);
    
    % This is a way to randomly pick a marker from the markers cell array
    % defined above. It does this by using the function min() to get the 
    % minimum number between two numbers. These two numbers are the 
    % length of the marker cell array (which is 6) and a number between
    % 0 to 6.
    mrk = markers{min(length(markers), 1+floor(rand()*(length(markers))))};
    disp(['now sending ' mrk]);
    % Note that the string is wrapped into a cell-array
    % Pushing a marker to the network.
    outlet.push_sample({mrk});   
end
