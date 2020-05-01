import tkinter as tkr
import datasets as dt
import functionality as func

class App:
    def __init__(self, master, database, url):
        
        self.datasetSelected = None
        self.url = url
        self.dataStructure = {}
        self.filters = []
        self.xValues = []
        self.yValues = []


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
                self.datasetSelected and self.dataStructure the correct value
            """
            self.datasetSelected = func.datasetSelectionGui(self.resultList.get(tkr.ANCHOR))
            self.dataStructure = dt.DatasetStructure(database[self.datasetSelected][1])
            filters = tkr.Label(frame, text="FILTERS")
            filters.grid(row=0, column=0, columnspan=2)
            counter = 1

            for x in self.dataStructure.keys():
                subframe = FiltersFrame(frame, self.dataStructure, x, counter, self.filters)
                counter +=1

        def runQuery(urlstring):
            """
                The function populate the url with the filters and the dataset name, running a request for collecting data and generating the chart
            """
            filterstring = ''
            for x in self.filters:
                filterstring = filterstring + x
            address = f'{urlstring}{self.datasetSelected}?{filterstring}&precision=1'
            #debugging
            print(urlstring)
            print(address)
            print(self.filters)
            print(self.datasetSelected)
            #
            func.GetValues(address, self.xValues, self.yValues)
            func.ChartCreate(address, self.xValues, self.yValues)
            self.filters.clear()
            self.xValues.clear()
            self.yValues.clear()
            



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
        self.selectButton = tkr.Button(master, text='Select Dataset', bg="#7DE884", relief=tkr.FLAT, command=lambda: populateFilters(self.frame))
        self.selectButton.grid(row=2, column=0, padx=5, sticky=tkr.W)
        #filtersframes
        self.frame = tkr.Frame(master, width=100)
        self.frame.grid(row=1, column=6, rowspan=6)
        #button datacollection and visualization:
        self.runQueryButton = tkr.Button(master, text='run query', bg="#7DE884", relief=tkr.FLAT, command = lambda: runQuery(self.url))
        self.runQueryButton.grid(row=3, column=1)


class FiltersFrame:
    """
    Creates single boxes for the filters
    """
    def __init__(self, master: tkr.Frame, datastructure: dict, label: str, counter: int, listOfFilters: list):

        def selectFilter(x: str, listSelection: tkr.Listbox):
            filter= f'&{x.lower()}={listSelection.get(tkr.ANCHOR)[0]}'
            print(filter) #for debugging
            listOfFilters.append(filter)

        self.title = tkr.Label(master, text=str(label))
        self.title.grid(row=counter, column=0)
        self.lister = tkr.Listbox(master, width=50, height=5)
        self.lister.grid(row=counter, column=1)
        for y in datastructure[label]:
            self.lister.insert(tkr.END, y)
        self.button = tkr.Button(master, text='Select', bg="#7DE884", relief=tkr.FLAT, command = lambda: selectFilter(label, self.lister))
        self.button.grid(row=counter, column=2)
    
        




        

