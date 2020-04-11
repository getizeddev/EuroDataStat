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

#Optimed to get all the filters from the id[] in the Json
def GetFilter(url):
    response = requests.get(url)
    data = response.json()
    print(f"{data['label']} - updated: {data['updated']} \n \n")

    filterDictionary = {}

    for x in data['id']:
        if (x != 'geo' and x!='time'):
            print(f'{x} : Choose one of the following label:')
            for key,value in data['dimension'][x]['category']['label'].items():
                print (f'{key} - {value}')
            unit = input(': ')
            filterDictionary[x] = unit.upper()
    
    for xFilter, yFilter in filterDictionary.items():
        url = f'{url}&{xFilter}={yFilter}'

    return url

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