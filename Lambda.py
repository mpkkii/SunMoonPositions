
from cmath import sqrt
from turtle import fillcolor
import folium
from PIL import Image
from math import sqrt, cos, sin, radians
from folium.plugins import SemiCircle



geo = [56.62468857, 47.89476849]
azimut = 180
head = 45
distance = 0.45091523185115
sunRiseAzimut = 67.22
sunSetAzimut = 292.31

# geo_objekt = [56.62692835, 47.94006479575362]
# sunRiseGeo = [56.61795653688834, 47.76909006818436]
# sunSetGeo = [56.63448190718452, 47.952252753240984]
# sunDayHigh= [56.64713072839149, 47.869168648679214]
m = folium.Map(location= geo, zoom_start=12,)

"""получение радиуса горионта"""
def radius_gorizont():
    d = 3.57 * sqrt(1.70) *1000
    #r = d/2*1000
    print(d)
    return float(d)


def geo_objekt(geo,azimut):
    geo_objekt = []
    end_lat = geo[0] + 0.009364 * radius_gorizont()/1000 * cos(radians(azimut))
    end_lon = geo[1] + 0.009364 * radius_gorizont()/1000 * sin(radians(azimut))
    geo_objekt.append(end_lat)
    geo_objekt.append(end_lon)
    print(geo_objekt)
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


# """Рисуем на карте искомую точку"""
# folium.CircleMarker(
#     location=geo_objekt,
#     radius=6,
#     popup="Искомая точка",
#     color="red",
#     fill=True,
#     fillcolor="red"
# ).add_to(m)

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