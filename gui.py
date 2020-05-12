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
            filters = tkr.Label(frame, text="FILTERS", bg='#509461')
            filters.grid(row=0, column=0, columnspan=2)
            counter = 1

            for x in self.dataStructure.keys():
                subframe = FiltersFrame(frame, self.dataStructure, x, counter, self.filters)
                counter +=1

            self.dowloadButton.configure(state=tkr.NORMAL)

        def runQuery(urlstring):
            """
                The function populate the url with the filters and the dataset name, running a request for collecting data and generating the chart
            """
            if len(self.filters) != 0:
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
                populateFilters(self.frame)
            else:
                #Not really. Needs to be fixed
                top = tkr.Toplevel()
                top.title("Warning")
                msg = tkr.Message(top, text='No filter has been applied')
                msg.pack()
                button = tkr.Button(top, text="OK", command=top.destroy)
                button.pack()

        def downloadData(urlstring):
            """
                The function populate the url with the filters and the dataset name, running a request for collecting data and run the donwloadData funtionality
            """
            if len(self.filters) != 0:
                filterstring = ''
                for x in self.filters:
                    filterstring = filterstring + x
                address = f'{urlstring}{self.datasetSelected}?{filterstring}&precision=1'
                func.GetValues(address, self.xValues, self.yValues)
                func.DownloadData(self.xValues, self.yValues)
                self.filters.clear()
                self.xValues.clear()
                self.yValues.clear()
                populateFilters(self.frame)
            else:
                #Not really. Needs to be fixed
                top = tkr.Toplevel()
                top.title("Warning")
                msg = tkr.Message(top, text='No filter has been applied')
                msg.pack()
                button = tkr.Button(top, text="OK", command=top.destroy)
                button.pack()
                
        
        def clearCommand():
            self.frame.destroy()
            self.__init__(master, database, url)



        #Label Search
        self.searchLabel = tkr.Label(master, text="Search: ", bg='#509461')
        self.searchLabel.grid(row=0, column=0, padx=5, sticky=tkr.W)
        #Entry for the search
        self.searchBar = tkr.Entry(master, width=50, relief=tkr.FLAT)
        self.searchBar.grid(row=0, column=1, sticky=tkr.W)
        self.searchBar.bind('<Return>', lambda e: populateList(self.resultList))
        #searchButton
        self.searchButton = tkr.Button(master, text='Search', bg="#A995E8", relief=tkr.FLAT, width=10, command = lambda: populateList(self.resultList))
        self.searchButton.grid(row=0, column=2, sticky=tkr.E)
        #ListBox
        self.resultList = tkr.Listbox(master, width=90, relief=tkr.FLAT)
        self.resultList.grid(row=1, column=0, padx=(5,0), pady=5, columnspan =3)
        #Button that run the query
        self.selectButton = tkr.Button(master, text='Select Dataset', bg="#A995E8", relief=tkr.FLAT, command=lambda: populateFilters(self.frame))
        self.selectButton.grid(row=2, column=0, padx=5, pady=5, sticky=tkr.W)
        #button datacollection and visualization:
        self.runQueryButton = tkr.Button(master, text='run query', bg="#A995E8", relief=tkr.FLAT, command = lambda: runQuery(self.url))
        self.runQueryButton.grid(row=2, column=1, pady=5)
        #Clear Button
        self.clearButton = tkr.Button(master, text='Clear', bg='#A995E8', relief=tkr.FLAT, command= clearCommand)
        self.clearButton.grid(row=2, column=2, pady=5, sticky=tkr.E)
        #dowload button
        self.dowloadButton = tkr.Button(master, text='Dowload data', bg='#A995E8', relief=tkr.FLAT, state=tkr.DISABLED, command= lambda: downloadData(self.url))
        self.dowloadButton.grid(row=3, column=0, padx=5, pady=5, sticky=tkr.W)
        #filtersframes
        self.frame = tkr.Frame(master, width=100, bg="#509461")
        self.frame.grid(row=1, column=6, rowspan=6, padx=5)



class FiltersFrame:
    """
    Creates single boxes for the filters
    """
    def __init__(self, master: tkr.Frame, datastructure: dict, label: str, counter: int, listOfFilters: list):

        def selectFilter(x: str, listSelection: tkr.Listbox):
            filter= f'&{x.lower()}={listSelection.get(tkr.ANCHOR)[0]}'
            listSelection.itemconfig(tkr.ANCHOR, bg="#E8A366")
            print(filter) #for debugging
            listOfFilters.append(filter)
            self.button.configure(state=tkr.DISABLED)

        self.title = tkr.Label(master, text=str(label), bg='#509461')
        self.title.grid(row=counter, column=0)
        self.lister = tkr.Listbox(master, width=50, height=4)
        self.lister.grid(row=counter, column=1)
        for y in datastructure[label]:
            self.lister.insert(tkr.END, y)
        self.button = tkr.Button(master, text='Select', bg="#A995E8", relief=tkr.FLAT, command = lambda: selectFilter(label, self.lister))
        self.button.grid(row=counter, column=2, padx=5)
    
        




        

