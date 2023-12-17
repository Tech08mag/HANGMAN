import random
from tkinter import *

words = ["PASSWORT", "CODE", "LOST", ]

def new_word():
    global word, display
    word = random.choice(words)
    display = len(word) * "-"
    word_label.config(text=display)

def check():
    global display
    display_list = list(display)

    for i in range (len(word)):
        if word[i] == key.get():
            display_list[i] = word[i]
    display = "".join(display_list)
    word_label.config(text=display)

window = Tk()

word_label = Label(master=window,
                   font=('Courier',20), width=28)

new_button = Button(master=window, text='Neues Wort',
                    command=new_word, font=("Arial", 14),
                    bg="black", fg="white")

key = StringVar(master=window)
key_rbs = [Radiobutton(master=window, command=check,
                       font=("Arial",14), width=3,
                       variable=key, value=ch,
                       text=ch, indicatoron=False)
                       for ch in "QWERTZUIOPÜASDFGHJKLÖÄYXCVBNM"]

word_label.grid(column=0, row=0, columnspan=10)
for i in range(11):
    key_rbs[i].grid(row=1, column=i)

for i in range(11, 22):
    key_rbs[i].grid(row=2, column=i-11)

for i in range(22, 28):
    key_rbs[i].grid(row=3, column=i-21)
new_button.grid(column=8, row=4,
                columnspan=3, sticky=E)

new_word()
window.mainloop()