from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import simpledialog
from datetime import datetime, timedelta
from functools import partial
from calculator import add_time, subtract_time

# globals
large_font = ("Helvetica", 24)
small_font = ("Helvetica", 18)
logTabBackground = "green"
todoTabBackground = "green"
calcTabBackground = "green"
warningBackground = "red"
note_list = []
note_time_list = []
todoCounter = 1
tasks_list = []
timeStart = datetime.now()
timeEnd = datetime.now()

# timer globals
timer_running = False
timer_job = None
elapsed_seconds = 0

def run_timer():
    global elapsed_seconds, timer_job

    if timer_running:
        elapsed_seconds += 1
        timer_job = window.after(1000, run_timer)

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

# check for empty entries
def inputError(field, errorField) :
    if field.strip() == "":
        errorField.config(text="Nothing Entered", bg = warningBackground)
        return 0
    return 1

# log functions
def clear_editNumberField():
    editNumberField.delete(0, END)

def clear_noteField():
    noteField.delete(0, END)

def clear_recordTextField():
    recordTextField.delete(0.0, END)

def editTitleClick():
    title = simpledialog.askstring("Input Title", "Change your Log's Title to:")
    value = inputError(title, noteError)
    if value == 0:
        return
    logTitleLabel.config(text=f"Log Title: {title}")
    note_list[0] = f"{note_time_list[0]} - Start of Log {title}: \n"
    noteError.config(text="", bg = logTabBackground)

def editDescClick():
    description = simpledialog.askstring("Input Description", "What is the Log about?")
    logDescriptionLabel.config(text=f"")
    if description != "":
        logDescriptionLabel.config(text=f"Description: {description}")
    noteError.config(text="", bg = logTabBackground)

def recordClick():
    title = simpledialog.askstring("Input Title", "What is your Log's Title?")
    description = simpledialog.askstring("Input Description", "What is the Log about?")
    value = inputError(title, noteError)
    if value == 0:
        return
    
    global note_list, note_time_list
    global timer_running, elapsed_seconds, timeStart
    clear_recordTextField()
    note_list = []
    note_time_list = []
    editTitleButton.config(state=NORMAL)
    editDescButton.config(state=NORMAL)

    elapsed_seconds = 0
    timer_running = True
    timeStart = datetime.now()
    run_timer()
    recordTextField.config(state=NORMAL)
    cTime = get_current_time()
    logTitleLabel.config(text=f"Log Title: {title}")
    logDescriptionLabel.config(text=f"")
    if description != "":
        logDescriptionLabel.config(text=f"Description: {description}")
    topEntry = f"{cTime} - Start of Log {title}: \n"
    note_list.append(topEntry)
    note_time_list.append(f"{cTime}")
    recordTextField.insert('end -1 chars', topEntry)

    clear_editNumberField()
    clear_noteField()
    noteError.config(text="", bg = logTabBackground)
    recordTextField.config(state=DISABLED)
    recordStart.config(state=DISABLED)
    recordNote.config(state=NORMAL)
    recordEnd.config(state=NORMAL)

def noteClick():
    global note_list, note_time_list
    value = inputError(noteField.get(), noteError)
    if value == 0 :
        return
    
    recordTextField.config(state=NORMAL)
    cTime = get_current_time()
    note_time_list.append(f"{cTime}")
    content = f"{noteField.get()}"
    note_list.append(content)
    recordTextField.insert('end -1 chars', f"[{len(note_list) - 1}] {cTime} - {content} \n")
    clear_editNumberField()
    clear_noteField()
    noteError.config(text="", bg = logTabBackground)
    recordTextField.config(state=DISABLED)
    return

def endClick():
    global timeStart, timeEnd
    global timer_running, elapsed_seconds, timer_job, timeStart
    
    recordTextField.config(state=NORMAL)
    cTime = get_current_time()
    timeEnd = datetime.now()
    
    timer_running = False
    if timer_job is not None:
        window.after_cancel(timer_job)
        timer_job = None
    total_time = timedelta(seconds=elapsed_seconds)

    recordTextField.insert('end -1 chars', f"{cTime} - End of log (Elapsed: {total_time})\n")
    clear_editNumberField()
    clear_noteField()
    noteError.config(text="", bg = logTabBackground)
    recordStart.config(state=NORMAL)
    recordNote.config(state=DISABLED)
    recordEnd.config(state=DISABLED)

