from ex2a import *

#winner is the top repo
winner=github_superstars("https://github.com/cepdnaclk")

repo_url=winner[0][1] 
#print(repo_url)

with requests.Session() as session:
    session.headers['Authorization'] = 'token 6681ff32377e78ecd43ac3a1de8495709be35aa4'  #Authentication   
    
    url=repo_url+"/subscription" #This url corresponds to watching the repo
    #Watch repo
    rep = session.put(url) # HTTP PUT method
    
    print("\n(2) part a:\n")   
    print("\n(b)(Response headers)\n")
    print(rep.headers)
    print("\n(b)(Response body)\n")
    print(rep.text)
    print("\n")
    
    
    
