import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MatPoly
from typing import List, Tuple
from .polygon import Polygon

def visualize(polygons: List[Polygon]):
    """
    Визуализация последовательности полигонов.

    Parameters:
    - polygons: List[Polygon] - список полигонов для визуализации.
    """
    fig, ax = plt.subplots()
    for polygon in polygons:
        points = polygon.points
        x, y = zip(*points)  # Разделяем координаты x и y
        ax.add_patch(MatPoly(points, closed=True))
    ax.autoscale_view()
    plt.axis('equal')  # Сохраняем пропорции осей
    plt.show()