def getNoteClick():
    global note_list
    global note_time_list
    if len(note_list) < 2:
        noteError.config(text="No notations", bg = warningBackground)
        return
    try:
        note_no = int(editNumberField.get())
        if note_no < 1 or note_no > len(note_list) - 1:
            raise ValueError
    except ValueError:
        noteError.config(text="Enter a valid note number", bg = warningBackground)
        return
    
    clear_noteField()
    noteField.insert(END, f"{note_list[note_no]}")
    noteError.config(text="", bg = logTabBackground)

def editNoteClick():
    global note_list
    global note_time_list
    if len(note_list) < 2:
        noteError.config(text="No notations", bg = warningBackground)
        return
    try:
        note_no = int(editNumberField.get())
        if note_no < 1 or note_no > len(note_list)-1:
            raise ValueError
    except ValueError:
        noteError.config(text="Enter a valid note number", bg = warningBackground)
        return
    value = inputError(noteField.get(), noteError)
    if value == 0 :
        return
    
    recordTextField.config(state=NORMAL)
    note_list[note_no] = noteField.get()
    clear_editNumberField()
    recordTextField.delete(1.0, END)
    for i, note in enumerate(note_list, start=1):
        if i == 1:
            recordTextField.insert(END, f"{note_list[0]}")
        else:
            recordTextField.insert(END, f"[{i-1}] {note_time_list[i-1]} - {note}\n")
    recordTextField.config(state=DISABLED)
    clear_editNumberField()
    clear_noteField()
    noteError.config(text="", bg = logTabBackground)

def deleteNoteClick():
    global note_list
    global note_time_list
    if len(note_list)<2:
        noteError.config(text="No notations", bg = warningBackground)
        return
    try:
        note_no = int(editNumberField.get())
        if note_no < 1 or note_no > len(note_list)-1:
            raise ValueError
    except ValueError:
        noteError.config(text="Enter a valid note number", bg = warningBackground)
        return
    
    recordTextField.config(state=NORMAL)
    note_list.pop(note_no)
    note_time_list.pop(note_no)
    clear_editNumberField()
    recordTextField.delete(1.0, END)
    for i, note in enumerate(note_list, start=1):
        if i == 1:
            recordTextField.insert(END, f"{note_list[0]}")
        else:
            recordTextField.insert(END, f"[{i-1}] {note_time_list[i-1]} - {note}\n")
    recordTextField.config(state=DISABLED)
    clear_editNumberField()
    noteError.config(text="", bg = logTabBackground)
    return

# todo functions
def clear_taskNumberField():
    taskNumberField.delete(0.0, END)

def clear_taskField():
    enterTodoTaskField.delete(0, END)

def insertTask():
    global todoCounter
    value = inputError(enterTodoTaskField.get(), taskError)
    if value == 0 :
        return
    
    TextArea.config(state = NORMAL)
    content = enterTodoTaskField.get()
    tasks_list.append(content)
    TextArea.insert('end -1 chars', f"[{todoCounter}] {content} \n")
    todoCounter += 1
    clear_taskField()
    taskError.config(text="", bg = todoTabBackground)
    TextArea.config(state = DISABLED)

def delete() :
    global todoCounter
    if not tasks_list:
        taskError.config(text="No tasks", bg = warningBackground)
        return
    try:
        task_no = int(taskNumberField.get(1.0, END))
        if task_no < 1 or task_no > len(tasks_list):
            raise ValueError
    except ValueError:
        taskError.config(text="Enter a valid task number", bg = warningBackground)
        return

    TextArea.config(state = NORMAL)
    tasks_list.pop(task_no - 1)
    todoCounter -= 1
    clear_taskNumberField()
    TextArea.delete(1.0, END)
    for i, task in enumerate(tasks_list, start=1):
        TextArea.insert(END, f"[{i}] {task}\n")
    taskError.config(text="", bg = todoTabBackground)
    TextArea.config(state = DISABLED)

