import gui
import datasets as dt
import tkinter as tkr

#Time to add the GUI -> TkInter

if __name__ == "__main__":

    
    datasetDictionary = dt.DatasetsName()
    url = 'http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/'
    root = tkr.Tk()
    application = gui.App(root, datasetDictionary, url)
    
    root.mainloop()
    try: 
        root.destroy()
    finally:
        pass