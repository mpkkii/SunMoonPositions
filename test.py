from turtle import color
import folium
import math

m = folium.Map(location=[37.0431575, -7.8449655], zoom_start=14)

tootip = "Célula em Olhão"

origin_point = [37.040893, -7.83197]

folium.CircleMarker(
    location=origin_point,
    radius=4,
    popup="célula",
    
).add_to(m)

length = .01
angle = 45

end_lat = origin_point[0] + length * math.sin(math.radians(angle))
end_lon = origin_point[1] + length * math.cos(math.radians(angle))

folium.PolyLine([origin_point, [end_lat, end_lon]]).add_to(m)

m.save("test.html")


def test_color_line():
    m = Map([22.5, 22.5], zoom_start=3)
    color_line = features.ColorLine(
        [[0, 0], [0, 45], [45, 45], [45, 0], [0, 0]],
        [0, 1, 2, 3],
        colormap=['b', 'g', 'y', 'r'],
        nb_steps=4,
        weight=10,
        opacity=1)
    m.add_child(color_line)
    m._repr_html_()
    
    
test_color_line()