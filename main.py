from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from functools import partial
from calculator import add_time, subtract_time

large_font = ("Helvetica", 24)
small_font = ("Helvetica", 18)

def validate_entry(P, max_length):
    if P.isdigit() or P == "":
        if len(P) <= max_length:
            return True
        else:
            return False
    else:
        return False
    
def ifZero(x):
    if (x == ""):
        return 0
    else:
        return int(x)

window = Tk()
xField = 900
window.geometry(f"900x{xField}")
window.title("PTL")
window.config(background="black")

notebook = ttk.Notebook(window)
logTab = Frame(notebook, bg="blue")
calcTab = Frame(notebook, bg="black")

notebook.add(logTab,text="PTL")
notebook.add(calcTab,text="Calculator")
notebook.pack(expand=True,fill="both")

# logTab
logTitle = Label(logTab,text="Personal Time Log")
logTitle.config(font=large_font)
logTitle.place(x=0,y=0)

#calcTab
twoVcmd = (calcTab.register(partial(validate_entry, max_length=2)), '%P')
threeVcmd = (calcTab.register(partial(validate_entry, max_length=3)), '%P')

calcTitle = Label(calcTab,text="Time Calculator")
calcTitle.config(font=large_font)
calcTitle.place(x=0, y=0)
calcOrg = Label(calcTab,text="Day    hour    minute    second")
calcOrg.config(font=small_font)
calcOrg.place(relx=0.5, y=75, anchor="center")

firstEntries = 150
secondEntries = 225
opEntries = 300
resultOutput = 400
ruleY = 500
textOutput = 650

centerField = xField / 2
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
showSign = Label(calcTab,text="")
showSign.config(font=small_font)
showSign.place(relx=0.5, y=350, anchor="center")

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
    #day3.insert(0, "    ")
    day3.delete(0, END)
    hour3.config(state=NORMAL)
    #hour3.insert(0, "  ")
    hour3.delete(0, END)
    minute3.config(state=NORMAL)
    #minute3.insert(0, "  ")
    minute3.delete(0, END)
    second3.config(state=NORMAL)
    #second3.insert(0, "  ")
    second3.delete(0, END)

def disablize():
    day3.config(state=DISABLED)
    hour3.config(state=DISABLED)
    minute3.config(state=DISABLED)
    second3.config(state=DISABLED)

def click():
    normalize()
    d1 = ifZero(day1.get())
    h1 = ifZero(hour1.get())
    m1 = ifZero(minute1.get())
    s1 = ifZero(second1.get())
    d2 = ifZero(day2.get())
    h2 = ifZero(hour2.get())
    m2 = ifZero(minute2.get())
    s2 = ifZero(second2.get())
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
        showSign.config(text="")
    elif (sign == "-"):
        showSign.config(text="negative time!")
    historyText.insert(END, f" {addNewText}\n", "center")
    historyText.see("end")
    day3.insert(0, str(d3))
    hour3.insert(0, str(h3))
    minute3.insert(0, str(m3))
    second3.insert(0, str(s3))
    disablize()
    

equalsButton = Button(calcTab,text="=")
equalsButton.config(command=click, font=small_font)
equalsButton.place(x=centerField-178, y=resultOutput, anchor="center")

window.mainloop()