# A/B калькулятор

import tkinter as tk

#Функция закрытия программы
def do_close():
    root.destroy()
    
#Создание главного окна
root = tk.Tk()
root.geometry("280x300")
root.title("A/B калькулятор")

#Добавление метки заголовка
lblTitle = tk.Label(text="A/B калькулятор", font = ('Helvetica',16,'bold'), fg='#0000cc')
lblTitle.place(x=55,y=25)

#Добавление кнопки Рассчитать
btnProcess = tk.Button(root, text = "Рассчитать", font = ('Helvetica',10,'bold'),fg='#0000FF')
btnProcess.place(x=25, y=250, width=90, height=30)

#Добавление кнопки закрытия программы
btnClose = tk.Button(root, text = "Закрыть", font = ('Helvetica',10,'bold'), command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)

#Запуск цикла mainloop
root.mainloop()
