import xml.etree.ElementTree as xmlET
import requests

#This would return a dictionay {datasetId: [datasetName, datasetStructureId]}
def DatasetsName() -> dict:
    endpoint = requests.get("http://ec.europa.eu/eurostat/SDMX/diss-web/rest/dataflow/ESTAT/all/latest")
    structure = endpoint.content
    doc = xmlET.fromstring(structure)
    datasetsDict = {}
    for tags in doc[1][0]:
        if tags.get("id")[0:2] != "DS":
            datasetsDict[tags.get("id")] = [tags[0].text, f"DSD_{tags.get('id')}"]
    
    return datasetsDict


#this method would retrieve the structure of each dataset so that the Filters would be asked 
# before the json request, avoiding the 416 error response 
def DatasetStructure(datasetStructureId):
    structure = requests.get(f"http://ec.europa.eu/eurostat/SDMX/diss-web/rest/datastructure/ESTAT/{datasetStructureId}")
    data = structure.content
    doc = xmlET.fromstring(data)
    filtersDictionary = {}
    for codelist in doc[1][0].getchildren():
        if '_OBS_' not in codelist.get('id') :
            filtersDictionary[codelist[0].text] = [[code.get('id'), code [0].text] for code in codelist[1:]]
    
    return filtersDictionary
