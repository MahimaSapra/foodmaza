import folium
import pandas
data=pandas.read_csv("india.txt")
lat=list(data["latitude"])
lon=list(data["longitude"])
latitude=[]
longitude=[]
for item in lat:
    latitude.append(float(item))
for item in lon:
    longitude.append(float(item))


name = list(data["place_name"])
fg=folium.FeatureGroup("my map")
fg.add_child(folium.GeoJson(data=(open('D:/college project/templates/india_states.json','r',encoding='utf-8-sig').read())))

fg.add_child(folium.Marker(location=[ latitude,longitude ],popup=str(name)))
#fg.add_child(folium.Marker(location=[ 77.150650, 28.848450 ],popup="this is were taj mahal is located  "))

map=folium.Map(location=[],zoom_start=5)

map.add_child(fg)
map.save("feed.html")
