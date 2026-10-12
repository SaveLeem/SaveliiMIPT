from random import randint

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""

class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    image = None
    """Изображение планеты"""
    
    
def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        dx = obj.x - body.x
        dy = obj.y - body.y
        r_sqr = dx ** 2 + dy ** 2
        r = r_sqr ** 0.5
        F = gravitational_constant * body.m * obj.m / r_sqr
        body.Fx += F * dx / r
        body.Fy += F * dy / r


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.Vx += ax * dt
    body.Vy += ay * dt
    body.x += body.Vx * dt
    body.y += body.Vy * dt


def angular_velocity(body, star):
    """Угловая скорость радиус-вектора тела относительно звезды (рад/с).

    omega = (rx * Vy - ry * Vx) / r^2, где (rx, ry) — вектор от звезды к телу,
    (Vx, Vy) — скорость тела относительно звезды.
    """

    rx = body.x - star.x
    ry = body.y - star.y
    vx = body.Vx - star.Vx
    vy = body.Vy - star.Vy
    return (rx * vy - ry * vx) / (rx ** 2 + ry ** 2)


def swept_area(body, star, dt):
    """Площадь, которую радиус-вектор тела заметает за один шаг dt.

    Один шаг численного интегрирования формулы S = 1/2 * integral(r^2 * omega dt):
    dS = 1/2 * r^2 * omega * dt.
    Сумма таких значений за все шаги интервала даёт площадь за интервал.
    """

    r_sqr = (body.x - star.x) ** 2 + (body.y - star.y) ** 2
    return 0.5 * r_sqr * abs(angular_velocity(body, star)) * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
