import csv
import json

#cod_munic de brasilia eh 530010

def convertCSVtoJSON(filePath):
    csvFile = open( filePath + 'ubs.csv', 'r' ) 
    jsonFile = open( filePath + 'ubs.json', 'w' )
    columnNames = ( "vlr_latitude", "vlr_longitude", "cod_munic", "dsc_cidade", "dsc_bairro", "dsc_endereco", "nom_estab", "dsc_telefone" )
    reader = csv.DictReader( csvFile, columnNames )
    for row in reader:
        json.dump( row, jsonFile )
        jsonFile.write('\n')

path = "resources/"
convertCSVtoJSON(path)