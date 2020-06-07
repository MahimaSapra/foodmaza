import folium
import pandas
def map():
    html="templates/feed.html"
    data=pandas.read_csv("static/india.txt")
 #d=data.drop("accuracy",1)
    lat=list(data["latitude"])
    lon=list(data["longitude"])
#elev=list(data["ELEV"])
    name = list(data["place_name"])
#html = """<h4>Volcano information:</h4>
#Height: %s m
#"""
    print(lat)

#html = """
#Volcano name:<br>
#<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
#Height: %s m
#"""

    map=folium.Map(location=[21.1458,79.0882], tiles="stamentoner", zoom_start=4)
    fg=folium.FeatureGroup(name="My first map")
    for lt, ln , n in zip(lat,lon, name):
    #iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
        fg.add_child(folium.Marker(location=[lt,ln], popup=str(n),icon=folium.Icon(color='red')))
    #fill_color=color_producer(lt),color='grey', fill_opacity=0.7))
    fg.add_child(folium.GeoJson(data=(open('static/india_states.json','r',encoding='utf-8-sig').read())))
    map.add_child(fg)
    map.save("templates/map_one.html")
