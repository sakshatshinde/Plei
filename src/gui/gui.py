from tkinter import *
from tkinter import ttk
import tkinter.font as fontyPoo # Sorry for the weird name :p
import winsound, pickle

# Dirty fix --------
import sys
sys.path.append('D:\\dev\\Plei\\src')
from gameOps import readData
# -----------

BG_VAL = "#212121"
FG_VAL = "#D2BF55"

def close(): #Close the window
    root.destroy()

def minWin():   #minimze the window
    root.withdraw()
    root.overrideredirect(False)
    root.iconify()

def check_map(event): # apply override on deiconify.
    if str(event) == "<Map event>":
        root.overrideredirect(True)
    else:
        pass

# Hover functions
def onEnterMin(e):
    minBtn['background'] = '#424242'

def onLeaveMin(e):
    minBtn['background'] = BG_VAL

def onEnterClose(e):
    closeBtn['background'] = '#424242'

def onLeaveClose(e):
    closeBtn['background'] = BG_VAL
        

root = Tk()

# removes title bar 
root.overrideredirect(True)

# Window config
root.configure(background = BG_VAL, height = 800, width = 1600)
root.resizable(FALSE, FALSE)

# sets the window in center of the screen
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

#Title 
titleLine = Label(  root, 
                text = 'Plei - A game launcher with no bloat',
                fg = '#039be5',
                background = BG_VAL,
                font=('Helvetica', 11, 'bold'),
                relief = FLAT
)
titleLine.place(x = root.winfo_width()/2, y = 20 , anchor= 'center')

# DATA FILE -> GAME_MASTER_LIST
# file = open('gameList.plei', 'rb')
# GAMES = pickle.load(file)
# file.close()
# print(GAMES)
GAMES = readData()
customFont = fontyPoo.Font(size = 12)
gameList = Listbox(root, 
                    bg = BG_VAL, 
                    bd = 20,
                    fg = '#ffab40',
                    relief = FLAT, 
                    highlightthickness = 5,
                    selectmode = SINGLE,
                    height = 35,
                    highlightcolor = '#f2209e',
                    selectbackground = BG_VAL,
                    selectforeground = '#039be5',
                    width = 0,
                    activestyle = NONE,
                    font = customFont
                    )
                    
gameList.yview()    #vertical scroll
gameList.insert(0, *GAMES)
gameList.place(x = root.winfo_width()/55, y = 40, anchor = NW )

# Footer 
title = Label(  root, 
                text = 'Games ',
                fg = '#039be5',
                background = BG_VAL,
                font = ('Helvetica', 20, 'bold'),
                relief = FLAT
)
title.place(x = root.winfo_width()/72, y = 60 , anchor= SW)

# Minimize button
minIcon = PhotoImage(file = 'resources\\minus.png')
minIcon = minIcon.subsample(20,20)
minBtn = Button(
    root, 
    image = minIcon,  
    background=BG_VAL, 
    command = minWin,
    activebackground = BG_VAL, 
    borderwidth = 0
) 
minBtn.place(relx = 1, x = -38, y = 5, anchor = NE)

# Close button
closeIcon = PhotoImage(file = 'resources\\close.png')
#Resizing the image for the button to fit
closeIcon = closeIcon.subsample(20,20)
closeBtn = Button(
    root, 
    image = closeIcon , 
    command=close, 
    background=BG_VAL, 
    activebackground = BG_VAL,
    borderwidth = 0
) 
closeBtn.place(relx = 1, x =-5, y = 5, anchor = NE)

# Hover for buttons
minBtn.bind("<Enter>", onEnterMin)
minBtn.bind("<Leave>", onLeaveMin)
closeBtn.bind("<Enter>", onEnterClose)
closeBtn.bind("<Leave>", onLeaveClose)



# Added bindings to pass windows status to function : MAXIMIZE AND MINIMIZE
root.bind('<Map>', check_map) 
root.bind('<Unmap>', check_map)
root.mainloop()