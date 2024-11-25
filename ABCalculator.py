# A/B калькулятор

import tkinter as tk
from tkinter import messagebox as mb
import os
import math

#Функция закрытия программы
def do_close():
    root.destroy()
    
#Функция форматирвания процентов
def num_percent(num):
    return"{:.2f}".format(num*100).rjust(10)+'%'
    
def do_processing():
    #Считывание данных из полей ввода
    n1 = int(entVisitors1.get())
    c1 = int(entConversion1.get())
    n2 = int(entVisitors2.get())
    c2 = int(entConversion2.get())
    
    #Проверка данных из полей ввода
    if n1<=0 or n2<=0:
        mb.showerror(title="Ошибка",message="Неверное количество поситителей")
        return
    
    popup_window(n1,c1,n2,c2)
    
#Функция вызова окна результатов
def popup_window(n1,c1,n2,c2):
    window = tk.Toplevel()
    window.geometry("500x500")
    window.title("A/B результат")
    
    #Добавление окна вывода текста
    txtOutput = tk.Text(window, font = ('Courier new',10,'bold'))
    txtOutput.place(x=15,y=115,width=470,height=300)
    
    #Добавление заголовк
    txtOutput.insert(tk.END,'                            Контрольная     Тестовая' + os.linesep)
    txtOutput.insert(tk.END,'                            группа          группа' + os.linesep)
    txtOutput.insert(tk.END,'----------------------------------------------------' + os.linesep)
    
    #Добавление вывода конверсии и стандартного отлонения
    p1=c1/n1
    p2=c2/n2
    txtOutput.insert(tk.END, 'Конверсия              ' + num_percent(p1) + '      '+ num_percent(p2)+ os.linesep)
    txtOutput.insert(tk.END,'----------------------------------------------------' + os.linesep)
    
    sigma1=math.sqrt(p1*(1-p1)/n1)  
    sigma2=math.sqrt(p2*(1-p2)/n2)
    txtOutput.insert(tk.END, 'Стандартное отклонение ' + num_percent(sigma1) + '      '+ num_percent(sigma2)+ os.linesep)
    txtOutput.insert(tk.END,'----------------------------------------------------' + os.linesep)
    
    #Добавление вывода возможных разбросов
    z1 = 1.96
    lower1_95 = p1-z1*sigma1
    if lower1_95 < 0:
        lower1_95=0
    upprel1_95 = p1+z1*sigma1
    if upprel1_95>1:
        upprel1_95 = 1
        
    lower2_95 = p2-z1*sigma2
    if lower2_95 < 0:
        lower2_95=0
    upprel2_95 = p2+z1*sigma2
    if upprel2_95>1:
        upprel2_95 = 1
    
    txtOutput.insert(tk.END,'95% возможный разброс  '+os.linesep)
    txtOutput.insert(tk.END,'                       от '+num_percent(lower1_95)+'    '+ num_percent(lower2_95)+os.linesep)
    txtOutput.insert(tk.END,'                       до '+num_percent(upprel1_95)+'    '+ num_percent(upprel2_95)+os.linesep)    
    txtOutput.insert(tk.END,'----------------------------------------------------' + os.linesep)    
    
    z2 = 2.575
    lower1_99 = p1-z2*sigma1
    if lower1_99 < 0:
        lower1_99=0
    upprel1_99 = p1+z2*sigma1
    if upprel1_99>1:
        upprel1_99 = 1
        
    lower2_99 = p2-z2*sigma2
    if lower2_99 < 0:
        lower2_99=0
    upprel2_99 = p2+z2*sigma2
    if upprel2_99>1:
        upprel2_99 = 1
    
    txtOutput.insert(tk.END,'99% возможный разброс  '+os.linesep)
    txtOutput.insert(tk.END,'                       от '+num_percent(lower1_99)+'    '+ num_percent(lower2_99)+os.linesep)
    txtOutput.insert(tk.END,'                       до '+num_percent(upprel1_99)+'    '+ num_percent(upprel2_99)+os.linesep)    
    txtOutput.insert(tk.END,'----------------------------------------------------' + os.linesep)    
    
    #Добавление кнопки закрытия окна
    btnClosePopup = tk.Button(window, text = "Закрыть", font = ('Helvetica',10,'bold'), command=window.destroy)
    btnClosePopup.place(x=190, y=450, width=90, height=30)
    
    #Перевод фокуса на соданное окно
    window.focus_force()
    
    
#Создание главного окна
root = tk.Tk()
root.geometry("280x300")
root.title("A/B калькулятор")

#Добавление метки заголовка
lblTitle = tk.Label(text="A/B калькулятор", font = ('Helvetica',16,'bold'), fg='#0000cc')
lblTitle.place(x=55,y=20)

#Добавление метки заголовка контрольной группы
lblTitle1 = tk.Label(text="Контрольная группа", font = ('Helvetica',12,'bold'), fg='#0066ff')
lblTitle1.place(x=25,y=55)

#Добавление полей ввода контрольной группы
lblVisitors1 = tk.Label(text="Посетители:", font = ('Helvetica',10,'bold'))
lblVisitors1.place(x=25,y=85)

entVisitors1 = tk.Entry(font = ('Helvetica',10,'bold'),justify='center')
entVisitors1.place(x=115, y=85, width=90, height=20)
entVisitors1.insert(tk.END,'255')

lblConversion1 = tk.Label(text="Конверсии:", font = ('Helvetica',10,'bold'))
lblConversion1.place(x=25,y=115)

entConversion1 = tk.Entry(font = ('Helvetica',10,'bold'),justify='center')
entConversion1.place(x=115, y=115, width=90, height=20)
entConversion1.insert(tk.END,'26')

#Добавление метки заголовка тестовой группы
lblTitle2 = tk.Label(text="Контрольная группа", font = ('Helvetica',12,'bold'), fg='#008800')
lblTitle2.place(x=25,y=145)

#Добавление полей ввода тестовой группы
lblVisitors2 = tk.Label(text="Посетители:", font = ('Helvetica',10,'bold'))
lblVisitors2.place(x=25,y=175)

entVisitors2 = tk.Entry(font = ('Helvetica',10,'bold'),justify='center')
entVisitors2.place(x=115, y=175, width=90, height=20)
entVisitors2.insert(tk.END,'235')

lblConversion2 = tk.Label(text="Конверсии:", font = ('Helvetica',10,'bold'))
lblConversion2.place(x=25,y=205)

entConversion2 = tk.Entry(font = ('Helvetica',10,'bold'),justify='center')
entConversion2.place(x=115, y=205, width=90, height=20)
entConversion2.insert(tk.END,'18')

#Добавление кнопки Рассчитать
btnProcess = tk.Button(root, text = "Рассчитать", font = ('Helvetica',10,'bold'), command=do_processing, fg="#0044CC")
btnProcess.place(x=25, y=250, width=90, height=30)

#Добавление кнопки закрытия программы
btnClose = tk.Button(root, text = "Закрыть", font = ('Helvetica',10,'bold'), command=do_close)
btnClose.place(x=160, y=250, width=90, height=30)

#Запуск цикла mainloop
root.mainloop()
