import folium 

# folium builds on the data wrangling strengths of python ecosystem 
# and the mapping strngths of the leaflet.js library
# Manipulate your data in Python
# visualize it in a leaflet map via folium 

#create a map object 
m = folium.Map(location=[40.761532, -73.831108], zoom_start=12)

# Generate Map
m.save('map.html')
