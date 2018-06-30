import urllib
import urllib.request

def getHTML(url):
    print(url)

def downloadFile(url, file_name):
# Download the file from `url` and save it locally under `file_name`:
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        data = response.read() # a `bytes` object
        print("downloading!")
        out_file.write(data)
    print("DONE!")

downloadFile( "http://repositorio.dados.gov.br/saude/unidades-saude/unidade-basica-saude/ubs.csv", "ubs.csv" )

