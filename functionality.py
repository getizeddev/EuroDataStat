import requests
import numpy as np
import json
import matplotlib.pyplot as plt
import random

#This function asks the user to select the dataset
def DatasetSelection(diction): #diction added only for debugging purpouses
    dataset = input (f"Please write the dataset to analyse: {random.choice(list(diction.keys()))} ")
    return dataset.lower()

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
    

#This function, after retrieving the structure of the dataset, asks the user to apply the desired filters
def GetFilter(url, datasetStructure):
    print("Select the filters to be applied")
    for x in datasetStructure.keys():
        print(x)
        for filter in datasetStructure[x]:
            print(f"{filter[0]} - {filter[1]}")
        filterselected = input()
        url = url+f"&{x.lower()}={filterselected.upper()}"
    return url

#This function retrieves the data allocating them in 2 lists[] of values 
#ISSUE: sometimes some filters of the structure don't exist for the selecting country, generating a 400 response
def GetValues(url, xValuesList, yValuesList):
    try:
        response = requests.get(url)
        data = response.json()

        for x, y in data["value"].items():
            for key, value in data["dimension"]["time"]["category"]['index'].items():
                if str(value) == x:
                    xValuesList.append(key)
                    yValuesList.append(y)
    except KeyError:
        print(f'{response.status_code} - Probably one of the filter doesn\'t apply to the country selected')
        exit()

#This function visualizes the data
def ChartCreate(url, xValuesList, yValuesList):
    response = requests.get(url)
    data = response.json()
    title = data['label']
    print(data['extension']['description'])

    plt.bar(xValuesList, yValuesList)
    plt.title(title)
    plt.show()