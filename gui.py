import tkinter as tkr
import datasets as dt
import functionality as func

class App:
    def __init__(self, master):
        #Menu
        # |SearchBar| |SearchButton|    | Filters
        # |ListResults |                |"
        # |Select Button |              |"
        # |SeeData(or export excel)     |Create Chart Button
        self.searchBar = tkr.Entry(master)
        self.searchBar.grid(row=0, column=0)
        self.searchButton = tkr.Button(master, text='Search')
        self.searchButton.grid(row=0, column=1)
        

        
#DEBUGGING:
# dataset = dt.DatasetsName()
root = tkr.Tk()
gui = App(root)

root.mainloop()
root.destroy()
