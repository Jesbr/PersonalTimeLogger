from tkinter import *
from tkinter import ttk

large_font = ("Helvetica", 24)
small_font = ("Helvetica", 18)

window = Tk()
window.geometry("600x600")
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
calcTitle = Label(calcTab,text="Time Calculator")
calcTitle.config(font=large_font)
calcTitle.place(x=0, y=0)
calcOrg = Label(calcTab,text="Day    hour    minute    second")
calcOrg.config(font=small_font)
calcOrg.place(relx=0.5, y=75, anchor="center")

firstEntries = 150
opEntries = 225
secondEntries = 300
resultOutput = 400

posOne = 195
posTwo = 268
posThree = 332
posFour = 395

#operations
x = IntVar()

plus = Radiobutton(calcTab, text="Plus+", variable=x,value=1, font=small_font)
minus = Radiobutton(calcTab, text="Minus-", variable=x,value=2, font=small_font)
plus.place(x=220,y=opEntries,anchor="center")
minus.place(x=380,y=opEntries,anchor="center")
x.set(1)

#days
day1 = Entry(calcTab)
day1.config(width=3, font=large_font)
day1.place(x=posOne, y=firstEntries, anchor="center")

day2 = Entry(calcTab)
day2.config(width=3, font=large_font)
day2.place(x=posOne, y=secondEntries, anchor="center")

day3 = Entry(calcTab)
day3.config(state=DISABLED, width=3, font=large_font)
day3.place(x=posOne, y=resultOutput, anchor="center")

#hours
hour1 = Entry(calcTab)
hour1.config(width=2, font=large_font)
hour1.place(x=posTwo, y=firstEntries, anchor="center")

hour2 = Entry(calcTab)
hour2.config(width=2, font=large_font)
hour2.place(x=posTwo, y=secondEntries, anchor="center")

hour3 = Entry(calcTab)
hour3.config(state=DISABLED, width=2, font=large_font)
hour3.place(x=posTwo, y=resultOutput, anchor="center")

#minutes
minute1 = Entry(calcTab)
minute1.config(width=2, font=large_font)
minute1.place(x=posThree, y=firstEntries, anchor="center")

minute2 = Entry(calcTab)
minute2.config(width=2, font=large_font)
minute2.place(x=posThree, y=secondEntries, anchor="center")

minute3 = Entry(calcTab)
minute3.config(state=DISABLED, width=2, font=large_font)
minute3.place(x=posThree, y=resultOutput, anchor="center")

#seconds
second1 = Entry(calcTab)
second1.config(width=2, font=large_font)
second1.place(x=posFour, y=firstEntries, anchor="center")

second2 = Entry(calcTab)
second2.config(width=2, font=large_font)
second2.place(x=posFour, y=secondEntries, anchor="center")

second3 = Entry(calcTab)
second3.config(state=DISABLED, width=2, font=large_font)
second3.place(x=posFour, y=resultOutput, anchor="center")

window.mainloop()