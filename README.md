#QuickRip#

A utility for ripping dvds with MakeMKV.  

First discs are loaded into a queue stored in a SQLITE database using the queue utility.  We can execute the queue utility every time a new disc is loaded on the computer.

Next the rip utility reads the SQLITE database and converts the disc to a MKV file onto the hard drive.

This approach allows us to have multiple dvd drives accessible on the same machine.

##Install##

1) Install MakeMKV
2) Install imdbpy


##Configuration##
###Queue.py###
####OS X####
1) From the Mac OS X Finder, choose Apple menu > System Preferences.
2) Click CDs & DVDs.
3) Under DVD, choose Open other Application.
4) Set the application to queue.py


####Windows####
Todo:

###Quick_Rip.py###
1) Open Quick_Rip.py in a python or text editor
2) Set the minumum_length. The minimum length value represents the minimum length of a video in minutes to copy to the system.  22 is a good choice for tv shows
3) Set the output_path.  This workspace folder on the machine that the user has read and write access into.



##Usage##

Todo:
