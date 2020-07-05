# https://fr.python-requests.org/en/latest/

# importing the requests library 
import requests 
from bs4 import BeautifulSoup
import json

  
# api-endpoint 
URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
  
# db given here 
db = "pubmed"
term= 'gene' #search term(s) (PubMed Help)
retmax= 20  #number of citations to display if other than 20
sort = 'relevance'
retmode= "json" #display format (DocSum (default display, except for a single citation), abstract, MEDLINE, XML
filter_txt = 'simsearch2.ffrft
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'db':db,
          'term':term,
          'retmax':retmax,
          'sort':sort,
          'retmode':retmode,
          'filter':filter_txt  } 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 
  
  
# extracting latitude, longitude and formatted address  
# of the first matching location 
#title = data['results'][0]['title']
#longitude = data['results'][0]['geometry']['location']['lng'] 
#formatted_address = data['results'][0]['formatted_address'] 
  
# printing the output 
print(data)
#print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
#      %(latitude, longitude,formatted_address)) 
