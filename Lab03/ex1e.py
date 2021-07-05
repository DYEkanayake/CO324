import requests
import json

#e)

with requests.Session() as session:
    #Set the headers for authentication
    session.headers['Authorization'] = 'token 6681ff32377e78ecd43ac3a1de8495709be35aa4'
    url = 'https://api.github.com/user/repos'
    data = {'name':'test', 'description':'some test repo'}  
    
    #HTTP POST method
    rep = session.post(url,data = json.dumps(data))
    print("\n(b)(Response headers)\n")
    print(rep.headers)
    print("\n(b)(Response body)\n")
    print(rep.text)
    print("\n")
    
    