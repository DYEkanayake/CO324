from urllib import request
from urllib import parse
import json

with request.urlopen("https://www.duckduckgo.com/?q=University+of+Peradeniya") as query:
    headers = query.headers.items()
    body = query.read()
    #print(headers)
    #print(body)

print("\n2)i\n")
with request.urlopen("https://www.duckduckgo.com/?q=University+of+Peradeniya&format=json&pretty=1") as query_2:
    headers_2 = query_2.headers.items()
    body_2 = query_2.read()
    #print(headers_2)
    #print(body_2)

#print("\n2)j\n")
with request.urlopen("https://www.duckduckgo.com/?q=Rocco's+basilisk&format=json&pretty=1") as response_3:
    headers_3 = response_3.headers.items()
    body_3=response_3.read()#"Results" : [](no results)
    #print(headers_3)
    #print(body_3)


print("\n2)l\n")
query_3=parse.quote("දුල්මිණී")
#print(query_3)
url="https://www.duckduckgo.com/?q="+query_3
with  request.urlopen(url) as response_4 :
    headers_4 = response_4.headers.items()
    body_4=response_4.read().decode('utf-8')
    print(body_4)

