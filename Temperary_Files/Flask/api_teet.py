import requests

r = requests.get("https://classroom.googleapis.com/$discovery/rest?version=v1")

print(help(r))