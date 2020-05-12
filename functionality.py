import requests
import numpy as np
import json
import matplotlib.pyplot as plt
import xlsxwriter as xl


#This function implement the Dataset search of the GUI
def searchDataset(entryText: str, database: dict) -> dict:
    """
    This function filters the database, searching the dataset(s) that match the entry of the user
    
    Parameters:
        entryText(str): the string typed by the user in the search bar
        database(dict): the whole database of Eurostat containing all the dataset and datastructures:
            see DatasetsName in datasets.py

    Returns:
        A dictionary of datasets matching the entrysearch: {datasetID: datasetName}

    """
    searchResultList = {}
    for x, y in database.items():
        if (entryText.lower() in x.lower() or entryText.lower() in y[0].lower()):
            searchResultList[x] = y[0]
    return searchResultList 

def datasetSelectionGui(selection: str) -> str:
    """
        From the dataset selected in the results listBox, this function simply retrieves the datasetID.

        Parameters:
            selection(str): selected entry in the results listBox

    """
    start = selection.find("[") + 1
    end = selection.find("]")
    datasetID = selection[start:end]
    return datasetID
    




def GetValues(url: str, xValuesList: list, yValuesList: list):
    """
        This function send a get request to the dataset endpoint and retrieves the values accordingly. The values are then populating the 2 lists of xValuea and yValues 
    """
    try:
        response = requests.get(url)
        data = response.json()

        for x, y in data["value"].items():
            for key, value in data["dimension"]["time"]["category"]['index'].items():
                if str(value) == x:
                    xValuesList.append(key)
                    yValuesList.append(y)
    except KeyError:
        #This needs to be fixed
        print(f'{response.status_code} - Probably one of the filter doesn\'t apply to the country selected')
        exit()


def ChartCreate(url: str, xValuesList: list, yValuesList: list):
    """
        Simple data visualization
    """
    with requests.get(url) as response:
        data = response.json()
        title = data['label']
        print(data['extension']['description'])

        plt.bar(xValuesList, yValuesList)
        plt.title(title)
        plt.show(block=False)


def DownloadData(xList: list, yList: list):
    """
        The method retireves the data stored in the x and y values list and download them in an Excel worksheet
    """
    with xl.Workbook('Data.xlsx') as wk:
        worksheet = wk.add_worksheet()
        worksheet.write(0,0,'x')
        worksheet.write(0,1,'y')
        row = 0
        column = 0
        while row < len(xList):
            worksheet.write(row + 1, column, xList[row])
            worksheet.write(row + 1, column + 1, yList[row])
            row +=1

