import tkinter as tk


def input_box(win):
    dop = tk.Toplevel(win)
    # dop.geometry('200x60')    
    label = tk.Label(dop, text='Введите тираж')
    label.pack()
    inpt = tk.Entry(dop)
    inpt.pack()

    result = None  # Значение по-умолчанию (будет возвращено, например, если закрыть дочернее окно через крестик)
    def callback():
        nonlocal result  # nonlocal говорит, что переменная result является переменной внешней функции (в данном случае inputBox)
        result = inpt.get()
        dop.destroy()  # закрываем окно

    Button = tk.Button(dop, text='ок', command=callback)
    Button.pack()

    # Три строки ниже нужны, чтобы пока существует второе диалоговое окно, основное окно блокировалось 
    # (чтобы дочернее окно было модальным)
    dop.transient(win)
    dop.grab_set()
    dop.focus_set()

    dop.wait_window()  # ждем закрытия окна
    return result

    
win = tk.Tk()

def show_result():
    res = input_box(win)
    label_result.config(text=res)


tk.Button(text="Show input box", command=show_result).pack()
label_result = tk.Label()
label_result.pack()

win.mainloop()
