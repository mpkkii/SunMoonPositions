import folium
from html2image import Html2Image
from math import sqrt, cos, sin, radians, pi
from folium.plugins import SemiCircle, Draw



geo = [56.62468857, 47.89476849]
azimut = 200
head = 90
sunRiseAzimut = 67.22
sunSetAzimut = 292.31
radius_gorizont = 3.57 * sqrt(1.2) * 1000 # радиус внутреннего круга в метрах
radius_out = radius_gorizont*1.4 #радиус внешнего круга в метрах



m = folium.Map(location= geo, zoom_start=13,)

def distance(head:int, radius_gorizont:float, radius_out:float):
    x = ((head/90) * (radius_out-radius_gorizont))+ radius_gorizont
    print(x, 'в метрах')
    print(x/1000, 'в километрах')
    return x


def geo_objekt(geo:list, azimut:int, distance:float):    
    geo_objekt = []
    end_lat = geo[0] + distance * cos(radians(azimut)) / (radians(6371000))
    end_lon = geo[1] + distance * sin(radians(azimut)) / cos(radians(geo[0])) / (radians(6371000))
    geo_objekt.append(end_lat)
    geo_objekt.append(end_lon)
    return geo_objekt

distance = distance(head, radius_gorizont, radius_out)
geo_objekt = geo_objekt(geo, azimut, distance)

"""Рисуем на карте точку наблюдения (нашу геопозицию)"""
folium.CircleMarker(
    location=geo,
    radius=2,
    popup="Ты тут",
    color="green",
    fill=True,
    fillcolor="green"
).add_to(m)

"""Рисуем на карте искомую точку"""
folium.CircleMarker(
    location=geo_objekt,
    radius=2,
    popup="Искомая точка",
    color="red",
    fill=True,
    fillcolor="red"
).add_to(m)

"""Круг внешний - солце в зените head = 90"""
SemiCircle(location=geo, radius=radius_out, direction=azimut, arc=0 , color= "green" ).add_to(m)

"""Круг видимости горизонта он же внутренний круг"""
SemiCircle(location=geo, radius=radius_gorizont, start_angle=sunRiseAzimut, stop_angle=sunSetAzimut , color= "red" ).add_to(m)

"""линия на искомую точку и сама искомая точка"""
folium.PolyLine([geo, geo_objekt]).add_to(m)


"""можно смотреть координаты тыкая по карте"""
# m.add_child(folium.LatLngPopup())

"""Добавление рисования на карту"""
# Draw(
#     export=True,
#     filename='my_data.geojson',
#     position='topleft',
#     draw_options={'polyline': {'allowIntersection': False}},
#     edit_options={'poly': {'allowIntersection': False}}
# ).add_to(m)

'''сохраняем карту в HTML'''
m.save("index.html")

hti = Html2Image(
    browser_executable="C:\Program Files\Google\Chrome\Application\chrome.exe"
    )
hti.screenshot(html_file='index.html', save_as='index.png')
