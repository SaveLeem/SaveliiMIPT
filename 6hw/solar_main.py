import tkinter
from tkinter.filedialog import *
from solar_visuals import * 
from solar_physics import *
from solar_read import *


perform_execution = False
"""Флаг цикличности выполнения расчёта"""

physical_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

displayed_time = None
"""Отображаемое на экране время.
Тип: переменная tkinter"""

time_step = None
"""Шаг по времени при моделировании.
Тип: float"""

space_objects = []
"""Список космических объектов."""

tracked_index = 0
"""Номер отслеживаемой планеты среди всех планет списка"""

swept_area_now = 0
"""Площадь, заметённая в текущем (незавершённом) интервале, м^2"""

swept_area_last = None
"""Площадь, заметённая в последнем завершённом интервале, м^2"""

interval_elapsed = 0
"""Сколько секунд прошло в текущем интервале"""

interval_t = None
"""Длина интервала в сутках. Тип: переменная tkinter"""

area_text = None
"""Текст над холстом с площадью. Тип: переменная tkinter"""


def get_planets():
    """Возвращает список всех планет."""
    return [obj for obj in space_objects if obj.type == 'planet']


def get_star():
    """Возвращает первую звезду из списка (или None)."""
    for obj in space_objects:
        if obj.type == 'star':
            return obj
    return None


def show_area():
    """Обновляет текст с площадью над холстом."""
    planets = get_planets()
    if not planets:
        area_text.set("Нет планет. Загрузите файл.")
        return
    body = planets[tracked_index]
    text = "Планета: %s | S в текущем интервале: %.4e м^2" % (body.color, swept_area_now)
    if swept_area_last is not None:
        text += " | в прошлом интервале: %.4e м^2" % swept_area_last
    area_text.set(text)


def highlight_tracked():
    """Обводит белым выбранную планету."""
    for i, planet in enumerate(get_planets()):
        if i == tracked_index:
            space.itemconfig(planet.image, outline="white", width=2)
        else:
            space.itemconfig(planet.image, outline="black", width=1)


def reset_tracking(index=0):
    """Сбрасывает накопленную площадь и выбирает планету с номером index."""
    global tracked_index, swept_area_now, swept_area_last, interval_elapsed
    tracked_index = index
    swept_area_now = 0
    swept_area_last = None
    interval_elapsed = 0
    highlight_tracked()
    show_area()


def select_next_planet():
    """Обработчик кнопки Next planet: переключает на следующую планету."""
    planets = get_planets()
    if not planets:
        return
    reset_tracking((tracked_index + 1) % len(planets))


def update_swept_area(dt):
    """Добавляет площадь за шаг dt к накопленной и закрывает интервал,
    когда он закончился."""
    global swept_area_now, swept_area_last, interval_elapsed
    planets = get_planets()
    star = get_star()
    if not planets or star is None:
        return
    body = planets[tracked_index]
    swept_area_now += swept_area(body, star, dt)
    interval_elapsed += dt
    if interval_elapsed >= interval_t.get() * 86400:
        swept_area_last = swept_area_now
        swept_area_now = 0
        interval_elapsed = 0
    show_area()


def execution():
    """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    global physical_time
    global displayed_time
    recalculate_space_objects_positions(space_objects, time_step.get())
    for body in space_objects:
        update_object_position(space, body)
    update_swept_area(time_step.get())
    physical_time += time_step.get()
    displayed_time.set("%.1f" % physical_time + " seconds gone")

    if perform_execution:
        space.after(101 - int(time_speed.get()), execution)


def start_execution():
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = True
    start_button['text'] = "Pause"
    start_button['command'] = stop_execution

    #from record import start
    #start(space, 100, __file__)

    execution()
    print('Started execution...')


def stop_execution():
    """Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = False
    start_button['text'] = "Start"
    start_button['command'] = start_execution
    print('Paused execution.')


def open_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    global perform_execution
    perform_execution = False
    for obj in space_objects:
        space.delete(obj.image)  # удаление старых изображений планет
    in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
    space_objects = read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    calculate_scale_factor(max_distance)

    for obj in space_objects:
        if obj.type == 'star':
            create_star_image(space, obj)
        elif obj.type == 'planet':
            create_planet_image(space, obj)
        else:
            raise AssertionError()

    reset_tracking()


def save_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    out_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
    write_space_objects_data_to_file(out_filename, space_objects)


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    global physical_time
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button
    global interval_t
    global area_text

    print('Modelling started!')
    physical_time = 0

    root = tkinter.Tk()
    # космическое пространство отображается на холсте типа Canvas
    space = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
    space.pack(side=tkinter.TOP)

    # строка с площадью над холстом
    area_text = tkinter.StringVar()
    area_text.set("Загрузите файл (Open file...)")
    area_label = tkinter.Label(root, textvariable=area_text)
    area_label.pack(side=tkinter.TOP, before=space)

    # нижняя панель с кнопками
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)

    start_button = tkinter.Button(frame, text="Start", command=start_execution, width=6)
    start_button.pack(side=tkinter.LEFT)

    time_step = tkinter.DoubleVar()
    time_step.set(1)
    time_step_entry = tkinter.Entry(frame, textvariable=time_step)
    time_step_entry.pack(side=tkinter.LEFT)

    time_speed = tkinter.DoubleVar()
    scale = tkinter.Scale(frame, variable=time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)

    load_file_button = tkinter.Button(frame, text="Open file...", command=open_file_dialog)
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Save to file...", command=save_file_dialog)
    save_file_button.pack(side=tkinter.LEFT)

    next_planet_button = tkinter.Button(frame, text="Next planet", command=select_next_planet)
    next_planet_button.pack(side=tkinter.LEFT)

    interval_t = tkinter.DoubleVar()
    interval_t.set(30)
    interval_entry = tkinter.Entry(frame, textvariable=interval_t, width=5)
    interval_entry.pack(side=tkinter.LEFT)
    interval_label = tkinter.Label(frame, text="сут")
    interval_label.pack(side=tkinter.LEFT)

    displayed_time = tkinter.StringVar()
    displayed_time.set(str(physical_time) + " seconds gone")
    time_label = tkinter.Label(frame, textvariable=displayed_time, width=30)
    time_label.pack(side=tkinter.RIGHT)

    root.mainloop()
    print('Modelling finished!')

if __name__ == "__main__":
    main()