# calcTab functions
def validate_entry(P, max_length):
    if P.isdigit() or P == "":
        if len(P) <= max_length:
            return True
        else:
            return False
    else:
        return False
    
def checkZero(x):
    if (x == ""):
        return 0
    else:
        return int(x)

# window info
window = Tk()
xField = 900
centerField = xField / 2
window.geometry(f"900x{xField}")
window.title("PTL")
window.config(background="black")

notebook = ttk.Notebook(window)
logTab = Frame(notebook, bg=logTabBackground)
todoTab = Frame(notebook, bg=todoTabBackground)
calcTab = Frame(notebook, bg=calcTabBackground)

notebook.add(logTab,text="PTL")
notebook.add(todoTab,text="Task List")
notebook.add(calcTab,text="Calculator")
notebook.pack(expand=True,fill="both")

# logTab
logTitle = Label(logTab,text="Personal Time Log")
logTitle.config(font=large_font)
logTitle.place(x=0,y=0)

recordingYpos = 100

recordStart = Button(logTab, text="Start", command=recordClick, font=small_font)
recordNoteLabel = Label(logTab, text="click to record a note:", font=small_font)
recordNote = Button(logTab, text="Note", command=noteClick, font=small_font, state=DISABLED)
recordEnd = Button(logTab, text="End", command=endClick, font=small_font, state=DISABLED)
recordEdit = Label(logTab, text="Edit note number:", font=small_font)
noteField = Entry(logTab, font=small_font, width=50)
editNumberField = Entry(logTab, font=small_font, width=2)
recordGetButton = Button(logTab, text="Get", command=getNoteClick, font=small_font)
recordEditButton = Button(logTab, text="Edit", command=editNoteClick, font=small_font)
noteDeleteButton = Button(logTab, text="Delete", command=deleteNoteClick, font=small_font)
noteError = Label(logTab, bg = logTabBackground, font=small_font)
editTitleButton = Button(logTab, text="Title", command=editTitleClick, font=small_font, state=DISABLED)
editDescButton = Button(logTab, text="Description", command=editDescClick, font=small_font, state=DISABLED)
editInfoLabel = Label(logTab, bg = logTabBackground, font=small_font, text="Edit:")
logTitleLabel = Label(logTab, bg = logTabBackground, font=small_font, text="Log Title:")
logDescriptionLabel = Label(logTab, bg = logTabBackground, font=small_font, text="Description:")
recordTextField = scrolledtext.ScrolledText(logTab, font=small_font,width=50, height=11)

recordStart.place(x=centerField-55, y=recordingYpos, anchor="center")
recordEnd.place(x=centerField+55, y=recordingYpos, anchor="center")
recordNoteLabel.place(x=centerField-140, y=recordingYpos+50, anchor="center")
recordNote.place(x=centerField+50, y=recordingYpos+50, anchor="center")
noteField.place(x=centerField, y=recordingYpos+100, anchor="center")
recordEdit.place(x=centerField-150, y=recordingYpos+150, anchor="center")
editNumberField.place(x=centerField, y=recordingYpos+150, anchor="center")
recordGetButton.place(x=centerField+70, y=recordingYpos+150, anchor="center")
recordEditButton.place(x=centerField+150, y=recordingYpos+150, anchor="center")
noteDeleteButton.place(x=centerField+250, y=recordingYpos+150, anchor="center")
noteError.place(x=centerField, y=recordingYpos+200, anchor="center")
editInfoLabel.place(x=centerField-130, y=recordingYpos+250, anchor="center")
editTitleButton.place(x=centerField-55, y=recordingYpos+250, anchor="center")
editDescButton.place(x=centerField+80, y=recordingYpos+250, anchor="center")
logTitleLabel.place(x=centerField, y=recordingYpos+300, anchor="center")
logDescriptionLabel.place(x=centerField, y=recordingYpos+350, anchor="center")
recordTextField.place(x=centerField, y=recordingYpos+550, anchor="center")

