from typing import List, Tuple
import requests

def github_superstars(orgnanization: str) -> List[Tuple]:
    arr=orgnanization.split("/")
    orgnanization_name=arr[len(arr)-1] #To get the organization name

    url="https://api.github.com/orgs/"+orgnanization_name+"/members" #url to get members
    with requests.Session() as session:
        #response = session.get("https://api.github.com/orgs/cepdnaclk/members")
        response = session.get(url)
        members=[]#list of members
        data=response.json() #Gives a list of dictionaries
        for k in data:
            #just members.append(k["login"]) is not used in case of response being not received
            try:
                members.append(k["login"]) #login is the key to memeber username
            except:
                print("Exception error occurred")
   
    
    mem_repo=[]#(list of lists) member and his repository of highest starts and star count
    final_list=[]
   
    for j in members:
        #Obtaining repos
        url_2="https://api.github.com/users/"+j+"/repos"
        pages={"page":1,"per_page":100}  #To get all or majority of repos(for 100 pages), this parameter is set
        response_2=session.get(url_2,params=pages)
        repo_stars=dict()#repo url and star count(key=url, value=star count)
        data_2=response_2.json() #Gives a list of dictionaries
        for l in data_2:
            repo_stars[l["url"]]=l["stargazers_count"]
          
        mem_repo.append([j,max(repo_stars,key=repo_stars.get),max(repo_stars.values())])  #list of (member, repo with max count,max star count) appended to max_repo
        final_list=sorted(mem_repo,key=lambda x:x[2],reverse=True)#sorting(descending)
               
    return final_list#returns the sorted list

print("(2) part a:\n")
print(github_superstars("https://github.com/cepdnaclk"))
