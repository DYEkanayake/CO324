import requests
#b)
response = requests.get("https://api.github.com/users/DYEkanayake")
print("\n(b)(Response headers)\n")
print(response.headers)
print("\n(b)(Response body)\n")
print(response.text)
print("\n")