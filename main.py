import gui
import datasets as dt
import tkinter as tkr


if __name__ == "__main__":

    
    datasetDictionary = dt.DatasetsName()
    url = 'http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/'
    root = tkr.Tk()
    root.geometry('1000x600')
    root.configure(bg='#509461')
    root.title('Eurostat Data')
    application = gui.App(root, datasetDictionary, url)
    
    root.mainloop()
    try: 
        root.destroy()
    except tkr.TclError:
        pass