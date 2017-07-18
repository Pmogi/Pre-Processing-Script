########################################
quickEdit
Patrick Mogianesi
pmogiane@ucsc.edu


Purpose:
A script to process videos to be readable by dicg motion-correction software.

video -> program -> edited video ready for motion correction

Required Software:
- Python 3.X
- VirtualDub Video editor
- .jobs file that contains the script for vdub processs
- Windows computer*

Optional:
DubMan, a handy tool that creates scripts for VirtualDub for batch processes. Beats having to tussle with
the awful Vdub scripting language.

**main.py starts the program**

*warning* If files get moved around/filenames change, you may need to change some Paths in the python/vdub script.
Most of this script is honestly me moving things around through accessing the windows commandline through python. SO
you'll have to change the path's if you try using this on a different pc or move files around.

For the rat data videos, there are a lot of unneccesary frames; so I opted to decimate 99 frames for every frame.
Through some experimentation, I did find that I can decimate as little as 50 frames and still have it load into
the motion-correction software. I'm still not sure the specific requirements for file size for the files to be
function properly in the program, but the max file-size that seemed to work through experimentation is ~60 MB.
The Dubman script can be adjusted accordingly to the rate of decimation.

*details are in python script