# Лабораторная работа №1

# На плоскости дано множество точек.
# Найти такой треугольник с вершинами в этих точках, у которого выстоа имеет
# максимальную длинну. Для каждого треугольника берётся та из трёх высот,
# длина которых максимальна. Сделать вывод в графическом режиме.

from tkinter import *
from tkinter import messagebox
from math import *
from geometry import *

canvas_x, canvas_y = 800, 500
bg_color_main = "white"
main_font = "Arial 11"
entry_font = "Arial 8"
title_font = "Arial 14"
point_width = 8
point_width_2 = 12

window_title_text = "Лабораторная работа №1"
point_title_text = "Введите точки:"
canvas_title_text = "Геометрическое решение:"
calculate_text = "Получить решение"

task_title = 'Условие задачи'
task_text = """32) На плоскости дано множество точек. \
Найти такой треугольник с вершинами в этих точках, у которого выстоа имеет максимальную длинну. \
Для каждого треугольника берётся та из трёх высот, длина которых максимальна. \
Сделать вывод в графическом режиме. """

point_format_title = 'Формат ввода точек'
point_format_text = """Координаты имеют вещественный тип. 
Формат ввода точки A(x,y) в декартовой системе координат:\n
 x\ty"""

error_title = "Ошибка ввода"

error_point = [0] * 4
error_point[1] = "Некорректный формат ввода точек"
error_point[2] = "Точки не могут совпадать"
error_point[3] = "Все точки образуют несуществующие треугольники. " \
                 "Решения не было найдено."


def add_point_entry():
    global point_entry_list
    temp_frame = Frame(point_frame, bg=bg_color_main)

    temp_frame.x = StringVar(temp_frame, value='0.0')
    temp_frame.y = StringVar(temp_frame, value='0.0')

    x_entry = Entry(temp_frame, bg=bg_color_main, width=point_width_2,
                    font=entry_font, textvariable=temp_frame.x)
    y_entry = Entry(temp_frame, bg=bg_color_main, width=point_width_2,
                    font=entry_font, textvariable=temp_frame.y)
    del_button = Button(temp_frame, text='-', width=3, font=entry_font,
                        command=lambda obj=temp_frame: delete_point_entry(obj))

    x_entry.grid(row=0, column=0, sticky="WE")
    y_entry.grid(row=0, column=1, sticky="WE")
    del_button.grid(row=0, column=2, padx=5, sticky="WE")

    temp_frame.pack(pady=1)
    point_entry_list.append(temp_frame)


def delete_point_entry(frame):
    global point_entry_list
    if len(point_entry_list) <= 3:
        return False
    point_entry_list.remove(frame)
    frame.pack_forget()


def clear_point_entry():
    global point_entry_list
    canvas.delete(ALL)
    add_point_entry()
    add_point_entry()
    add_point_entry()
    for i in range(len(point_entry_list) - 3):
        delete_point_entry(point_entry_list[0])



def adp_x(x):
    return (x - x_min)/(x_max - x_min) * canvas_x
def adp_y(y):
    return (y_max - y)/(y_max - y_min) * canvas_y
def adp_xy(A):
    return (A['x'] - x_min) / (x_max - x_min) * canvas_x,\
           (y_max - A['y']) / (y_max - y_min) * canvas_y
def text_xy(A, space):
    x, y = adp_xy(A)
    # x += copysign(space, x - canvas_x / 2)
    # y += copysign(space, y - canvas_y / 2)
    x += (x - canvas_x / 2) * 0.1 + space
    if x < 40: x = 40
    y += (y - canvas_y / 2) * 0.1 + space
    if y < 20: y = 20
    return x, y


# Find field borders
def define_borders(A, B, C, D):
    global x_min, x_max, y_min, y_max
    print(A, B, C, D)
    x_min = min(A['x'], B['x'], C['x'], D['x'])
    x_max = max(A['x'], B['x'], C['x'], D['x'])
    y_min = min(A['y'], B['y'], C['y'], D['y'])
    y_max = max(A['y'], B['y'], C['y'], D['y'])

    x_min -= (x_max - x_min) / 10
    x_max += (x_max - x_min) / 10
    y_min -= (y_max - y_min) / 10
    y_max += (y_max - y_min) / 10

    kx = (x_max - x_min) / canvas_x
    ky = (y_max - y_min) / canvas_y
    if (kx > ky):
        y_min -= (kx - ky) * canvas_y / 2
        y_max += (kx - ky) * canvas_y / 2
    else:
        x_min -= (ky - kx) * canvas_x / 2
        x_max += (ky - kx) * canvas_x / 2


def get_points(entry_list):
    points = []
    for i in entry_list:
        points.append({})
        try:
            points[-1]['x'] = float(i.x.get())
            points[-1]['y'] = float(i.y.get())
        except:
            return points, 1, [len(points) - 1]

        for j in range(len(points) - 1):
            if points[-1] == points[j]:
                return points, 2, [len(points) - 1, j]
            """
            for k in range(j + 1, len(points) - 1):
                if not is_correct_triangle(points[-1], points[j], points[k]):
                    return points, 3, [len(points) - 1, j, k]
            """
    return points, 0, []


