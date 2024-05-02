import numpy as np

from typing import Iterable
from matplotlib import patches

def tr_translate(polygons, dx, dy):
    """
    Параллельный перенос последовательности полигонов на заданное смещение.

    Параметры:
        - polygons: Iterable[patches.RegularPolygon] - последовательность полигонов.
        - dx: float - смещение по оси X.
        - dy: float - смещение по оси Y.

    Результат:
        Последовательность полигонов, сдвинутых на указанное смещение.
    """
    translated_polygons = []
    for polygon in polygons:
        x, y = polygon.xy
        polygon.xy = (x + dx, y + dy)
        translated_polygons.append(polygon)
    return translated_polygons

def tr_homothety(polygons, scale):
    """
    Гомотетия последовательности полигонов относительно их центров.

    Параметры:
        - polygons: Iterable[patches.RegularPolygon] - последовательность полигонов.
        - scale: float - коэффициент масштабирования.

    Результат:
        Последовательность полигонов, увеличенных или уменьшенных в scale раз.
    """
    homothetic_polygons = []
    for polygon in polygons:
        x, y = polygon.xy
        polygon.xy = (x * scale, y * scale)
        polygon.radius *= scale
        homothetic_polygons.append(polygon)
    return homothetic_polygons


def tr_symmetry(polygons, axis):
    """
    Симметрия последовательности полигонов относительно заданной оси.

    Параметры:
        - polygons: Iterable[patches.RegularPolygon] - последовательность полигонов.
        - axis: str - ось симметрии ('x' для оси X, 'y' для оси Y).

    Результат:
        Последовательность полигонов, отраженных относительно заданной оси.
    """
    symmetrical_polygons = []
    for polygon in polygons:
        x, y = polygon.xy
        if axis == 'x':
            polygon.xy = (x, -y)
        elif axis == 'y':
            polygon.xy = (-x, y)
        symmetrical_polygons.append(polygon)
    return symmetrical_polygons


def tr_rotate(polygons: Iterable[patches.RegularPolygon], angle):
    """
    Поворот последовательности полигонов на заданный угол.

    Параметры:
        - polygons: Iterable[patches.RegularPolygon] - последовательность полигонов.
        - angle: float - угол поворота в градусах.

    Результат:
        Последовательность полигонов, повернутых на указанный угол.
    """
    rotated_polygons = []
    for polygon in polygons:
        if isinstance(polygon, patches.RegularPolygon):
            polygon.orientation += np.deg2rad(angle)
        elif isinstance(polygon, patches.Rectangle):
            polygon.set_angle(np.deg2rad(angle))

        rotated_polygons.append(polygon)
    return rotated_polygons