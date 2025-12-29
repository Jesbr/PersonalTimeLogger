# PersonalTimeLogger

What the project is, and what it does:

This project is split into three parts: a personal log, a task list, and a time calculator.

When starting the log, it will require a title for the log, and give an option to have a description for it. Both of these can be edited later on. The log is not interactable when it is ongoing. The log will show when the user started the log, allow the user to take notes and show when those notes were taken, get, edit, and/or delete those notes if needed, and once the log is done it will show when the log ended, how long the log took to complete, and the description of the log if there is one.
All notes are numbered with ([#] - ) to help identify which note to get, edit, or delete if necessary.
Once the log ends, the user can interact with the log. It is also possible to start a new log after the first was completed.

With the task list the user can input tasks into the list they wish to focus on. The list will number the tasks with
([#] - ), and when the task is complete they can delete the task with the specified number in the number field and click [delete].

The time calculator can add or subtract two different times in the form of (day, hour, minute, second) with a maximum/minimum number of (999days, 23hours, 59minutes, 59 seconds). It calculates the two numbers into a third, non-interactable row that can be swiftly entered into the first entry row with the [result] button. It also takes into account blank entries acting as zeroes. The user can only enter positive numbers, as it is not expected to calculate negative amounts of time within the entries, but will warn the user if the output has been subtracted into a negative amount of time.
There is also a history list at the bottom, showing past calculations entered with the appropriate sign for the output in case of negative time. The history list is interactable for ease of  use.

# How to clone and run it:
## requirements:
- Python 3.12.3+
- Tkinter (usually installed with Python on windows/MacOS)

First ensure Python is installed with:
- python3 --version

Ensure Tkinter is installed with:
- python3 -m tkinter

A new window should appear displaying the Tkinter version number and information.

## Installing Tkinter on Linux:
Note: I have little to no experience with Linux as of yet, this has simply been double checked with google.

Linux (Ubuntu/Debian):
- sudo apt update
- sudo apt install python3-tk

Linux Arch:
- sudo pacman -S tk

Linux Fedora:
- sudo dnf install python3-tkinter

## Clone and run:
Clone the repository with: git clone https://github.com/Jesbr/PersonalTimeLogger.git
This should create a folder with: main.py, calculator.py, README.md, and __pycache__/.
go to the project folder with:
- cd PersonalTimeLogger

run the program with:
- python3 main.py