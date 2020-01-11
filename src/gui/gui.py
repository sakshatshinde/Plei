from tkinter import *
from tkinter import ttk
import winsound

BG_VAL = "#000000"
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

def onEnterMin(e):
    minBtn['background'] = '#424242'

def onLeaveMin(e):
    minBtn['background'] = BG_VAL
        

root = Tk()
# removes title bar 
root.overrideredirect(True)
root.configure(background = BG_VAL, height = 800, width = 1600)
root.resizable(FALSE, FALSE)
# sets the window in center of the screen
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

# Minimize button
minIcon = PhotoImage(file = r'resources/minus.png')
minIcon = minIcon.subsample(20,20)
minBtn = Button(
    root, 
    image = minIcon,  
    background=BG_VAL, 
    command = minWin,
    activebackground = BG_VAL, 
    borderwidth = 0
) 
minBtn.place(relx = 1, x = -45, y = 5, anchor = NE)

# Close button
closeIcon = PhotoImage(file = r'resources/close.png')
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
closeBtn.place(relx = 1, x =-10, y = 5, anchor = NE)

minBtn.bind("<Enter>", on_enter)
minBtn.bind("<Leave>", on_leave)
root.bind('<Map>', check_map) # added bindings to pass windows status to function
root.bind('<Unmap>', check_map)
root.mainloop()