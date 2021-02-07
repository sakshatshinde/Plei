def plei():
    import tkinter as tk
    from tkinter import ttk
    import tkinter.font as fontyPoo # Sorry for the weird name :p
    import winsound, pickle
    from src.gameOps import readData, sync, launchGame
    # import fetchData

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



    root = tk.Tk()

    # removes title bar 
    root.overrideredirect(True)

    # Window config
    root.configure(background = BG_VAL, height = 800, width = 1600)
    root.resizable(tk.FALSE, tk.FALSE)

    # sets the window in center of the screen
    try:
        root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
    # fix for some devices
    except:
        root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

    # Title 
    titleLine = tk.Label(  root, 
                    text = 'Plei - A game launcher with no bloat',
                    fg = '#039be5',
                    background = BG_VAL,
                    font=('Helvetica', 11, 'bold'),
                    relief = tk.FLAT
    )
    titleLine.place(x = root.winfo_width()/2, y = 20 , anchor= 'center')


    # Game list
    sync()  # Update List STATE
    GAMES = readData() # Read from plei data file
    customFont = fontyPoo.Font(size = 12)
    gameList = tk.Listbox(root, 
                        bg = BG_VAL, 
                        bd = 20,
                        fg = '#ffab40',
                        relief = tk.FLAT, 
                        highlightthickness = 5,
                        selectmode = tk.SINGLE,
                        height = 35,
                        highlightcolor = '#f2209e',
                        selectbackground = BG_VAL,
                        selectforeground = '#039be5',
                        width = 0,
                        activestyle = tk.NONE,
                        font = customFont
                        )
                        
    gameList.yview()    #vertical scroll
    gameList.insert(0, *GAMES)
    gameList.place(x = root.winfo_width()/55, y = 40, anchor = tk.NW )

    # A class to save object state
    class Selection:
        currentSelection = ''

    # Selecting the game from the list 
    def curSelect(evt):
        # Save the selection state inside the class variable
        Selection.currentSelection = gameList.get(tk.ANCHOR)
    gameList.bind('<<ListboxSelect>>',curSelect)

    # Launching the selected game
    def launch():
        launchGame(Selection.currentSelection)

    # Launch button label
    launchLabel = tk.Label(  root, 
                    text = 'Plei ',
                    fg = '#039be5',
                    background = BG_VAL,
                    font = ('Helvetica', 20, 'bold'),
                    relief = tk.FLAT
    )
    launchLabel.place(x = root.winfo_width()/2, y = root.winfo_height()/2.5, anchor= tk.CENTER)

    # Launch Button
    launchIcon = tk.PhotoImage(file = 'resources\\tic-tac-toe.png')
    launchIcon = launchIcon.subsample(5,5)
    launchBtn = tk.Button(
        root, 
        image = launchIcon,  
        background=BG_VAL, 
        command = launch,
        activebackground = BG_VAL, 
        borderwidth = 0
    ) 
    launchBtn.place(x = root.winfo_width()/2, y = root.winfo_height()/2, anchor = tk.CENTER)
    # x = 1200

    # Header
    title = tk.Label(  root, 
                    text = 'Games ',
                    fg = '#039be5',
                    background = BG_VAL,
                    font = ('Helvetica', 20, 'bold'),
                    relief = tk.FLAT
    )
    title.place(x = root.winfo_width()/72, y = 60 , anchor= tk.SW)

    # # Image
    # img = PhotoImage(file = 'data\\img\\Apex legends.png') # Test image
    # label = Label(image = img)
    # label.place(x = root.winfo_width()/2, y = root.winfo_height()/2, anchor = CENTER )


    # Footer
    footer = tk.Label(  root, 
                    text = 'Have Fun ',
                    fg = '#039be5',
                    background = BG_VAL,
                    font = ('Helvetica', 14, 'bold'),
                    relief = tk.FLAT
    )
    footer.place(x = root.winfo_width()/65, y = 765 , anchor = tk.SW)

    # Minimize button
    minIcon = tk.PhotoImage(file = 'resources\\minus.png')
    minIcon = minIcon.subsample(20,20)
    minBtn = tk.Button(
        root, 
        image = minIcon,  
        background=BG_VAL, 
        command = minWin,
        activebackground = BG_VAL, 
        borderwidth = 0
    ) 
    minBtn.place(relx = 1, x = -38, y = 5, anchor = tk.NE)

    # Close button
    closeIcon = tk.PhotoImage(file = 'resources\\close.png')
    #Resizing the image for the button to fit
    closeIcon = closeIcon.subsample(20,20)
    closeBtn = tk.Button(
        root, 
        image = closeIcon , 
        command=close, 
        background=BG_VAL, 
        activebackground = BG_VAL,
        borderwidth = 0
    ) 
    closeBtn.place(relx = 1, x =-5, y = 5, anchor = tk.NE)

    # Hover for buttons
    minBtn.bind("<Enter>", onEnterMin)
    minBtn.bind("<Leave>", onLeaveMin)
    closeBtn.bind("<Enter>", onEnterClose)
    closeBtn.bind("<Leave>", onLeaveClose)

    # Added bindings to pass windows status to function : MAXIMIZE AND MINIMIZE
    root.bind('<Map>', check_map) 
    root.bind('<Unmap>', check_map)
    root.mainloop()
