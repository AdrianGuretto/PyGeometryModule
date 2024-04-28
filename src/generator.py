# Этот файл отвечает за генерацию координат фигур

from typing import List, Tuple, Generator
import itertools
import math
from .polygon import Polygon

def gen_rectangle(last_rectangle: Polygon, diagonal_shift: bool = False) -> Polygon:
    """
    Генерация прямоугольника.

    Parameters:
    - last_rectangle: Polygon - Предыдущий прямоугольник.
    - diagonal_shift: bool - Смещать прямоугольник по диагонали вверх или нет.

    Returns:
    - Polygon: Многоугольник с координатами вершин прямоугольника.
    """
    # Получаем координаты предыдущего прямоугольника
    last_rectangle_coords = [(x, y) for x, y in last_rectangle.points]
    
    # Вычисляем максимальные значения x и y координат
    max_x = max(last_rectangle_coords, key=lambda point: point[0])[0]
    
    # Смещение от максимальных значений координат
    x_offset = max_x + 1
    y_offset = 0
    if diagonal_shift:
        y_offset += math.sqrt(3)  # Смещаемся на sqrt(3) вверх, чтобы треугольники были выше
    # Создаем вершины прямоугольника
    verts = [(0, 0), (1, 0), (1, 1), (0, 1)]
    
    # Смещаем прямоугольник относительно максимальных значений координат
    shifted_verts = [(x + x_offset, y + y_offset) for x, y in verts]
    
    return Polygon(shifted_verts)

def gen_triangle(edge_triangle: Polygon, diagonal_shift: bool = False) -> Polygon:
    """
    Генерация треугольника.

    Parameters:
    - edge_triangle: Polygon - Предыдущий треугольник.
    - diagonal_shift: bool - Смещать ли треугольник по диагонали вверх или нет.

    Returns:
    - Polygon: Многоугольник с координатами вершин треугольника.
    """
    # Получаем координаты предыдущего треугольника
    edge_triangle_coords = [(x, y) for x, y in edge_triangle.points]
    
    # Вычисляем максимальные значения x и y координат
    max_x = max(edge_triangle_coords, key=lambda point: point[0])[0]
    
    # Смещение от максимальных значений координат
    x_offset = max_x + 1
    y_offset = 0
    if diagonal_shift:
        y_offset += math.sqrt(3)  # Смещаемся на sqrt(3) вверх, чтобы треугольники были выше
    
    # Создаем вершины треугольника
    verts = [(0, 0), (1, 0), (0.5, math.sqrt(3) / 2)]
    
    # Смещаем треугольник относительно максимальных значений координат
    shifted_verts = [(x + x_offset, y + y_offset) for x, y in verts]
    
    return Polygon(shifted_verts)

#def gen_hexagon(last_hexagon_coords: List[float, float], diagonal=False) -> List[Tuple[float, float]]:
def gen_hexagon(last_hexagon_polygon: Polygon, diagonal_shift: bool = False) -> Polygon:
    """
    Генерация правильного шестиугольника.

    Parameters:
    - last_hexagon_coords: Tuple[float, float] - Координаты предыдущего гексагона
    - diagonal: bool - Флаг, обозначающий генерировать ли следующий гексагон по диагонали вверх

    Returns:
    - List[Polygon]: Список координат вершин шестиугольника.
    """
   # Получаем координаты предыдущего гексагона
    last_hexagon_coords = [(x, y) for x, y in last_hexagon_polygon.points]
    
    # Вычисляем максимальные значения x и y координат
    max_x = max(last_hexagon_coords, key=lambda point: point[0])[0]
    
    # Смещение от максимальных значений координат
    x_offset = max_x + 1
    y_offset = 0
    if diagonal_shift:
        y_offset += math.sqrt(3)  # Смещаемся на sqrt(3) вверх, чтобы гексагоны были выше
    
    # Создаем вершины шестиугольника
    vertices = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        x = math.cos(angle_rad) + x_offset
        y = math.sin(angle_rad) + y_offset
        vertices.append((x, y))
    
    return Polygon(vertices)

def generate_shapes(figure_type: str, shapes_count: int) -> Generator[List[Polygon], None, None]:
    """
    Генерация ряда фигур.

    Parameters:
    - figure_type: str - Тип фигуры, которую нужно сгенерировать в ряд ("треугольник", "прямоугольник", "шестиугольник")
    - shapes_count: int - Количество фигур, которые надо сгенерировать

    Yields:
    - List[Polygon]: Список координат вершин фигур.
    """
    figure_type = figure_type.lower()

    # Под каждый тип фигуры создаём генерирующий итератор
    if figure_type == "треугольник":
        last_triangle = Polygon([(0, 0), (3, 0), (3 / 2, 3 * math.sqrt(3) / 2)])
        for _ in range(shapes_count):
            yield gen_triangle(last_triangle)

    elif figure_type == "прямоугольник":
        last_rectangle = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])  # Начальный прямоугольник
        for _ in range(shapes_count):
            yield gen_rectangle(last_rectangle)

    elif figure_type == "шестиугольник":
        last_hexagon = Polygon([(0, 0), (1, 0), (1.5, math.sqrt(3) / 2), (1, math.sqrt(3)), (0, math.sqrt(3)), (-0.5, math.sqrt(3) / 2)])  # Начальный шестиугольник
        for _ in range(shapes_count):
            yield gen_hexagon(last_hexagon)