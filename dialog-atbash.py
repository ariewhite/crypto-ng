from customtkinter import * 
from tkinter import Text as tx
import tkinter as tk
from PIL import Image

root = CTk()
root.title("Шифр Атбаш")
root.geometry('430x400')


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
    abc = alhabet_entry.get()
    
    s = encypter_entry.get(0.0, 'end')

    print(s, 'end')
    
    s = s.translate(str.maketrans(
        abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))
    
    print(s, 'end')

    dencypter_entry.insert(0.0, s)

def decrypt(*args):
    encypter_entry.delete(0.0, 'end')
    abc = alhabet_entry.get()
    
    s = dencypter_entry.get(0.0, 'end')
    
    s = s.translate(str.maketrans(
        abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))
    
    print(s)

    encypter_entry.insert(0.0, s)


################                RESOURCES                    #####################
cp_btn_img = CTkImage(dark_image=Image.open(r'C:\Users\ariew\Projects\atbash-ng\source\cp_btn.png'),
                 size=(33, 33))

del_btn_img = CTkImage(dark_image=Image.open(r'C:\Users\ariew\Projects\atbash-ng\source\del_btn.png'),
                       size=(33, 33))


################                MAIN - LABEL                 #####################
main_lable = CTkLabel(root, width=410, height=40, corner_radius=0, bg_color='transparent',
                      fg_color='#7A89C2', text_color='#E3D7FF', text='Atbash cipher',
                      anchor='center')

main_lable.place(x=10, y=10)

alhabet_label = CTkLabel(master=root, width=300, height=20, corner_radius=0,
                         bg_color='transparent', fg_color='transparent',
                         text_color='#BFD5E2', anchor='w',
                         text='Alpabet')

alhabet_label.place(x=10, y=60)


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

alhabet_entry = CTkEntry(master=root, width=410, height=20,
                        corner_radius=5, bg_color='transparent',
                        fg_color='#B2ABBF', text_color='#C7EBF0',
                        state='normal')

alhabet_entry.place(x=10, y=80)
alhabet_entry.insert(string='абвгдеёжзийклмнопрстуфхцчшщъыьэюя', index=0)


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


cp_denc_btn = CTkButton(master=root, width=33, height=33,
                       corner_radius=5, bg_color='transparent',
                       fg_color='transparent', image=cp_btn_img, text='',
                       command=lambda: copy_to_clipboard(dencypter_entry))

cp_denc_btn.place(y=250, x=370)


del_denc_btn = CTkButton(master=root, width=33, height=33,
                       corner_radius=5, bg_color='transparent',
                       fg_color='transparent', image=del_btn_img, text='',
                       command=lambda: delete_value(dencypter_entry))

del_denc_btn.place(y=295, x=370)


root.mainloop()
