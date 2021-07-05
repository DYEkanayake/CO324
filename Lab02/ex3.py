from urllib import request
import requests
from json import loads
from urllib import parse
from typing import List, Dict
import json

def ddg_query(url: str, nr_results: int) -> List[str]:
    
    query=parse.quote(url)
    url="https://www.duckduckgo.com/?q="+query+"&format=json&pretty=1"
    response=request.urlopen(url)
        
    body=response.read()
       
    #parsing the json body 
    data=json.loads(body)#python dictionary
       
    a=[] #list for urls
    keys_Results=data["Results"]
    keys_relatedTopics=data["RelatedTopics"]
        
    for k in keys_Results:
        a.append(k["FirstURL"])
    
    for k in keys_relatedTopics:
        a.append(k["FirstURL"])
        
    response.close()
   
    return a[0:nr_results]
    
#3)part b   
def spider_metadata(urls: List[str]) -> List[List]:
    #get the headers for each url then pull the header out
    r=[]
    for k in urls:
        with request.urlopen(k) as s:
            r.append(s.headers.items())
                
    return r #List of headers
    
#3)part c   
def spider_metadata_2(urls: List[str]) -> List[List]: 
    #use HEAD method
    r=[]
    for k in urls:
        r.append((requests.head(k)).headers)
    
    return r #List of headers
    
print("(3)a")
print(ddg_query("University of Peradeniya",1))
print("\n")

a=["https://www.duckduckgo.com/?q=University+of+Peradeniya&format=json&pretty=1","https://ta.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AE%AE%E0%AF%8D"]
print("(3)b")
print(spider_metadata(a))

print("\n(3)c")
print(spider_metadata_2(a)) 

  
   