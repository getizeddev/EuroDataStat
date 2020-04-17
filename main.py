import functionality as func
import datasets as dt

if __name__ == "__main__":

    datasetDictionary = dt.DatasetsName()
    country = func.CountrySelect() #see comment in functionality.py
    dataset = func.DatasetSelection(datasetDictionary) #for debugging purposes

    url = f'http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/{dataset}?geo={country}&precision=1'
    #some dataset have too many categories to be retrieved with only these 2 inital filter
    # Implementation needed in such cases - (response 416) -> dt.DatasetStructure()
    xValues = []
    yValues = []
    
    address = func.GetFilter(url)

    func.GetValues(address, xValues, yValues)

    func.ChartCreate(address, xValues,yValues, country)