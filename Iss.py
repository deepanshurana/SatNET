import urllib.request
import json
import turtle


url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
res = json.loads(response.read().decode('utf-8'))
t = res['people']
print('total people in spacestation: ',res['number'])
for i in t:
    print(i['name'],"in",i['craft'])


iss_url = 'http://api.open-notify.org/iss-now.json'
response2 = urllib.request.urlopen(iss_url)
res2 = json.loads(response2.read().decode('utf-8'))
t2 = res2['iss_position']
print(t2['latitude'])
print(t2['longitude'])

Scr = turtle.Screen()
image = "/Users/deepanshurana/Downloads/world-map.gif"
Scr.bgpic(image)
Scr.setup(720,360)
turtle.mainloop()

