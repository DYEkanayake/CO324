import requests
#a)
response = requests.get("https://api.github.com")
print("\n(a)(Response headers)\n")
print(response.headers)
print("\n(a)(Response body)\n")
print(response.text)  #character encoded
#print(response.json())
print("\n")

