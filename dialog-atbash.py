from customtkinter import * 
from tkinter import Text as tx
import tkinter as tk
from PIL import Image

root = CTk()
################                CONFIGURATION                 ####################
root.title("Шифр Атбаш")
root.geometry('430x400')
root.iconbitmap(bitmap=r'C:\Users\ariew\Projects\atbash-ng\source\ico.ico')

set_appearance_mode('dark')

default_font = CTkFont(family='Cascadia Code', size=14)
default_font_16 = CTkFont(family='Cascadia Code', size=16)
default_font_italic = CTkFont(family='Cascadia Code Italic', size=14)
default_font_italic_ul = CTkFont(family='Cascadia Code Italic', size=14, underline=True)
main_font = CTkFont(family='Anta', size=20)


################                FUNCTIONS                    #####################
def copy_to_clipboard(value : tk.Text):
    root.clipboard_clear()
    
    try: 
        text = value.get("1.0", tk.END)      
        text = bytes(text, 'utf-8').translate(None, b'\n').decode()     
        root.clipboard_append(text)
    except:
        pass    

def delete_value(value : tk.Text):
    try:
        value.delete("1.0", tk.END)
    except:
        pass

def encrypt(*args):
    dencypter_entry.delete(0.0, 'end')
    abc = alhabet_entry.get()
    
    s = encypter_entry.get(0.0, 'end')
    
    s = s.translate(str.maketrans(
        abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))
    
    dencypter_entry.insert(0.0, s)

def decrypt(*args):
    encypter_entry.delete(0.0, 'end')
    abc = alhabet_entry.get()
    
    s = dencypter_entry.get(0.0, 'end')
    
    s = s.translate(str.maketrans(
        abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))
    
    encypter_entry.insert(0.0, s)

def insert_alp(*args, alp : CTkEntry, lng : int):

    print('durak')

    alp.delete(0, "end")

    if lng == 0:
        alp.insert(string='абвгдеёжзийклмнопрстуфхцчшщъыьэюя', index=0)
    elif lng == 1: 
        alp.insert(string='abcdefghijklmnopqrstuvwxyz', index=0)
    elif lng == 2:
        alp.insert(string='abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                   index=0)
    else: 
        pass 
    


################                RESOURCES                    #####################
cp_btn_img = CTkImage(dark_image=Image.open(r'C:\Users\ariew\Projects\atbash-ng\source\cp_btn.png'),
                 size=(33, 33))

del_btn_img = CTkImage(dark_image=Image.open(r'C:\Users\ariew\Projects\atbash-ng\source\del_btn.png'),
                       size=(33, 33))

cp_btn_img_d = CTkImage(dark_image=Image.open(r'C:\Users\ariew\Projects\atbash-ng\source\cp_btn_d.png'),
                        size=(33, 33))

del_btn_img_d = CTkImage(dark_image=Image.open(r'C:\Users\ariew\Projects\atbash-ng\source\del_btn_d.png'),
                        size=(33, 33))


################                MAIN - LABEL                 #####################
main_lable = CTkLabel(root, width=410, height=40, corner_radius=0, bg_color='transparent',
                      fg_color='#242F40', text_color='#E3D7FF', text='Atbash cipher',
                      anchor='center', font=main_font)

main_lable.place(x=10, y=10)

alhabet_label = CTkLabel(master=root, width=300, height=20, corner_radius=0,
                         bg_color='transparent', fg_color='transparent',
                         text_color='#E3D7FF', anchor='w',
                         text='Алфавит', font=default_font_italic)

alhabet_label.place(x=10, y=59)


################                ENTRY'S                      #####################
encypter_entry = tx(master=root, foreground='white', 
                    width=44, height=7,
                    background='#283F3B', font=default_font)

encypter_entry.place(x=10, y=110)
encypter_entry.bind('<Any-KeyRelease>', encrypt)


dencypter_entry = tx(master=root, foreground='white', 
                    width=44, height=7,
                    background='#22223B', font=default_font)

dencypter_entry.place(x=10, y=250)
dencypter_entry.bind('<Any-KeyRelease>', decrypt)

alhabet_entry = CTkEntry(master=root, width=410, height=20,
                        corner_radius=5, bg_color='transparent',
                        fg_color='#242F40', text_color='#97C8EB',
                        state='normal', font=default_font)

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
                       fg_color='transparent', image=cp_btn_img_d, text='',
                       command=lambda: copy_to_clipboard(dencypter_entry))

cp_denc_btn.place(y=250, x=370)


del_denc_btn = CTkButton(master=root, width=33, height=33,
                       corner_radius=5, bg_color='transparent',
                       fg_color='transparent', image=del_btn_img_d, text='',
                       command=lambda: delete_value(dencypter_entry))

del_denc_btn.place(y=295, x=370)


select_alhabet_cyr = CTkButton(master=root, width=10, height=14,
                           bg_color='transparent',
                           fg_color='transparent',
                           text_color='#E3D7FF', text='rus', 
                           font=default_font_italic_ul,
                           command=lambda: insert_alp(alp=alhabet_entry, lng=0))

select_alhabet_cyr.place(x=293, y=54)


select_alhabet_eng = CTkButton(master=root, width=10, height=14,
                           bg_color='transparent',
                           fg_color='transparent',
                           text_color='#E3D7FF', text='eng', 
                           font=default_font_italic_ul,
                           command=lambda: insert_alp(alp=alhabet_entry, lng=1))

select_alhabet_eng.place(x=333, y=54)


select_alhabet_both = CTkButton(master=root, width=10, height=14,
                           bg_color='transparent',
                           fg_color='transparent',
                           text_color='#E3D7FF', text='both', 
                           font=default_font_italic_ul,
                           command=lambda: insert_alp(alp=alhabet_entry, lng=2))

select_alhabet_both.place(x=373, y=54)


root.mainloop()