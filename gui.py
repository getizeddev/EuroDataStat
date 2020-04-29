import tkinter as tkr
import datasets as dt
import functionality as func

class App:
    def __init__(self, master, database):
        
        self.datasetSelected = None


        def populateList(listbox: tkr.Listbox):
            """
                The method populates the listbox with the names of the datasets matching the search of the user,
                basically visualizing the results of func.searchDataset
            """
            if self.searchBar.get() != "":
                listbox.delete(0 , tkr.END)
                results = func.searchDataset(self.searchBar.get(), database)
                for x, y in results.items():
                    listbox.insert(0, f'{y} [{x}]')

        #temporary: clear filter each time
        def populateFilters(frame: tkr.Frame):
            """
                Method displaying a listbox for each filter. The method also assigning to
                self.datasetSelected the correct value
            """
            filterList = None
            self.datasetSelected = func.datasetSelectionGui(self.resultList.get(tkr.ANCHOR))
            dataStructure = dt.DatasetStructure(database[self.datasetSelected][1])
            filters = tkr.Label(frame, text="FILTERS")
            filters.grid(row=0, column=0, columnspan=2)
            counter = 1
            for x in dataStructure.keys():
                filterTitle = tkr.Label(frame, text=str(x))
                filterTitle.grid(row=counter, column=0)
                filterList = tkr.Listbox(frame, width=30, height=5)
                filterList.grid(row=counter, column=1)
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
        self.frame.grid(row=1, column=6, rowspan=6)
    
        




        
#DEBUGGING:
database1 = dt.DatasetsName()
root = tkr.Tk()
gui = App(root, database1)


root.mainloop()
root.destroy()
