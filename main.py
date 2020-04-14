from functionality import *

if __name__ == "__main__":

    country = CountrySelect()
    dataset = DatasetSelection()

    url = f'http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/{dataset}?geo={country}&precision=1'
    #some dataset have too many categories to be retrieved with only these 2 inital filter
    # Implementation needed in such cases - (response 416) 
    xValues = []
    yValues = []
    
    address = GetFilter(url)

    GetValues(address, xValues, yValues)

    ChartCreate(address, xValues,yValues, country)