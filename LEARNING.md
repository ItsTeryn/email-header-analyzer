# Learning notes. Creating an email header analyzer.

# This is my notepad of things I learned while creating this project. 
##
- I built a Kali Linux VM in Virtualbox. One of the issues I've ran into was that the ISO I had from previous labs last year went bad. I was unable to update it, so I went and pulled the image from the site that came pre-loaded with credentials for me to use instead of building it from scratch.
- I learned how to set up python in the VM using .venv and learned the importance of creating a requirements.txt file. 
- I did some digging and learned about how to create a parser with python's built in email module. I use this to pull the header fields. 
- During the build I ran into an error from here, I learned how to read errors in python and how to troubleshoot. This was a NameError from a typo that I did. 
- Learned how to create my first project on GitHub using the GitHub CLI interface. 

##
- Most of the work was completed on my laptop running a Kali VM. I have a gaming PC that I've done some work with this project using GitBash. 
- First thing I learned was how to pull the project from GitHub using GitBash so I could continue work without having to break out my laptop. 
- One thing to note from working on my gaming PC, is that when I tried to run the pip.exe, my antivirus flagged it as malicious. I created a little write up with screenshots showing the pop up and the logs. (I need to save it to my laptop so I can keep it all together.)

##
- I created the hops.py file to trace the servers the email passes through from start to finish. 
- I learned that using regular expression (re) can pull server names and IPs. 
- I learned while creating the hops.py, that the Recieved Lines stack with the newest on top, I swapped those to see where the email originated, so it's easier to read. 
- During this process, I read to use '&' at the end of using a mousepad command. I learned that using '&' runs the program in the background so it doesn't get stuck. 
