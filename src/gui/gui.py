from tkinter import *
from tkinter import ttk
import tkinter.font as fontyPoo # Sorry for the weird name :p
import winsound, pickle, fetchData, asyncio

# Dirty fix --------
import sys
sys.path.append('D:\\dev\\Plei\\src')
from gameOps import readData, sync, launchGame
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

# def rating():
#     ratingList = []
#     allGames = GAMES
#     for game in allGames:
#         ratingList.append(fetchData.gameRating(game))
#     final = dict(zip(allGames, ratingList))
#     print(final)

# rating()

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

# Title 
titleLine = Label(  root, 
                text = 'Plei - A game launcher with no bloat',
                fg = '#039be5',
                background = BG_VAL,
                font=('Helvetica', 11, 'bold'),
                relief = FLAT
)
titleLine.place(x = root.winfo_width()/2, y = 20 , anchor= 'center')


# Game list
sync()  # Update List STATE
GAMES = readData() # Read from plei data file
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

# A class to save object state
class Selection:
    currentSelection = ''

# Selecting the game from the list 
def curSelect(evt):
    # Save the selection state inside the class variable
    Selection.currentSelection = gameList.get(ANCHOR)
gameList.bind('<<ListboxSelect>>',curSelect)

# Launching the selected game
def launch():
    launchGame(Selection.currentSelection)

# Launch button label
launchLabel = Label(  root, 
                text = 'Plei ',
                fg = '#039be5',
                background = BG_VAL,
                font = ('Helvetica', 20, 'bold'),
                relief = FLAT
)
launchLabel.place(x = root.winfo_width()/2, y = root.winfo_height()/2.5, anchor= CENTER)

# Launch Button
launchIcon = PhotoImage(file = 'resources\\tic-tac-toe.png')
launchIcon = launchIcon.subsample(5,5)
launchBtn = Button(
    root, 
    image = launchIcon,  
    background=BG_VAL, 
    command = launch,
    activebackground = BG_VAL, 
    borderwidth = 0
) 
launchBtn.place(x = root.winfo_width()/2, y = root.winfo_height()/2, anchor = CENTER)
# x = 1200

# Header
title = Label(  root, 
                text = 'Games ',
                fg = '#039be5',
                background = BG_VAL,
                font = ('Helvetica', 20, 'bold'),
                relief = FLAT
)
title.place(x = root.winfo_width()/72, y = 60 , anchor= SW)

# # Image
# img = PhotoImage(file = 'data\\img\\Apex legends.png') # Test image
# label = Label(image = img)
# label.place(x = root.winfo_width()/2, y = root.winfo_height()/2, anchor = CENTER )


# Footer
footer = Label(  root, 
                text = 'by ScreX ',
                fg = '#039be5',
                background = BG_VAL,
                font = ('Helvetica', 14, 'bold'),
                relief = FLAT
)
footer.place(x = root.winfo_width()/65, y = 765 , anchor= SW)

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