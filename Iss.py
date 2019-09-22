import urllib.request
import json
import turtle
#json file for people present in the satellite
url = 'http://api.open-notify.org/astros.json' # url fetching of the data,
response = urllib.request.urlopen(url)
res = json.loads(response.read().decode('utf-8'))
t = res['people']
print('total people in spacestation: ',res['number'])
for i in t:
    print(i['name'],"in",i['craft'])

# json file for satellite information
iss_url = 'http://api.open-notify.org/iss-now.json'
response2 = urllib.request.urlopen(iss_url)
res2 = json.loads(response2.read().decode('utf-8'))
t2 = res2['iss_position']
longitude = t2['longitude']
latitude = t2['latitude']
# print('LONGITUDE: ',longitude)
# print('LATITUDE: ',latitude)

Scr = turtle.Screen()
image = "wm.gif" # gif file for world map; taken from nasa website
Scr.bgpic(image)
# screen setup for dimensions. Must be same as of GIF file.

Scr.setup(1200,600)

# For mapping turtle co-ordinates to gif map co-ordinates, we can use setworldcoordinates() method

Scr.setworldcoordinates(-180,-90,180,90)
# Every thing is done, now initialise the turtle. using turtle.Turtle()

stl = turtle.Turtle()

stl.shape("classic")
# for orienting the shape of the turtle, use .setheading(angle_value).
stl.setheading(270)
# for enhancing the color schema of the turtle, use .color() method.
stl.color('red', 'blue')

stl.up()  # no draw when moving.if not, the pen will trace a line from the origin i.e. the center of the screen
# Everything is ready. Now map satellite coordinates with the turtle coordinates.
stl.goto(float(longitude),float(latitude))
print('--'*40)
# print longitude and latitude
print('LONGITUDE: ',longitude)
print('LATITUDE: ',latitude)

# for never closing screen, use .mainloop()
turtle.mainloop()