#todoTab
todoTitle = Label(todoTab,text="Task List")
todoTitle.config(font=large_font)
todoTitle.place(x=0, y=0)

enterTask = Label(todoTab, text = "Enter Your Task", font=small_font)
enterTodoTaskField = Entry(todoTab, font=small_font)
Submit = Button(todoTab, text = "Submit", font=small_font, fg = "Black", command = insertTask)
TextArea = scrolledtext.ScrolledText(todoTab, height = 12, width = 25, font=small_font, state = DISABLED)
taskNumber = Label(todoTab, text = "Delete Task Number", font=small_font)                       
taskNumberField = Text(todoTab, height = 1, width = 2, font =small_font)
deleteButton = Button(todoTab, text = "Delete", font=small_font, fg = "Black", command = delete)
taskError = Label(todoTab, bg = todoTabBackground, font=small_font) 

enterTask.place(x=centerField, y=recordingYpos, anchor="center")
enterTodoTaskField.place(x=centerField, y=recordingYpos+50, anchor="center")
Submit.place(x=centerField, y=recordingYpos+100, anchor="center")
TextArea.place(x=centerField, y=recordingYpos+310, anchor="center")
taskNumber.place(x=centerField-60, y=recordingYpos+520, anchor="center")
taskNumberField.place(x=centerField+100, y=recordingYpos+520, anchor="center")
deleteButton.place(x=centerField, y=recordingYpos+570, anchor="center")
taskError.place(x=centerField, y=recordingYpos+620, anchor="center")

#calcTab
twoVcmd = (calcTab.register(partial(validate_entry, max_length=2)), '%P')
threeVcmd = (calcTab.register(partial(validate_entry, max_length=3)), '%P')

calcTitle = Label(calcTab,text="Time Calculator", font=large_font)
calcTitle.place(x=0, y=0)
calcOrg = Label(calcTab,text="Day    hour    minute    second", font = small_font)
calcOrg.place(relx=0.5, y=recordingYpos, anchor="center")

firstEntries = recordingYpos + 75
secondEntries = recordingYpos + 150
opEntries = recordingYpos + 210
resultOutput = recordingYpos + 325
ruleY = recordingYpos + 375
textOutput = recordingYpos + 525

posOne =  centerField - 105         #195
posTwo = centerField - 32           #268
posThree = centerField + 32         #332
posFour = centerField + 95          #395

#operations
x = IntVar()

plus = Radiobutton(calcTab, text="Plus+", variable=x,value=1, font=small_font)
minus = Radiobutton(calcTab, text="Minus-", variable=x,value=2, font=small_font)
plus.place(x=centerField-80,y=opEntries,anchor="center")
minus.place(x=centerField+80,y=opEntries,anchor="center")
x.set(1)

# first row
day1 = Entry(calcTab)
day1.config(width=3, font=large_font, validate="key", validatecommand=threeVcmd)
day1.place(x=posOne, y=firstEntries, anchor="center")

hour1 = Entry(calcTab)
hour1.config(width=2, font=large_font, validate="key", validatecommand=twoVcmd)
hour1.place(x=posTwo, y=firstEntries, anchor="center")

minute1 = Entry(calcTab)
minute1.config(width=2, font=large_font, validate="key", validatecommand=twoVcmd)
minute1.place(x=posThree, y=firstEntries, anchor="center")

second1 = Entry(calcTab)
second1.config(width=2, font=large_font, validate="key", validatecommand=twoVcmd)
second1.place(x=posFour, y=firstEntries, anchor="center")

# second row
day2 = Entry(calcTab)
day2.config(width=3, font=large_font, validate="key", validatecommand=threeVcmd)
day2.place(x=posOne, y=secondEntries, anchor="center")

hour2 = Entry(calcTab)
hour2.config(width=2, font=large_font, validate="key", validatecommand=twoVcmd)
hour2.place(x=posTwo, y=secondEntries, anchor="center")

