# Этот файл нужен для генерации фигур на нужных координатах и под нужным углом

import matplotlib.patches as patches
from matplotlib.axes import Axes
from typing import Generator, List
import itertools
import numpy as np

import numpy as np

def calculate_offset(angle: float, side_length: float) -> tuple[float, float]:
    """
    Рассчитывает смещение по осям X и Y на основе угла.

    Параметры:
        - angle: float - угол в градусах.
        - side_length: float - длина стороны треугольника.

    Результат:
        Кортеж смещения по осям X и Y.
    """
    # Преобразование угла в радианы
    angle_rad = np.deg2rad(angle)

    # Вычисление смещения по оси X и Y
    dx = side_length * np.cos(angle_rad)
    dy = side_length * np.sin(angle_rad)

    return dx, dy


def gen_rect(last_square: patches.Rectangle, angle: int = 0, max_depth: int = 10) -> Generator[patches.Rectangle, None, None]:
    """
    Получить генератор для объектов прямоугольника.

    Параметры:
        - last_square: patches.Rectangle - объект последнего прямоугольника.
        - angle: int - угол, под которым генерировать следующий объект.
        - max_depth: int - максимальная глубина рекурсии.

    Результат:
        Генератор объектов прямоугольника с разумным отступом.
    """
    if max_depth <= 0:
        return

    rect_height = 3
    rect_width = 4

    # Получить координаты центра последнего прямоугольника
    center_x, center_y = last_square.get_xy()

    offset_x, offset_y = calculate_offset(angle, rect_width)

    # Вычислить координаты левого нижнего угла нового прямоугольника
    new_x = center_x + offset_x + (rect_width * 0.2 if angle > 0 else 0)
    new_y = center_y + offset_y + (rect_width * 0.2 if angle > 0 else 0)

    # Создать новый объект прямоугольника
    new_square = patches.Rectangle(xy=(new_x, new_y),
                                 width=rect_width, height=rect_height,
                                 color='green', alpha=0.4, angle=angle)

    # Сгенерировать следующий прямоугольник
    yield new_square

    # Рекурсивно генерировать последующие прямоугольники
    for rect in gen_rect(new_square, angle, max_depth - 1):
        yield rect

def gen_triangle(last_triangle: patches.RegularPolygon, angle: int = 0, max_depth: int = 10) -> Generator[patches.RegularPolygon, None, None]:
    """
    Получить генератор для объектов треугольника.

    Параметры:
        - last_triangle: patches.RegularPolygon - объект последнего треугольника.
        - angle: int - угол, под которым генерировать следующий объект.

    Результат:
        Генератор объектов треугольника с разумным отступом.
    """
    if max_depth <= 0:
        return
        
    side_len = 4

    # Получить координаты центра последнего треугольника
    center_x, center_y = last_triangle.xy

    # Вычислить новый угол с учетом поворота
    new_angle = (angle + 120) % 360

    # Вычислить смещение по оси X и Y в зависимости от угла
    offset_x, offset_y = calculate_offset(angle, side_len)

    # Вычислить координаты центра нового треугольника
    new_x = center_x + offset_x + (side_len * 0.3 if angle > 0 else 0)
    new_y = center_y + offset_y + (side_len * 0.3 if angle > 0 else 0)

    # Создать новый объект треугольника
    new_triangle = patches.RegularPolygon(xy=(new_x, new_y), numVertices=3, radius=side_len/3,
                                          orientation=new_angle, color='blue', alpha=0.4)

    # Сгенерировать следующий треугольник
    yield new_triangle

    # Рекурсивно генерировать последующие треугольники
    for triangle in gen_triangle(new_triangle, angle, max_depth - 1):
        yield triangle


def gen_hexagons(last_hex: patches.RegularPolygon, angle=0, max_depth:int=10) -> Generator[patches.RegularPolygon, None, None]:
    """
    Получить генератор для объектов шестиугольника.

    Параметры:
        - last_triangle: patches.RegularPolygon - объект последнего шестиугольника
        - angle: int - угол, под которым генерировать следующий объект

    Результат:
        Генератор объектов шестиугольником с разумным отступом.
    """
    axis_num = 6
    size_num = 2

def gen_hexagon(last_hex: patches.RegularPolygon, angle: int = 0, max_depth: int = 10) -> Generator[patches.RegularPolygon, None, None]:
    """
    Получить генератор для объектов шестиугольника.

    Параметры:
        - last_hex: patches.RegularPolygon - объект последнего шестиугольника.
        - angle: int - угол, под которым генерировать следующий объект.
        - max_depth: int - максимальная глубина рекурсии.

    Результат:
        Генератор объектов шестиугольника с разумным отступом.
    """
    if max_depth <= 0:
        return

    axis_num = 6
    size_num = 2

    # Получить координаты центра последнего шестиугольника
    center_x, center_y = last_hex.xy

    # Вычислить новый угол с учетом поворота
    new_angle = (angle + 360 / axis_num) % 360

    # Вычислить смещение по оси X и Y
    offset_x, offset_y = calculate_offset(angle, size_num)

    # Вычислить координаты центра нового шестиугольника
    new_x = center_x + offset_x
    new_y = center_y + offset_y

    # Создать новый объект шестиугольника
    new_hex = patches.RegularPolygon(xy=(new_x, new_y), numVertices=axis_num, radius=size_num/3,
                                     orientation=new_angle, color='orange', alpha=0.4)

    # Сгенерировать следующий шестиугольник
    yield new_hex

    # Рекурсивно генерировать последующие шестиугольники
    for hexagon in gen_hexagon(new_hex, angle, max_depth - 1):
        yield hexagon


def gen_polygon(last_poly: patches.RegularPolygon, axis_num: int, angle: int = 0) -> Generator[patches.RegularPolygon, None, None]:
    """
    Получить генератор для объектов полигона.

    Параметры:
        - last_poly: patches.RegularPolygon - объект последнего полигона.
        - axis_num: int - количество углов у полигона.
        - angle: int - угол, под которым генерировать следующий объект.

    Результат:
        Генератор объектов полигонов с разумным отступом.
    """
    # Получить координаты центра последнего полигона
    center_x, center_y = last_poly.xy

    # Вычислить новый угол с учетом поворота
    new_angle = (angle + 360 / axis_num) % 360

    # Вычислить смещение по оси X и Y
    offset_x, offset_y = calculate_offset(angle, 2)

    # Вычислить координаты центра нового полигона
    new_x = center_x + offset_x
    new_y = center_y + offset_y

    # Создать новый объект полигона
    new_poly = patches.RegularPolygon(xy=(new_x, new_y), numVertices=axis_num, radius=2/3,
                                      orientation=new_angle, color='green', alpha=0.4)

    # Сгенерировать следующий полигон
    yield new_poly

    # Рекурсивно генерировать последующие полигоны
    for polygon in gen_polygon(new_poly, axis_num, angle):
        yield polygon
