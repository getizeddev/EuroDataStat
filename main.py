from functionality import *

if __name__ == "__main__":

    country = CountrySelect()
    dataset = DatasetSelection()

    url = f'http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/{dataset}?geo={country}&precision=1'
    xValues = []
    yValues = []
    
    address = GetFilter(url)

    GetValues(address, xValues, yValues)

    ChartCreate(address, xValues,yValues)