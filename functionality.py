import requests
import numpy as np
import json
import matplotlib.pyplot as plt

#TO BE IMPLEMENTED: this would ask the user to select a country
def CountrySelect():
    country = input('Please select the country: ')
    return country.upper()

#TO BE IMPLEMENTED: this would ask the user to select the dataset
def DatasetSelection():
    dataset = input ("Please write the dataset to analyse: ")
    return dataset.lower()

#THIS need to be optimized: there are various filters to be taken in consideration. All the filters are displayed in "id" key in the Json file
def GetFilter(url):
    response = requests.get(url)
    data = response.json()

    print('Choose one of the following label:')

    #retrieve the filters to be applied
    for x,y in data['dimension']['unit']['category']['label'].items():
        print (f'{x} - {y}')
    #get user selection
    unit = input(': ')

    return f'{url}&unit={unit.upper()}'

def GetValues(url, xValuesList, yValuesList):
    response = requests.get(url)
    data = response.json()

    for x, y in data["value"].items():
        for key, value in data["dimension"]["time"]["category"]['index'].items():
            if str(value) == x:
                xValuesList.append(key)
                yValuesList.append(y)

def ChartCreate(url, xValuesList, yValuesList):
    response = requests.get(url)
    data = response.json()
    title = f"{data['label']} \n {data['dimension']['unit']['category']['label']}"

    plt.bar(xValuesList, yValuesList)
    plt.title(title)
    plt.show()