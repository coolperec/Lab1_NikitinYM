import math
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs.txt", encoding="utf-8"),
        logging.StreamHandler()
    ]
)



def parse_side(value):
    try:
        number = float(value)

        if number <= 0:
            return None

        return number

    except Exception:
        return None



def get_triangle_type(a, b, c):

    if a + b <= c or a + c <= b or b + c <= a:
        return "не треугольник"

    if a == b == c:
        return "равносторонний"

    if a == b or a == c or b == c:
        return "равнобедренный"

    return "разносторонний"



def calculate_coordinates(a, b, c):


    ax = 0
    ay = 0

    B
    bx = c
    by = 0


    try:
        x = (b**2 + c**2 - a**2) / (2 * c)

        y_squared = b**2 - x**2

        if y_squared < 0:
            return [(-1, -1), (-1, -1), (-1, -1)]

        y = math.sqrt(y_squared)

        cx = x
        cy = y


        max_x = max(ax, bx, cx)
        max_y = max(ay, by, cy)

        scale_x = 90 / max_x if max_x != 0 else 1
        scale_y = 90 / max_y if max_y != 0 else 1

        scale = min(scale_x, scale_y)

        ax = int(ax * scale + 5)
        ay = int(ay * scale + 5)

        bx = int(bx * scale + 5)
        by = int(by * scale + 5)

        cx = int(cx * scale + 5)
        cy = int(cy * scale + 5)

        return [
            (ax, ay),
            (bx, by),
            (cx, cy)
        ]

    except Exception:
        logging.exception("Ошибка при вычислении координат")

        return [(-1, -1), (-1, -1), (-1, -1)]



def process_triangle(s1, s2, s3):

    try:
        a = parse_side(s1)
        b = parse_side(s2)
        c = parse_side(s3)


        if a is None or b is None or c is None:

            result_type = ""
            coords = [(-2, -2), (-2, -2), (-2, -2)]

            logging.error(
                f"Невалидный ввод | "
                f"Вход: {s1}, {s2}, {s3} | "
                f"Результат: {result_type}, {coords}"
            )

            return result_type, coords


        triangle_type = get_triangle_type(a, b, c)


        if triangle_type == "не треугольник":

            coords = [(-1, -1), (-1, -1), (-1, -1)]

            logging.error(
                f"Не треугольник | "
                f"Вход: {a}, {b}, {c} | "
                f"Результат: {triangle_type}, {coords}"
            )

            return triangle_type, coords


        coords = calculate_coordinates(a, b, c)

        logging.info(
            f"Успешный запрос | "
            f"Вход: {a}, {b}, {c} | "
            f"Результат: {triangle_type}, {coords}"
        )

        return triangle_type, coords

    except Exception:

        logging.exception(
            f"Критическая ошибка | "
            f"Вход: {s1}, {s2}, {s3}"
        )

        return "", [(-2, -2), (-2, -2), (-2, -2)]


if __name__ == "__main__":

    print("Введите стороны треугольника")

    side1 = input("Сторона A: ")
    side2 = input("Сторона B: ")
    side3 = input("Сторона C: ")

    triangle_type, coordinates = process_triangle(
        side1,
        side2,
        side3
    )

    print("\nРЕЗУЛЬТАТ")
    print("Тип треугольника:", triangle_type)
    print("Координаты:", coordinates)