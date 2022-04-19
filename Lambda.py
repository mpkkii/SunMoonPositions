import folium
from PIL import Image
from math import sqrt, cos, sin, radians
from folium.plugins import SemiCircle



geo = [56.62468857, 47.89476849]
azimut = 245
head = 45
distance = 0.009364
sunRiseAzimut = 67.22
sunSetAzimut = 292.31

m = folium.Map(location= geo, zoom_start=12,)

"""получение радиуса горизонта"""
def radius_gorizont():
    d = 3.57 * sqrt(1.7) * 1000
    return float(d)


def geo_objekt(geo, azimut, distance=0.009364):
    geo_objekt = []
    end_lat = geo[0] + distance * radius_gorizont()/1000 * cos(radians(azimut))
    end_lon = geo[1] + distance * radius_gorizont()/1000 * sin(radians(azimut))
    geo_objekt.append(end_lat)
    geo_objekt.append(end_lon)
    return geo_objekt


"""Рисуем на карте точку наблюдения (нашу геопозицию)"""
folium.CircleMarker(
    location=geo,
    radius=6,
    popup="Ты тут",
    color="green",
    fill=True,
    fillcolor="green"
).add_to(m)


"""Рисуем на карте искомую точку"""
folium.CircleMarker(
    location=geo_objekt(geo, azimut),
    radius=2,
    popup="Искомая точка",
    color="red",
    fill=True,
    fillcolor="red"
).add_to(m)

"""Круг видимости горизонта"""
#folium.plugins.SemiCircle(location=geo, radius=radius_gorizont(), direction=azimut, arc=1 , color= "green" ).add_to(m)
folium.plugins.SemiCircle(location=geo, radius=radius_gorizont(), start_angle=sunRiseAzimut, stop_angle=sunSetAzimut , color= "red" ).add_to(m)

"""круг хз чего"""
folium.Circle(
    radius=5000,
    location=geo,
    color="black",
    fill=False,
).add_to(m)

# folium.Polygon(locations=[sunRiseGeo, sunDayHigh, sunSetGeo]).add_to(m)

# """линия на искомую точку и сама искомая точка"""
folium.PolyLine([geo, geo_objekt(geo,azimut)]).add_to(m)


"""можно смотреть координаты тыкая по карте"""
m.add_child(folium.LatLngPopup())

'''сохраняем карту в HTML'''
m.save("index.html")