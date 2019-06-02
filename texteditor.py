from tkinter import *
from tkinter.filedialog import *

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    openedFile = open(filename, 'w')
    openedFile.write(t)
    openedFile.close()

def saveFileAs():
    global filename
    openedFile = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        openedFile.write(t.rstrip())
        filename = openedFile.name
    except:
        showerror("Oops!", "Unable to save file")

def openFile():
    global filename
    openedFile = askopenfile(mode='r')
    t = openedFile.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    filename = openedFile.name

def selectDarkTheme():
    global text
    text.config(fg="white", bg="black")

def selectWhiteTheme():
    global text
    text.config(fg="black", bg="white")

root = Tk()
root.title("Text Editor")

text = Text(root, width=400, height=400)
text.pack()

# Menu Bar
menuBar = Menu(root)
fileMenu = Menu(menuBar)
themeMenu = Menu(menuBar)

# Menu: File Load / Save
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Save As...", command=saveFileAs)
fileMenu.add_separator()

# Menu: Quit
fileMenu.add_command(label="Quit", command=root.quit)

# Themes
themeMenu.add_command(label="Dark Theme", command=selectDarkTheme)
themeMenu.add_command(label="White Theme", command=selectWhiteTheme)

# Add menu to root
menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Style", menu=themeMenu)
root.config(menu=menuBar)

root.mainloop()