def show_solution():
    canvas.delete(ALL)
    global x_min, y_min
    global x_max, y_max

    for i in point_entry_list:
        i['bg'] = bg_color_main

    # Считывание точек
    points, err_code, err_entries = get_points(point_entry_list)
    if err_code:
        if err_code == 1:
            point_entry_list[err_entries[0]]['bg'] = '#eb3b5a'
        elif err_code == 2:
            point_entry_list[err_entries[0]]['bg'] = '#f7b731'
            point_entry_list[err_entries[1]]['bg'] = '#f7b731'

        messagebox.showerror(error_title, error_point[err_code])
        return False



    # Поиск треугольника с максимальной высотой
    ans_h, ans_triangle = find_max_height(points)
    if ans_triangle is None:
        for i in range(len(points)):
            point_entry_list[i]['bg'] = '#f7b731'
        messagebox.showerror(error_title, error_point[3])
        return False

    ans_points = [points[ans_triangle[0]], points[ans_triangle[1]], points[ans_triangle[2]]]
    # Поиск точки падения высоты
    H = find_h_xy(ans_points[0], ans_points[1], ans_points[2])



    # Отображение результата
    point_entry_list[ans_triangle[0]]['bg'] = '#20bf6b'
    point_entry_list[ans_triangle[1]]['bg'] = '#20bf6b'
    point_entry_list[ans_triangle[2]]['bg'] = '#20bf6b'

    define_borders(ans_points[0], ans_points[1], ans_points[2], H)

    ## Координатные оси
    canvas.create_line(adp_x(x_min), adp_y(0),
                       adp_x(x_max), adp_y(0),
                       fill='grey', dash=(3, 1), arrow='last')
    canvas.create_line(adp_x(0), adp_y(y_min),
                       adp_x(0), adp_y(y_max),
                       fill='grey', dash=(3, 1), arrow='last')

    ## Точки
    for i in [ans_points[0], ans_points[1], ans_points[2], H]:
        canvas.create_oval(adp_xy(i), adp_xy(i), width=3)

    ## Надписи
    canvas.create_text(text_xy(ans_points[0], -5),
                       text="P{} ({:.2f}, {:.2f})".format(ans_triangle[0] + 1,
                                                          ans_points[0]['x'],
                                                          ans_points[0]['y']))
    canvas.create_text(text_xy(ans_points[1], -5),
                       text="P{} ({:.2f}, {:.2f})".format(ans_triangle[1] + 1,
                                                          ans_points[1]['x'],
                                                          ans_points[1]['y']))
    canvas.create_text(text_xy(ans_points[2], -5),
                       text="P{} ({:.2f}, {:.2f})".format(ans_triangle[2] + 1,
                                                          ans_points[2]['x'],
                                                          ans_points[2]['y']))
    canvas.create_text(text_xy(H, 10), fill='red',
                       text="H ({:.2f}, {:.2f})".format(H['x'], H['y']))

    ## Линии
    canvas.create_line(adp_xy(ans_points[0]), adp_xy(ans_points[1]),
                       adp_xy(ans_points[2]), adp_xy(ans_points[0]),
                       fill='#40407a')
    canvas.create_line(adp_xy(ans_points[0]), adp_xy(H), fill='red')
    canvas.create_line(adp_xy(ans_points[1]), adp_xy(H),
                       fill='#40407a', dash=(1, 10), width=0.1)

    messagebox.showinfo("Решение", "Максимальная высота - из точки №{:} треугольника {:}-{:}-{:} \nВысота равна {:.3f}".format(ans_triangle[0], ans_triangle[0], ans_triangle[1], ans_triangle[2], ans_h))


def show_task():
    messagebox.showinfo(task_title, task_text)


def show_point_format():
    messagebox.showinfo(point_format_title, point_format_text)


main = Tk()

main_menu = Menu(main)
main_menu.add_command(label=task_title, command=show_task)
main_menu.add_command(label=point_format_title, command=show_point_format)


main_frame = Frame(main, bg=bg_color_main)
main_frame.place(x=15, y=15)

point_entry_list = []

# Заголовок
point_title_label = Label(main_frame, text=point_title_text,
                          bg=bg_color_main, font=main_font)
# Поле ввода точек
point_frame = Frame(main_frame, bg=bg_color_main)

point_frame_title = Frame(point_frame, bg=bg_color_main)
Button(point_frame_title, text='Удалить все точки', command=clear_point_entry).grid(row=0, column=0, columnspan=3, sticky="NSWE")
Label(point_frame_title, text='x', bg=bg_color_main, relief=GROOVE,
      font=main_font, width=point_width).grid(row=1, column=0, sticky="NSWE")
Label(point_frame_title, text='y', bg=bg_color_main, relief=GROOVE,
      font=main_font, width=point_width).grid(row=1, column=1, sticky="NSWE")
Button(point_frame_title, text='+', width=3, command=add_point_entry).grid(row=1, column=2, padx=5)
point_frame_title.pack()


# Заголовок
canvas_title_label = Label(main_frame, text=canvas_title_text,
                           bg=bg_color_main, font=main_font)
calculate_button = Button(main_frame, text=calculate_text, font=main_font,
                          bg=bg_color_main, command=show_solution)
# Поле геометрического решения
canvas = Canvas(main_frame, width=canvas_x, height=canvas_y, bg=bg_color_main)


# Размещение виджетов
point_title_label.grid(row=0, column=0, sticky="NSWE", pady=5)
point_frame.grid(row=1, column=0, sticky="NW")
add_point_entry()
add_point_entry()
add_point_entry()

canvas_title_label.grid(row=0, column=1, sticky="NSWE", padx=20)
calculate_button.grid(row=0, column=2, sticky="NSWE", padx=20)
canvas.grid(row=1, column=1, rowspan=7, columnspan=2,
            sticky="NSWE", padx=20, pady=10)

canvas.create_line(10, 10, 200, 200, smooth = 1,
                       fill='black', stipple="gray50")
# canvas.create_rectangle(20, 50, 300, 100, outline="black", fill="red", width=2, stipple="gray50")

main.config(menu = main_menu)
main.title(window_title_text)
main.config(bg=bg_color_main)
# main.geometry('{}x{}+0+0'.format(x, y))
main.state('zoomed')
main.resizable(1, 1)
main.mainloop()
