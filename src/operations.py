from typing import List, Tuple
from .polygon import Polygon

def tr_translate(polygons: List[Polygon], vector: Tuple[float, float]) -> List[Polygon]:
    """
    Параллельный перенос последовательности полигонов на вектор.

    Parameters:
    - polygons: List[Polygon] - список полигонов для переноса.
    - vector: Tuple[float, float] - вектор переноса (dx, dy).

    Returns:
    - List[Polygon]: Список новых полигонов, полученных после переноса.
    """
    return [polygon.translate(vector) for polygon in polygons]

def tr_rotate(polygons: List[Polygon], angle: float) -> List[Polygon]:
    """
    Поворот последовательности полигонов на заданный угол.

    Parameters:
    - polygons: List[Polygon] - список полигонов для поворота.
    - angle: float - угол поворота в радианах.

    Returns:
    - List[Polygon]: Список новых полигонов, полученных после поворота.
    """
    return [polygon.rotate(angle) for polygon in polygons]

def tr_symmetry(polygons: List[Polygon], axis: Tuple[float, float]) -> List[Polygon]:
    """
    Отражение последовательности полигонов относительно заданной оси симметрии.

    Parameters:
    - polygons: List[Polygon] - список полигонов для отражения.
    - axis: Tuple[float, float] - координаты точки, через которую проходит ось симметрии.

    Returns:
    - List[Polygon]: Список новых полигонов, полученных после отражения.
    """
    return [polygon.symmetry(axis) for polygon in polygons]

def tr_homothety(polygons: List[Polygon], factor: float) -> List[Polygon]:
    """
    Гомотетия последовательности полигонов относительно начала координат.

    Parameters:
    - polygons: List[Polygon] - список полигонов для гомотетии.
    - factor: float - коэффициент гомотетии.

    Returns:
    - List[Polygon]: Список новых полигонов, полученных после гомотетии.
    """
    return [polygon.homothety(factor) for polygon in polygons]

def apply_operation(polygons: List[Polygon], operation, *args) -> List[Polygon]:
    """
    Применение операции к последовательности полигонов.

    Parameters:
    - polygons: List[Polygon] - список полигонов для применения операции.
    - operation: function - функция операции.
    - args: дополнительные аргументы операции.

    Returns:
    - List[Polygon]: Список новых полигонов, полученных после применения операции.
    """
    return operation(polygons, *args)
