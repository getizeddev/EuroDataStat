import tkinter as tkr
import datasets as dt
import functionality as func

class App:
    def __init__(self, master, database):
        #Menu
        # |SearchBar| |SearchButton|    | Filters
        # |ListResults |                |"
        # |Select Button |              |"
        # |SeeData(or export excel)     |Create Chart Button
     

        def populateList(listbox):
            if self.searchBar.get() != "":
                listbox.delete(0 , tkr.END)
                results = func.searchDataset(self.searchBar.get(), database)
                for x, y in results.items():
                    listbox.insert(0, f'{y} [{x}]')

        #temporary: clear filter each time
        def populateFilters(frame):
            filterList = None
            dataset = func.datasetSelectionGui(self.resultList.get(tkr.ANCHOR), database)
            dataStructure = dt.DatasetStructure(database[dataset][1])
            counter = 0
            for x in dataStructure.keys():
                filterTitle = tkr.Label(frame, text=str(x))
                filterTitle.grid(row=0, column=counter)
                filterList = tkr.Listbox(frame, width=30)
                filterList.grid(row=1, column=counter)
                for y in dataStructure[x]:
                    filterList.insert(tkr.END,y)
                counter += 1


        #Label Search
        self.searchLabel = tkr.Label(master, text="Search: ")
        self.searchLabel.grid(row=0, column=0)
        #Entry for the search
        self.searchBar = tkr.Entry(master, width=50, relief=tkr.FLAT)
        self.searchBar.grid(row=0, column=1)
        self.searchBar.bind('<Return>', lambda e: populateList(self.resultList))
        #searchButton
        self.searchButton = tkr.Button(master, text='Search', bg="#7DE884", relief=tkr.FLAT, width=20, command = lambda: populateList(self.resultList))
        self.searchButton.grid(row=0, column=2)
        #ListBox
        self.resultList = tkr.Listbox(master, width=90, relief=tkr.FLAT)
        self.resultList.grid(row=1, column=0, columnspan =3)
        #Button that run the query
        self.selectButton = tkr.Button(master, text='Select Dataset', command=lambda: populateFilters(self.frame))
        self.selectButton.grid(row=2, column=0, padx=5, sticky=tkr.W)
        #debugger
        self.frame = tkr.Frame(master, width=100)
        self.frame.grid(row=1, column=4)




        
#DEBUGGING:
database1 = dt.DatasetsName()
root = tkr.Tk()
gui = App(root, database1)


root.mainloop()
root.destroy()
