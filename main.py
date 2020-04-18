import functionality as func
import datasets as dt

if __name__ == "__main__":

    datasetDictionary = dt.DatasetsName()

    dataset = func.DatasetSelection(datasetDictionary) #see comment in func
    print(datasetDictionary[dataset][0])
    structure = dt.DatasetStructure(datasetDictionary[dataset][1])

    url = f'http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/{dataset}?precision=1'
    address = func.GetFilter(url, structure)


    xValues = []
    yValues = []
    

    func.GetValues(address, xValues, yValues)

    func.ChartCreate(address,xValues, yValues)