minute2 = Entry(calcTab)
minute2.config(width=2, font=large_font, validate="key", validatecommand=twoVcmd)
minute2.place(x=posThree, y=secondEntries, anchor="center")

second2 = Entry(calcTab)
second2.config(width=2, font=large_font, validate="key", validatecommand=twoVcmd)
second2.place(x=posFour, y=secondEntries, anchor="center")

#sign
showSign = Label(calcTab,text="", bg=calcTabBackground)
showSign.config(font=small_font)
showSign.place(relx=0.5, y=recordingYpos + 265, anchor="center")

# third row
day3 = Entry(calcTab)
day3.config(state=DISABLED, width=3, font=large_font)
day3.place(x=posOne, y=resultOutput, anchor="center")

hour3 = Entry(calcTab)
hour3.config(state=DISABLED, width=2, font=large_font)
hour3.place(x=posTwo, y=resultOutput, anchor="center")

minute3 = Entry(calcTab)
minute3.config(state=DISABLED, width=2, font=large_font)
minute3.place(x=posThree, y=resultOutput, anchor="center")

second3 = Entry(calcTab)
second3.config(state=DISABLED, width=2, font=large_font)
second3.place(x=posFour, y=resultOutput, anchor="center")

ruleSign = Label(calcTab,text="Entry One       +/-        Entry Two        =          Result")
ruleSign.config(font=small_font)
ruleSign.place(relx=0.5, y=ruleY, anchor="center")

historyText = scrolledtext.ScrolledText(calcTab,font=small_font, height=8,width=55)
historyText.place(x=centerField, y=textOutput, anchor="center")

def normalize():
    day3.config(state=NORMAL)
    day3.delete(0, END)
    hour3.config(state=NORMAL)
    hour3.delete(0, END)
    minute3.config(state=NORMAL)
    minute3.delete(0, END)
    second3.config(state=NORMAL)
    second3.delete(0, END)

def disablize():
    day3.config(state=DISABLED)
    hour3.config(state=DISABLED)
    minute3.config(state=DISABLED)
    second3.config(state=DISABLED)

def calcClick():
    setResult.config(state=NORMAL)
    normalize()
    d1 = checkZero(day1.get())
    h1 = checkZero(hour1.get())
    m1 = checkZero(minute1.get())
    s1 = checkZero(second1.get())
    d2 = checkZero(day2.get())
    h2 = checkZero(hour2.get())
    m2 = checkZero(minute2.get())
    s2 = checkZero(second2.get())
    d3 = 0
    h3 = 0
    m3 = 0
    s3 = 0
    sign = ""
    addNewText = ""
    
    selected = x.get()
    if selected == 1: #Plus is selected
        addNewText, d3, h3, m3, s3 = add_time(d1, h1, m1, s1, d2, h2, m2, s2)
        sign = ""
    elif selected == 2: #Minus is selected
        addNewText, sign, d3, h3, m3, s3 = subtract_time(d1, h1, m1, s1, d2, h2, m2, s2)
    
    if (sign == ""):
        showSign.config(text="", bg=calcTabBackground)
    elif (sign == "-"):
        showSign.config(text="negative time!", bg=warningBackground)
    historyText.insert(END, f" {addNewText}\n", "center")
    historyText.see("end")
    day3.insert(0, str(d3))
    hour3.insert(0, str(h3))
    minute3.insert(0, str(m3))
    second3.insert(0, str(s3))
    disablize()

def resultClick():
    day1.delete(0, END)
    hour1.delete(0, END)
    minute1.delete(0, END)
    second1.delete(0, END)
    day1.insert(0, day3.get())
    hour1.insert(0, hour3.get())
    minute1.insert(0, minute3.get())
    second1.insert(0, second3.get())
    
setResult = Button(calcTab, text="set result:")
setResult.config(font=small_font,command=resultClick, state=DISABLED)
setResult.place(x=posOne-120, y=firstEntries, anchor="center")

equalsButton = Button(calcTab,text="=")
equalsButton.config(command=calcClick, font=small_font)
equalsButton.place(x=centerField-178, y=resultOutput, anchor="center")

window.mainloop()