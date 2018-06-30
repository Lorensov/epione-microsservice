import pandas as pd
from itertools import groupby 
from collections import OrderedDict
import json    

#cod_munic de brasilia eh 530010
def pdConvertCSVtoJSON( filePath ):
    dataFrame = pd \
    .read_csv( filePath, dtype = {
    "vlr_latitude"  : str,
    "vlr_longitude" : str,
    "cod_munic"     : str,
    "dsc_cidade"    : str,
    "dsc_bairro"    : str,
    "dsc_endereco"  : str,
    "nom_estab"     : str,
    "dsc_telefone"  : str
    }) \
    .set_index('cod_cnes') \
    .drop(
        ['dsc_estrut_fisic_ambiencia',
        'dsc_adap_defic_fisic_idosos',
        'dsc_equipamentos',
        'dsc_medicamentos'], 
    axis=1)

    queriedDataframe = dataFrame.query( 'cod_munic=="530010"' )

    json = queriedDataframe.to_json( orient='index' )

    return json
    
path = "resources/ubs.csv"