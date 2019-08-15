# Macagno Lab Software
This is a repository for all necessary software used in Macagno Lab located at UCSD(Created on 2019 August 13) Our lab focuses on collecting data via a multi-modal bio-sensing system composed of an EEG headset, eye-tracking eye wear, and an ECG monitor: 
1. __[Emotiv EPOC+](https://www.emotiv.com/epoc/) EEG headset__ 
2. __[Monocular Pupil Core](https://pupil-labs.com/products/core/) eye wear__
3. __[HeartyPatch](https://heartypatch.protocentral.com/)__ (Still in progress as of 2019 August 13)

All the data is streamed through [lab streaming layer](https://github.com/sccn/labstreaminglayer/wiki) (LSL) that allows all data points to be time synchronized in a convenient .xdf file. This __repo is accompanied by a lab manual__ that details all instructions on how to install all software and plugins.

# Dependencies
All instructions from the lab manual refers to a Windows computer, but a Mac can be used as well (although instructions for installing may be different). All sample scripts were run on the __latest version of MATLAB (2019b)__ and __Python 3.7__ (make sure you added Python 3 to your path as well!). As a UCSD student, we get a free academic license for MATLAB, which can be found __[here](https://matlab.ucsd.edu/student.html)__. Python 3.7 can be downloaded and installed from __[here](https://www.python.org/downloads/)__. We also use EEGLAB, a free MATLAB toolbox for EEG analysis, and this can be downloaded from __[here](https://sccn.ucsd.edu/eeglab/index.php)__.
