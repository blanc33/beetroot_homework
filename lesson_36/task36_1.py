import requests
response = requests.get("https://en.wikipedia.org/robots.txt")
test = response.text
print("robots.txt for http://www.wikipedia.org/")
print("===================================================")
print(test)
