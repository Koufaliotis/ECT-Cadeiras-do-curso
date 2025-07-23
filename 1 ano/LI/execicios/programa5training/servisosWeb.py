import requests
import cherrypy

f = requests.get("http://www.python.org")
print(f.status_code)
#print(f.text)
print(f.history)
print(f)

file = open("python.txt",'w')
lines = f.text.split("\n")
for line in lines:
    file.write(line)

#++++train a bit more here