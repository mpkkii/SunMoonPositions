
from cmath import sqrt
from turtle import fillcolor
import folium
from PIL import Image
from math import sqrt



geo = [56.636720806323076, 47.83301060816586]
geo_objekt = [56.62692835, 47.94006479575362]
sunRiseGeo = [56.61795653688834, 47.76909006818436]
sunSetGeo = [56.63448190718452, 47.952252753240984]
sunDayHigh= [56.64713072839149, 47.869168648679214]
m = folium.Map(location= geo, zoom_start=12,)


def radius_gorizont():
    d = 3.57 * sqrt(1.75)
    r = d/2
    print(r)
    return r

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
    location=geo_objekt,
    radius=6,
    popup="Искомая точка",
    color="red",
    fill=True,
    fillcolor="red"
).add_to(m)

"""Круг видимости горизонта"""
folium.Circle(
    radius=radius_gorizont()*1700,
    location=geo,
    color="red",
    fill=False,
).add_to(m)

"""круг хз чего"""
folium.Circle(
    radius=5000,
    location=geo,
    color="black",
    fill=False,
).add_to(m)

# folium.Polygon(locations=[sunRiseGeo, sunDayHigh, sunSetGeo]).add_to(m)


"""линия на искомую точку и сама искомая точка"""
folium.PolyLine([geo, geo_objekt]).add_to(m)


"""можно смотреть координаты тыкая по карте"""
m.add_child(folium.LatLngPopup())

'''сохраняем карту в HTML'''
m.save("index.html")