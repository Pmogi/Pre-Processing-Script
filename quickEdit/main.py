# Patrick Mogianesi REU Summer Student 2017
# July 12 - 20, 2017
# Python 3.X required & virtualdub software
# Unfortunatly becuase of the virtualdub software, this will only work on windows

# video pre-processing
# this initial script has a user input to find the .avi file of interest
# this file path is then passed off to a virtualdub and uses a .jobs script (the script for virtualdub) to fix up the video according to some settings

#importing libraries
from tkinter import filedialog # gets file information w/ gui like matlab
from tkinter import *
import os # for command line actions

# initalizing Tk object
guiObj = Tk()
# get path to file using graphic interface
# source for more information
# https://pythonspot.com/en/tk-file-dialogs/
guiObj.file = filedialog.askopenfilename(initialdir = "C:\\Users\ktichauer\Desktop" , title = "Select AVI File To Process", filetypes = [("AVI files", "*.avi")]) #similar gui to file picking with matlab, if different pc, switch to ur desktop
programLocation = "\"C:\\Users\ktichauer\Desktop\quickEdit\movie2edit.avi\"" # if different pc change to quickEdit location and save as movie2edit
selectedVideo = guiObj.file # picking a more friendly variable for the file pathname
print(selectedVideo)
print(programLocation)


# change forward slashes to black slashes so cmd can use the path
selectedVideo = list(selectedVideo)
for i in range(0,len(selectedVideo)): # for-loop through the lenth of the filepath
    if selectedVideo[i] == '/':
        selectedVideo[i] = '\\'
selectedVideo = ''.join(selectedVideo) # after changing the forward slashes to back slashes, make the list into a string again
print(selectedVideo)


# this function gets the name of the video
def getVideoName(videoList):
    i = (len(videoList)-5)
    fileName = [] # this list will hold the filename
    while videoList[i] != "\\": #loop until it hits the directory slash
        fileName.append(videoList[i])
        i = i - 1
    fileName = fileName[::-1] # reverse the list, because the method above actually messes up the title lol
    for i in range(0, len(fileName)):
        if fileName[i] == " ":
            fileName[i] = "_" # this makes sure there are no spaces in the file's name, spaces gave me a lot of grief when renaming the edited file
    
    fileName = ''.join(fileName) # this list filename to a string
    fileName = fileName + "_edited.avi" # change original filename to indicate this is the edited file
    return fileName # returns the string of the filename
# use the function defined above
fileName = getVideoName(selectedVideo)
print(fileName)


selectedVideo = "\"" + selectedVideo + "\"" # make sure the file has "" around the path, if there are spaces and no apostrophes, cmd cannot read that as a path


# test to see filepath
print ("Filepath: " + selectedVideo)
print ("copy " + " " + selectedVideo + " " + programLocation)
print("Copying files please wait...")
os.system("copy " + " " + selectedVideo + " " + programLocation) # this will move the selected movie to quickEdit renaming it to movie2edit.avi so I have a common name to use in the virtualdub script

def pass2VirtualDub():
    response = input("Are you fixing Rat Data? y or n > ")
    if response == "y":
        os.system(".\\vdub.exe /i fixerScript.jobs movie2edit.avi editedMovie.avi") # pass video to virtualdub using rat data 'fixerScript' reanme video as editedMovie

    elif response == "n": # if it isn't rat data, it probably just needs to be resized to 256x256
        os.system(".\\vdub.exe /i fixerScriptNotRat.jobs movie2edit.avi editedMovie.avi") # pass video to virtualdub using non-rat data 'fixerScript'

    else:
        print("That is not a valid input.")
        pass2VirtualDub() # send user back to start of function and make a valid

# use function defined above
pass2VirtualDub()

os.system('del /f movie2edit.avi') # delete the movie2edit .avi file, it's redundant now that the video has been fixed up in virtualDub

# rename the file as the original name with _edited at the end
os.system('rename' + " " + "editedMovie.avi" + " " + fileName)
