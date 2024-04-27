# Этот файл отвечает за генерацию координат фигур

from typing import List, Tuple, Generator
import itertools
import math
from .polygon import Polygon

def gen_rectangle() -> Polygon:
    """
    Генерация прямоугольника.

    Returns:
    - List[Tuple[float, float]]: Список координат вершин прямоугольника.
    """
    x1, y1 = 0, 0
    width, height = 1, 1
    x2, y2 = x1 + width, y1
    x3, y3 = x1 + width, y1 + height
    x4, y4 = x1, y1 + height
    verts = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    return Polygon(verts)

def gen_triangle() -> Polygon:
    """
    Генерация треугольника.

    Returns:
    - List[Polygo[float, float]]: Список координат вершин треугольника.
    """
    x1, y1 = 0, 0
    x2, y2 = 1, 0
    x3, y3 = 0.5, math.sqrt(3) / 2
    verts = [(x1, y1), (x2, y2), (x3, y3)]
    return Polygon(verts)

#def gen_hexagon(last_hexagon_coords: List[float, float], diagonal=False) -> List[Tuple[float, float]]:
def gen_hexagon() -> Polygon:
    """
    Генерация правильного шестиугольника.

    Parameters:
    - last_hexagon_coords: Tuple[float, float] - Координаты предыдущего гексагона
    - diagonal: bool - Флаг, обозначающий генерировать ли следующий гексагон по диагонали вверх

    Returns:
    - List[Tuple[float, float]]: Список координат вершин шестиугольника.
    """
    vertices = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        x = math.cos(angle_rad)
        y = math.sin(angle_rad)
        vertices.append((x, y))
    return Polygon(vertices)

def generate_shapes() -> Generator[List[Polygon], None, None]:
    """
    Генерация различных фигур.

    Yields:
    - List[Tuple[float, float]]: Список координат вершин фигуры.
    """
    generators = [gen_triangle, gen_rectangle, gen_hexagon]
    for generator in itertools.cycle(generators):
        yield generator()