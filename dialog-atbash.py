from customtkinter import * 
from tkinter import 

root = CTk()
root.title("Шифр Атбаш")
root.geometry('430x455')


def copy_text():
    print('yes')

def clear_text():
    print('no')


# Label
main_lable = CTkLabel(root, width=410, height=80, corner_radius=5, bg_color='transparent',
                      fg_color='#7A89C2', text_color='#E3D7FF', text='Atbash cipher',
                      anchor='center')

main_lable.place(x=10, y=10)


encypter_entry = CTkEntry(master=root, width=350, height=160, 
                          corner_radius=5, 
                          bg_color='transparent', fg_color='#466060',
                          text_color='#FFFFFF', 
                          state='normal')

encypter_entry.place(x=10, y=110)


dencypter_entry = CTkEntry(master=root, width=350, height=160, 
                          corner_radius=5, 
                          bg_color='transparent', fg_color='#496A81',
                          text_color='#FFFFFF', 
                          state='normal')

dencypter_entry.place(x=10, y=280)





# Запуск цикла обработки событий
root.mainloop()
