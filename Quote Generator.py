from tkinter import * # библиотека графического интерфейса
from PIL import ImageTk, Image # библиотеки для заднего фона
import random # для рандомной генерации цитат

f = open("quotes.txt", "r")
quotes = f.readlines() # файл с цитатами
NumTest = -1 # для дальнейшей проверки

def againprint():
    text.destroy()
    printquote() # удаление канваса для создания нового

def printquote(): # вывод цитаты
    global text, NumTest
    canvas = Canvas(window)
    text = Text(window, width=20, height=4, font="Arial 14")
    text.pack(fill="both", expand=True, anchor="s")
    def typequote(widget, index, string):
        if len(string) > 0:
            widget.insert(index, string[0])
            if len(string) > 1:
                # compute index of next char
                index = widget.index("%s + 1 char" % index)
                # type the next character in half a second
                widget.after(60, typequote, widget, index, string[1:])
    NumQuote = random.randint(0, 10)
    while NumQuote == NumTest: # проверка чтобы не попадались одинаковые
        NumQuote = random.randint(0, 10)
    NumTest = NumQuote
    canvas.create_text(5, 100, text=typequote(text, "0.5", quotes[NumQuote]), fill="Yellow", font="Verdana 14")
    Button(window, image=button_image, command=againprint).place(x=180, y=200) #кнопка

# окно
window = Tk()# создание окна
window.title("генератор цитат")  # титульное название программы
window.geometry('+450+150')  # размеры окна
window.iconbitmap('icon.ico')  # иконка
window.resizable(width=False, height=False) # запрет на изменение разрешения окна

# задний фон
path = "background.png"
img = Image.open(path)
width = 500
ratio = (width / float(img.size[0]))
height = int((float(img.size[1]) * float(ratio)))
imag = img.resize((width, height))
image = ImageTk.PhotoImage(imag)
panel = Label(window, image=image)
panel.pack(side="top", fill="both")

# кнопка вывода цитаты
button_image = PhotoImage(file='button.png') # фото кнопки
Button(window, image=button_image, command=printquote).place(x=180, y=200) #кнопка

window.mainloop()