import requests

response = requests.get('https://www.google.com')

#Alright, now what did the web server respond with? Let's take a look at the first 300 characters of the response
print(response.text[:300])

#
print(response.raw.read()[:100])


#
print(response.request.headers['Accept-Encoding'])