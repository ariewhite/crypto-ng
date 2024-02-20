from customtkinter import * 
from tkinter import Text as tx
import tkinter as tk
from PIL import Image

root = CTk()
root.title("Шифр Атбаш")
root.geometry('430x385')


################                FUNCTIONS                    #####################
def copy_to_clipboard(value : tk.Text):
    root.clipboard_clear()
    try: 
        text = value.get("1.0", tk.END)
        root.clipboard_append(text)
    except:
        print(f'error to append {value} to clipboard')

def delete_value(value : tk.Text):
    try:
        value.delete("1.0", tk.END)
    except:
        print(f'error to delete VALUE-{value}')

def encrypt(*args):
    dencypter_entry.delete(0.0, 'end')
    value = encypter_entry.get(0.0, 'end')
    temp = ""
    for i in range(len(value)):
        if value[i]!=" " and value[i]!='\n' and value[i]!="\t":
            if ord(value[i]) in range(97,123):
                temp += chr(96 + 26-(ord(value[i])-97))
            elif ord(value[i]) in range(65,91):
                temp += chr(64 + 26-(ord(value[i])-65))
            else:
                temp += value[i]
        else:
            temp += value[i]
    dencypter_entry.insert(0.0, temp)

def decrypt(*args):
    encypter_entry.delete(0.0, 'end')
    value = dencypter_entry.get(0.0, 'end')
    temp=""
    for i in range(len(value)):
        if value[i]!=" " and value[i]!='\n'and value[i]!="\t":
            if ord(value[i]) in range(97,123):
                temp += chr(96 + 26-(ord(value[i])-97))
            elif ord(value[i]) in range(65,91):
                temp += chr(64 + 26-(ord(value[i])-65))
            else:
                temp += value[i]
        else:
            temp += value[i]
    encypter_entry.insert(0.0, temp)


################                RESOURCES                    #####################
cp_btn_img = CTkImage(dark_image=Image.open(r'C:\Users\ariew\Projects\atbash-ng\source\cp_btn.png'),
                 size=(33, 33))

del_btn_img = CTkImage(dark_image=Image.open(r'C:\Users\ariew\Projects\atbash-ng\source\del_btn.png'),
                       size=(33, 33))


################                MAIN - LABEL                 #####################
main_lable = CTkLabel(root, width=410, height=80, corner_radius=0, bg_color='transparent',
                      fg_color='#7A89C2', text_color='#E3D7FF', text='Atbash cipher',
                      anchor='center')

main_lable.place(x=10, y=10)


################                ENTRY'S                      #####################
encypter_entry = tx(master=root, foreground='white', 
                    width=44, height=7,
                    background='#466060')

encypter_entry.place(x=10, y=110)
encypter_entry.bind('<Any-KeyRelease>', encrypt)


dencypter_entry = tx(master=root, foreground='white', 
                    width=44, height=7,
                    background='#496A81')

dencypter_entry.place(x=10, y=250)
dencypter_entry.bind('<Any-KeyRelease>', decrypt)


################                BUTTONS'S                    #####################
cp_enc_btn = CTkButton(master=root, width=33, height=33,
                       corner_radius=5, bg_color='transparent',
                       fg_color='transparent', image=cp_btn_img, text='',
                       command=lambda: copy_to_clipboard(encypter_entry))

cp_enc_btn.place(y=110, x=370)


del_enc_btn = CTkButton(master=root, width=33, height=33,
                       corner_radius=5, bg_color='transparent',
                       fg_color='transparent', image=del_btn_img, text='',
                       command=lambda: delete_value(encypter_entry))

del_enc_btn.place(y=155, x=370)


root.mainloop()
