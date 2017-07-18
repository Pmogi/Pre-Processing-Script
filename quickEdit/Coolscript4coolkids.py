# Patrick Mogianesi REU Summer Student 2017
# 7/12/17
# Python 3.X required & virtualdub software
# Unfortunatly becuase of the virtualdub software, this will only work on windows

# video pre-processing
# this initial script has a user input to find the .avi file of interest
# this file path is then passed off to a virtualdub and uses a .jobs script (the script for virtualdub) to fix up the video according to some settings

#importing libraries
from tkinter import filedialog # gets file information w/ gui like matlab
from tkinter import *
import os # for command line actions
import time # just in case I need pauses

# initalizing Tk object
guiObj = Tk()
# get path to file using graphic interface
# source for more information
# https://pythonspot.com/en/tk-file-dialogs/
guiObj.file = filedialog.askopenfilename(initialdir = "C:\\Users\ktichauer\Desktop" , title = "Select AVI File To Process", filetypes = [("AVI files", "*.avi")]) #similar gui to file picking with matlab
programLocation = "\"C:\\Users\ktichauer\Desktop\quickEdit\movie2edit.avi\""

selectedVideo = guiObj.file
print(programLocation)
print(selectedVideo)

# change forward slashes to black slashes so cmd can use the path
selectedVideo = list(selectedVideo)
for i in range(0,len(selectedVideo)):
    if selectedVideo[i] == '/':
        selectedVideo[i] = '\\'
selectedVideo = ''.join(selectedVideo)
print(selectedVideo)
selectedVideo = "\"" + selectedVideo + "\"" # make sure the file has "" around the path, if there are spaces and no apostrophes, cmd cannot read that as a path
# test to see filepath
print ("Filepath: " + selectedVideo)
print ("copy " + " " +selectedVideo + " " + programLocation)
os.system("copy " + " " + selectedVideo + " " + programLocation) # this will move the selected movie to quickEdit renaming it to movie2edit.avi so I have a common name to use in the virtualdub script
os.system(".\\vdub.exe /i fixerScript.jobs movie2edit.avi MovieSaveHere\editedMovie.avi") # use virtualDub to cut down and resize the video
os.sytem('del /f movie2edit.avi') # delete the movie2edit, it's redundant now that the video has been fixed up in virtualDub
