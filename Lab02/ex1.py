from urllib import request
#a)
response = request.urlopen("http://eng.pdn.ac.lk")
print("\n(a)(Response code)\n")
print(response.getcode())
print("\n")
#print("Response:",response)
#print("\n")

#b)
#right way
print("(b)(The headers)\n")
with request.urlopen("http://eng.pdn.ac.lk") as s:
    print(s.headers.items())

#print(response.headers.items())
#print("\n")

#c)
print("\n(c)(The response body size)\n")
print("Without decoding:")
print(len(request.urlopen("http://eng.pdn.ac.lk").read()))#54123

print("\nAfter decoding:")
print(len(request.urlopen("http://eng.pdn.ac.lk").read().decode('utf-8'))) #54108

#d)
print("\n(d)(The body variable type)\n")
body=response.read()
print(type(body))

#f)
#print("\n(f)\n")
#print("For http://eng.pdn.ac.lk/nothere : (Gives error)")
#response_2 = request.urlopen("http://eng.pdn.ac.lk/nothere")
#print(response_2.getcode())
#print("\n")

#print("For http://unknown.pdn.ac.lk :(Gives error)")
#response_3 = request.urlopen("http://unknown.pdn.ac.lk")
#print(response_3.getcode())
#print("\n")



#g)
print("\n(g)\n")
response_4 = request.urlopen("https://ta.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AE%AE%E0%AF%8D")
body_4=response_4.read()
print(body_4) #printing the body

#(response_5 is as same request as response_4)
print("\n(h)\n")
response_5 = request.urlopen("https://ta.wikipedia.org/wiki/%E0%AE%9A%E0%AE%BF%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B3%E0%AE%AE%E0%AF%8D")
body_5=response_5.read().decode('utf-8')
print(body_5)
 

